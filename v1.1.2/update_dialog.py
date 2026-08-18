"""
TidyUUUUp - 更新对话框（PyQt6）

深色玻璃风格，与灵动岛 Dock 视觉一致。
支持：查看更新内容 / 下载（带进度）/ 跳过此版本 / 打开 Release 页面。
下载仅写入用户「下载」目录，绝不触碰用户设置目录，确保用户数据保留。
"""
import os
import sys
import subprocess
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QColor, QPainterPath
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QProgressBar, QTextEdit, QWidget, QApplication
)

from updater import UpdateDownloader
from settings import UserSettings


class UpdateDialog(QDialog):
    def __init__(self, update_info: dict, settings: UserSettings, parent=None):
        super().__init__(parent)
        self.update_info = update_info
        self.settings = settings
        self.downloader = None
        self._finished = False

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(540, 450)

        self._build_ui()

    # ---------- UI ----------
    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)

        container = QWidget()
        container.setObjectName("container")
        container.setStyleSheet("""
            #container {
                background: rgba(28, 28, 32, 0.98);
                border: 1px solid rgba(255, 255, 255, 0.12);
                border-radius: 22px;
            }
        """)
        inner = QVBoxLayout(container)
        inner.setContentsMargins(28, 28, 28, 24)
        inner.setSpacing(14)

        title = QLabel("✨  发现新版本")
        title.setStyleSheet("color:#FFFFFF; font-size:22px; font-weight:700;")
        inner.addWidget(title)

        cur = self.update_info.get("current_version", "")
        latest = self.update_info.get("latest_version", "")
        date = self.update_info.get("publish_date", "")
        ver_html = (f"v{cur}  →  "
                    f"<span style='color:#0A84FF; font-weight:700;'>v{latest}</span>")
        if date:
            ver_html += f"  <span style='color:rgba(255,255,255,0.4); font-size:12px;'>({date})</span>"
        ver = QLabel(ver_html)
        ver.setTextFormat(Qt.TextFormat.RichText)
        ver.setStyleSheet("color:rgba(255,255,255,0.75); font-size:14px;")
        inner.addWidget(ver)

        repo = self.update_info.get("repo", "")
        if repo:
            rl = QLabel(f"📂 来源：github.com/{repo}")
            rl.setStyleSheet("color:rgba(255,255,255,0.45); font-size:12px;")
            inner.addWidget(rl)

        ct = QLabel("📝  更新内容")
        ct.setStyleSheet("color:#FFFFFF; font-size:15px; font-weight:600; margin-top:4px;")
        inner.addWidget(ct)

        self.changelog = QTextEdit()
        self.changelog.setReadOnly(True)
        self.changelog.setPlainText(self.update_info.get("changelog", "暂无更新说明"))
        self.changelog.setFixedHeight(150)
        self.changelog.setStyleSheet("""
            QTextEdit {
                background: rgba(255,255,255,0.05);
                color: rgba(255,255,255,0.85);
                border: 1px solid rgba(255,255,255,0.08);
                border-radius: 12px;
                padding: 12px 14px;
                font-size: 13px;
            }
        """)
        inner.addWidget(self.changelog)

        self.progress = QProgressBar()
        self.progress.setFixedHeight(8)
        self.progress.setTextVisible(False)
        self.progress.setRange(0, 100)
        self.progress.hide()
        self.progress.setStyleSheet("""
            QProgressBar { background: rgba(255,255,255,0.08); border:none; border-radius:4px; }
            QProgressBar::chunk {
                background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
                    stop:0 #0A84FF, stop:1 #5AC8FA);
                border-radius:4px;
            }
        """)
        inner.addWidget(self.progress)

        self.status = QLabel("")
        self.status.setStyleSheet("color:rgba(255,255,255,0.55); font-size:12px;")
        self.status.hide()
        inner.addWidget(self.status)

        inner.addStretch()

        btns = QHBoxLayout()
        btns.setSpacing(12)

        self.later_btn = QPushButton("稍后安装")
        self.later_btn.setFixedHeight(42)
        self.later_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.later_btn.setStyleSheet(self._ghost_btn_css())
        self.later_btn.clicked.connect(self.reject)
        btns.addWidget(self.later_btn)

        self.action_btn = QPushButton("立即下载更新")
        self.action_btn.setFixedHeight(42)
        self.action_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.action_btn.setStyleSheet(self._primary_btn_css())
        self.action_btn.clicked.connect(self._start_download)
        btns.addWidget(self.action_btn)

        inner.addLayout(btns)
        root.addWidget(container)

    def _ghost_btn_css(self):
        return """
            QPushButton {
                background: rgba(255,255,255,0.08); color: rgba(255,255,255,0.8);
                border:none; border-radius:12px; font-size:14px; font-weight:600; padding:0 20px;
            }
            QPushButton:hover { background: rgba(255,255,255,0.16); }
            QPushButton:disabled { background: rgba(255,255,255,0.05); color: rgba(255,255,255,0.3); }
        """

    def _primary_btn_css(self):
        return """
            QPushButton {
                background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
                    stop:0 #0A84FF, stop:1 #5AC8FA);
                color:#FFFFFF; border:none; border-radius:12px;
                font-size:14px; font-weight:700; padding:0 24px;
            }
            QPushButton:hover { background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
                    stop:0 #2A94FF, stop:1 #6AD0FA); }
            QPushButton:disabled { background: rgba(255,255,255,0.1); color: rgba(255,255,255,0.3); }
        """

    # ---------- 行为 ----------
    def _start_download(self):
        url = self.update_info.get("download_url", "")
        if not url:
            self._set_status("❌ 下载地址无效，将打开 Release 页面。")
            QTimer.singleShot(800, self._open_release_page)
            return
        self.action_btn.setEnabled(False)
        self.action_btn.setText("下载中...")
        self.later_btn.setEnabled(False)
        self.progress.show()
        self.status.show()
        self._set_status("正在下载更新包...")

        self.downloader = UpdateDownloader(
            url, self.update_info.get("asset_name", "TidyUUUUp_Update.exe"), self)
        self.downloader.progress.connect(self._on_progress)
        self.downloader.download_finished.connect(self._on_finished)
        self.downloader.start()

    def _on_progress(self, pct):
        self.progress.setValue(pct)
        self._set_status(f"正在下载更新包...  {pct}%")

    def _on_finished(self, ok, result):
        if not ok:
            self.action_btn.setEnabled(True)
            self.action_btn.setText("重试下载")
            self.later_btn.setEnabled(True)
            self._set_status(f"❌ 下载失败：{result}")
            return
        self.progress.setValue(100)
        dest = result
        self._reveal_path(dest)
        self._finished = True
        self.action_btn.setEnabled(True)
        self.action_btn.clicked.disconnect()
        if dest.lower().endswith(".exe"):
            self._set_status(
                f"✅ 安装程序已下载到：{dest}\n"
                "点击“安装更新”即可更新应用；用户设置、桌面索引路径与小岛位置会保留。"
            )
            self.action_btn.setText("安装更新")
            self.action_btn.clicked.connect(lambda: self._launch_installer(dest))
            self.later_btn.setText("稍后安装")
        else:
            self._set_status(f"✅ 已下载到：{dest}\n请在下载目录手动安装；用户设置与桌面索引会保留。")
            self.action_btn.setText("打开 Release 页面")
            self.action_btn.clicked.connect(self._open_release_page)
            self.later_btn.setText("完成")
            self.later_btn.clicked.disconnect()
            self.later_btn.clicked.connect(self.accept)

    def _launch_installer(self, installer_path):
        try:
            if sys.platform.startswith("win"):
                os.startfile(installer_path)  # type: ignore[attr-defined]
            elif sys.platform == "darwin":
                subprocess.Popen(["open", installer_path])
            else:
                subprocess.Popen(["xdg-open", os.path.dirname(installer_path)])
            self.accept()
        except Exception as error:
            self._set_status(f"无法启动安装程序：{error}")

    def _set_status(self, text):
        self.status.setText(text)
        self.status.show()

    def _open_release_page(self):
        url = self.update_info.get("release_url") or self.update_info.get("download_url", "")
        if url:
            try:
                if sys.platform.startswith("win"):
                    os.startfile(url)  # type: ignore[attr-defined]
                elif sys.platform == "darwin":
                    subprocess.Popen(["open", url])
                else:
                    subprocess.Popen(["xdg-open", url])
            except Exception as e:
                self._set_status(f"无法打开页面：{e}")

    def _reveal_path(self, path):
        try:
            if sys.platform.startswith("win"):
                subprocess.Popen(["explorer", "/select,", os.path.basename(path)],
                                 cwd=os.path.dirname(path))
            elif sys.platform == "darwin":
                subprocess.Popen(["open", "-R", path])
            else:
                subprocess.Popen(["xdg-open", os.path.dirname(path)])
        except Exception:
            pass

    def paintEvent(self, event):
        # 透明背景下的圆角裁剪由 WA_TranslucentBackground + container 圆角处理
        super().paintEvent(event)

    def closeEvent(self, event):
        if self.downloader is not None and self.downloader.isRunning():
            try:
                self.downloader.quit()
                self.downloader.wait(2000)
            except Exception:
                pass
        super().closeEvent(event)

    def show_centered(self):
        screen = QApplication.primaryScreen().geometry()
        self.move(screen.center().x() - self.width() // 2,
                  screen.center().y() - self.height() // 2)
        self.show()
        self.raise_()
