"""
TidyUUUUp - 自动更新模块
启动时检查版本，有更新自动下载
"""

import os
import sys
import json
import tempfile
import shutil
import urllib.request
import urllib.error
from PyQt5.QtCore import QThread, pyqtSignal, QObject


# ==================== 配置区域 ====================

# 当前版本号（发版时更新这里）
CURRENT_VERSION = "1.0.3"

# 版本信息文件地址（你发布新版本的地方）
# 你可以把 version.json 放到任何能直接访问的地方：
#   - GitHub Raw: https://raw.githubusercontent.com/你的用户名/仓库/main/version.json
#   - Gitee Raw:  https://gitee.com/你的用户名/仓库/raw/main/version.json
#   - 你的服务器: https://你的域名/version.json
VERSION_CHECK_URL = "https://raw.githubusercontent.com/BigCake2026/TidyUUUUp/main/v1.0.3/version.json"

# ==================================================


class UpdateChecker(QThread):
    """版本检查线程"""

    check_finished = pyqtSignal(bool, dict)  # (是否有更新, 信息字典)
    error_occurred = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        try:
            req = urllib.request.Request(
                VERSION_CHECK_URL,
                headers={'User-Agent': 'TidyUUUUp-Updater/1.0'}
            )

            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode('utf-8'))

            latest_version = data.get('version', '0.0.0')
            has_update = self._compare_versions(latest_version, CURRENT_VERSION)

            info = {
                'current_version': CURRENT_VERSION,
                'latest_version': latest_version,
                'download_url': data.get('download_url', ''),
                'changelog': data.get('changelog', ''),
                'force_update': data.get('force_update', False),
                'file_size': data.get('file_size', ''),
                'publish_date': data.get('publish_date', ''),
            }

            self.check_finished.emit(has_update, info)

        except urllib.error.URLError as e:
            self.error_occurred.emit(f"网络连接失败: {e}")
        except json.JSONDecodeError as e:
            self.error_occurred.emit(f"版本信息解析失败: {e}")
        except Exception as e:
            self.error_occurred.emit(f"检查更新失败: {e}")

    def _compare_versions(self, v1, v2):
        """比较版本号，v1 > v2 返回 True"""
        try:
            parts1 = [int(x) for x in v1.split('.')]
            parts2 = [int(x) for x in v2.split('.')]
            for a, b in zip(parts1, parts2):
                if a > b:
                    return True
                elif a < b:
                    return False
            return len(parts1) > len(parts2)
        except Exception:
            return False


class UpdateDownloader(QThread):
    """更新下载线程"""

    progress = pyqtSignal(int)  # 下载进度 0-100
    download_finished = pyqtSignal(bool, str)  # (是否成功, 文件路径或错误信息)

    def __init__(self, download_url):
        super().__init__()
        self.download_url = download_url

    def run(self):
        try:
            tmp_dir = tempfile.gettempdir()
            tmp_file = os.path.join(tmp_dir, f"nexus-dock-update-{os.getpid()}.zip")

            req = urllib.request.Request(
                self.download_url,
                headers={'User-Agent': 'TidyUUUUp-Updater/1.0'}
            )

            with urllib.request.urlopen(req, timeout=60) as response:
                total_size = int(response.headers.get('Content-Length', 0))
                downloaded = 0

                with open(tmp_file, 'wb') as f:
                    while True:
                        chunk = response.read(8192)
                        if not chunk:
                            break
                        f.write(chunk)
                        downloaded += len(chunk)

                        if total_size > 0:
                            percent = int(downloaded * 100 / total_size)
                            self.progress.emit(percent)

            self.progress.emit(100)
            self.download_finished.emit(True, tmp_file)

        except Exception as e:
            self.download_finished.emit(False, str(e))


def apply_update(update_file, app_dir):
    """应用更新（支持EXE版本和源码版本）"""
    try:
        import zipfile

        if not os.path.exists(update_file):
            return False, "更新文件不存在"

        # 判断当前是EXE模式还是源码模式
        is_exe_mode = getattr(sys, 'frozen', False)

        # 创建备份目录
        backup_dir = os.path.join(app_dir, f"_backup_{CURRENT_VERSION}")
        if os.path.exists(backup_dir):
            shutil.rmtree(backup_dir, ignore_errors=True)

        if not is_exe_mode:
            # ========== 源码模式：备份所有文件 ==========
            os.makedirs(backup_dir, exist_ok=True)
            for item in os.listdir(app_dir):
                src = os.path.join(app_dir, item)
                dst = os.path.join(backup_dir, item)
                if item.startswith('_backup') or item == backup_dir:
                    continue
                if os.path.isdir(src):
                    shutil.copytree(src, dst, dirs_exist_ok=True)
                else:
                    shutil.copy2(src, dst)

        # 解压更新文件
        with zipfile.ZipFile(update_file, 'r') as zf:
            # 检查zip内容，找到正确的目录
            root_dirs = set()
            has_exe = False
            for name in zf.namelist():
                parts = name.split('/')
                if len(parts) > 1:
                    root_dirs.add(parts[0])
                if name.lower().endswith('.exe'):
                    has_exe = True

            # 如果zip里有一个根目录，用它作为基准
            if len(root_dirs) == 1:
                root_prefix = list(root_dirs)[0] + '/'
            else:
                root_prefix = ''

            for member in zf.infolist():
                if member.filename.startswith(root_prefix):
                    target_path = member.filename[len(root_prefix):]
                    if not target_path:
                        continue

                    full_path = os.path.join(app_dir, target_path)

                    if member.is_dir():
                        os.makedirs(full_path, exist_ok=True)
                    else:
                        os.makedirs(os.path.dirname(full_path), exist_ok=True)
                        with zf.open(member) as src, open(full_path, 'wb') as dst:
                            dst.write(src.read())

        if is_exe_mode and has_exe:
            return True, "更新成功，请重启软件（EXE已自动替换）"
        else:
            return True, "更新成功，请重启软件"

    except Exception as e:
        return False, f"更新失败: {e}"
