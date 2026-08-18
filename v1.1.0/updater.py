"""
TidyUUUUp - GitHub 更新检测与下载

设计要点：
  1. 通过 GitHub Releases API（GET /repos/{owner}/{repo}/releases/latest）检测最新版本，
     解析 tag_name（如 "v1.0.12"、"1.1.0"），与当前版本做语义化比较。
  2. 支持任意高位版本检测：1.0.11 < 1.0.12 < 1.1.0 < 2.0.0，自动识别 "v" 前缀。
  3. 全程后台线程，不阻塞 UI；通过 Qt 信号通知结果。
  4. 下载更新包到用户「下载」目录，绝不触碰用户设置目录（settings.json），
     从而在更新时保留全部用户数据。
  5. 不自动覆盖正在运行的程序（Windows 文件锁会导致失败）；下载完成后引导用户
     手动解压/安装或打开 Release 页面，确保可用与安全。
  6. 无需任何 token：使用未认证 GitHub API（60 次/小时/IP，桌面应用足够），
     带合规 User-Agent 头（GitHub 强制要求）。
"""
import os
import re
import json
import urllib.request
import urllib.error
from PyQt6.QtCore import QThread, pyqtSignal, QStandardPaths


CURRENT_VERSION = "1.1.0"
USER_AGENT = "TidyUUUUp-Updater/1.1.0 (+https://github.com/BigCake2026/TidyUUUUp)"


# ==========================================
# 语义化版本比较
# ==========================================
def parse_version(v: str):
    """把 'v1.0.12' / '1.1.0' / '1.0.12-beta' 解析为可比较的元组 (major, minor, patch, pre)。
    pre 为空表示正式版（比任何预发布版大）。"""
    if v is None:
        return (0, 0, 0, "")
    s = str(v).strip().lstrip("vV").strip()
    # 拆出预发布标识
    pre = ""
    if "-" in s:
        s, pre = s.split("-", 1)
        pre = pre.strip()
    parts = re.split(r"[.\s]+", s)
    nums = []
    for p in parts:
        try:
            nums.append(int(p))
        except ValueError:
            nums.append(0)
    while len(nums) < 3:
        nums.append(0)
    # 正式版 pre="" 排在预发布之后（更大）
    return (nums[0], nums[1], nums[2], 0 if pre == "" else -1, pre)


def is_newer(latest: str, current: str) -> bool:
    """latest 是否高于 current。"""
    try:
        return parse_version(latest) > parse_version(current)
    except Exception:
        return False


# ==========================================
# 更新检测线程
# ==========================================
class UpdateChecker(QThread):
    """后台检测 GitHub 最新 Release。"""

    # (有更新?, 信息字典)
    check_finished = pyqtSignal(bool, dict)
    check_error = pyqtSignal(str)

    def __init__(self, repo: str = "BigCake2026/TidyUUUUp",
                 current_version: str = CURRENT_VERSION, parent=None):
        super().__init__(parent)
        self.repo = repo
        self.current_version = current_version
        self._cancel = False

    def cancel(self):
        self._cancel = True

    def run(self):
        try:
            info = self._fetch_latest()
            if info is None:
                self.check_error.emit("未能解析到任何发布版本")
                return
            latest = info.get("latest_version", "0.0.0")
            has_update = is_newer(latest, self.current_version)
            info["current_version"] = self.current_version
            info["repo"] = self.repo
            self.check_finished.emit(has_update, info)
        except urllib.error.URLError as e:
            self.check_error.emit(f"网络连接失败：{e.reason if hasattr(e, 'reason') else e}")
        except Exception as e:
            self.check_error.emit(f"检查更新失败：{e}")

    def _fetch_latest(self) -> dict | None:
        url = f"https://api.github.com/repos/{self.repo}/releases/latest"
        req = urllib.request.Request(url, headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/vnd.github+json",
        })
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))

        tag = (data.get("tag_name") or "").strip()
        if not tag:
            return None

        # 优先选取 zip 资源，其次源码 zipball，最后 release html_url
        download_url = ""
        asset_name = ""
        for asset in data.get("assets", []) or []:
            name = asset.get("name", "")
            if name.lower().endswith(".zip"):
                download_url = asset.get("browser_download_url", "")
                asset_name = name
                break
        if not download_url:
            download_url = data.get("zipball_url", "")
            asset_name = "source.zip"
        if not download_url:
            download_url = data.get("html_url", "")

        return {
            "latest_version": tag.lstrip("vV"),
            "latest_tag": tag,
            "download_url": download_url,
            "asset_name": asset_name,
            "release_url": data.get("html_url", ""),
            "changelog": data.get("body", "") or "暂无更新说明",
            "publish_date": (data.get("published_at") or "")[:10],
            "is_prerelease": bool(data.get("prerelease", False)),
        }


# ==========================================
# 更新下载线程
# ==========================================
class UpdateDownloader(QThread):
    """下载更新包到用户下载目录（保留用户数据：绝不写入设置目录）。"""

    progress = pyqtSignal(int)            # 0-100
    download_finished = pyqtSignal(bool, str)  # (成功?, 文件路径或错误)

    def __init__(self, download_url: str, suggested_name: str = "", parent=None):
        super().__init__(parent)
        self.download_url = download_url
        self.suggested_name = suggested_name

    def run(self):
        try:
            dest_dir = QStandardPaths.writableLocation(
                QStandardPaths.StandardLocation.DownloadLocation)
            if not dest_dir:
                dest_dir = os.path.join(os.path.expanduser("~"), "Downloads")
            os.makedirs(dest_dir, exist_ok=True)

            name = self.suggested_name or os.path.basename(self.download_url) or "tidyuuuup_update.zip"
            # 规范扩展名：已有扩展名则保留；zipball_url（无扩展名）补 .zip
            if "." not in os.path.basename(name):
                name += ".zip"
            dest = os.path.join(dest_dir, name)
            # 避免覆盖同名
            base, ext = os.path.splitext(name)
            i = 1
            while os.path.exists(dest):
                dest = os.path.join(dest_dir, f"{base}_{i}{ext}")
                i += 1

            req = urllib.request.Request(self.download_url, headers={
                "User-Agent": USER_AGENT,
            })
            with urllib.request.urlopen(req, timeout=60) as response:
                total = int(response.headers.get("Content-Length", 0))
                downloaded = 0
                with open(dest, "wb") as f:
                    while True:
                        chunk = response.read(64 * 1024)
                        if not chunk:
                            break
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total > 0:
                            self.progress.emit(int(downloaded * 100 / total))
            self.progress.emit(100)
            self.download_finished.emit(True, dest)
        except Exception as e:
            self.download_finished.emit(False, str(e))
