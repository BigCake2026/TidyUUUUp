"""
TidyUUUUp - 更新对话框
显示新版本信息、下载进度、更新结果
"""

import sys
import os
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QProgressBar, QTextEdit, QWidget, QApplication
)
from PyQt5.QtGui import QPainter, QColor, QLinearGradient, QBrush

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.updater import UpdateDownloader, apply_update


class UpdateDialog(QDialog):
    """更新对话框"""

    def __init__(self, update_info, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(520, 480)

        self.update_info = update_info
        self.downloader = None
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # 主容器
        container = QWidget()
        container.setObjectName("container")
        container.setStyleSheet("""
            #container {
                background: rgba(30, 30, 50, 0.98);
                backdrop-filter: blur(40px);
                border: 1px solid rgba(255, 255, 255, 0.12);
                border-radius: 22px;
            }
        """)

        inner = QVBoxLayout(container)
        inner.setContentsMargins(28, 28, 28, 24)
        inner.setSpacing(16)

        # 标题
        title = QLabel("✨  发现新版本")
        title.setStyleSheet("color: white; font-size: 24px; font-weight: 700;")
        inner.addWidget(title)

        # 版本信息
        version_text = f"v {self.update_info.get('current_version', '')}  →  v <span style='color: #8b5cf6; font-weight: 700;'>{self.update_info.get('latest_version', '')}</span>"
        if self.update_info.get('publish_date'):
            version_text += f"  <span style='color: rgba(255,255,255,0.4); font-size: 12px;'>({self.update_info['publish_date']})</span>"
        version_label = QLabel(version_text)
        version_label.setTextFormat(Qt.RichText)
        version_label.setStyleSheet("color: rgba(255, 255, 255, 0.7); font-size: 14px;")
        inner.addWidget(version_label)

        # 文件大小
        if self.update_info.get('file_size'):
            size_label = QLabel(f"📦  大小: {self.update_info['file_size']}")
            size_label.setStyleSheet("color: rgba(255, 255, 255, 0.5); font-size: 13px;")
            inner.addWidget(size_label)

        # 更新日志
        changelog_title = QLabel("📝  更新内容")
        changelog_title.setStyleSheet("color: white; font-size: 15px; font-weight: 600; margin-top: 8px;")
        inner.addWidget(changelog_title)

        self.changelog = QTextEdit()
        self.changelog.setReadOnly(True)
        self.changelog.setPlainText(self.update_info.get('changelog', '暂无更新说明'))
        self.changelog.setFixedHeight(140)
        self.changelog.setStyleSheet("""
            QTextEdit {
                background: rgba(255, 255, 255, 0.05);
                color: rgba(255, 255, 255, 0.85);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 12px;
                padding: 12px 14px;
                font-size: 13px;
            }
        """)
        inner.addWidget(self.changelog)

        # 进度条（初始隐藏）
        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(8)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                background: rgba(255, 255, 255, 0.08);
                border: none;
                border-radius: 4px;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #8b5cf6, stop:1 #ec4899);
                border-radius: 4px;
            }
        """)
        self.progress_bar.hide()
        inner.addWidget(self.progress_bar)

        # 状态文本
        self.status_label = QLabel("")
        self.status_label.setStyleSheet("color: rgba(255, 255, 255, 0.5); font-size: 12px;")
        self.status_label.hide()
        inner.addWidget(self.status_label)

        inner.addStretch()

        # 按钮区域
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)

        self.skip_btn = QPushButton("跳过")
        self.skip_btn.setFixedHeight(42)
        self.skip_btn.setCursor(Qt.PointingHandCursor)
        self.skip_btn.setStyleSheet("""
            QPushButton {
                background: rgba(255, 255, 255, 0.08);
                color: rgba(255, 255, 255, 0.7);
                border: none;
                border-radius: 12px;
                font-size: 14px;
                font-weight: 600;
                padding: 0 24px;
            }
            QPushButton:hover {
                background: rgba(255, 255, 255, 0.15);
            }
        """)
        self.skip_btn.clicked.connect(self.reject)
        btn_layout.addWidget(self.skip_btn)

        self.update_btn = QPushButton("立即更新")
        self.update_btn.setFixedHeight(42)
        self.update_btn.setCursor(Qt.PointingHandCursor)
        self.update_btn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #8b5cf6, stop:1 #ec4899);
                color: white;
                border: none;
                border-radius: 12px;
                font-size: 14px;
                font-weight: 700;
                padding: 0 28px;
            }
            QPushButton:hover {
                opacity: 0.9;
            }
            QPushButton:disabled {
                background: rgba(255, 255, 255, 0.1);
                color: rgba(255, 255, 255, 0.3);
            }
        """)
        self.update_btn.clicked.connect(self._start_download)
        btn_layout.addWidget(self.update_btn)

        inner.addLayout(btn_layout)

        layout.addWidget(container)

    def _start_download(self):
        download_url = self.update_info.get('download_url', '')
        if not download_url:
            self.status_label.setText("❌ 下载地址无效")
            self.status_label.show()
            return

        self.update_btn.setEnabled(False)
        self.update_btn.setText("更新中...")
        self.skip_btn.setEnabled(False)
        self.progress_bar.show()
        self.status_label.show()
        self.status_label.setText("正在下载更新包...")

        self.downloader = UpdateDownloader(download_url)
        self.downloader.progress.connect(self._on_progress)
        self.downloader.download_finished.connect(self._on_download_finished)
        self.downloader.start()

    def _on_progress(self, percent):
        self.progress_bar.setValue(percent)
        self.status_label.setText(f"正在下载更新包...  {percent}%")

    def _on_download_finished(self, success, result):
        if not success:
            self.update_btn.setEnabled(True)
            self.update_btn.setText("重试")
            self.skip_btn.setEnabled(True)
            self.status_label.setText(f"❌ 下载失败: {result}")
            return

        self.status_label.setText("正在安装更新...")
        self.progress_bar.setValue(100)

        # 应用更新
        QTimer.singleShot(300, lambda: self._apply_update(result))

    def _apply_update(self, update_file):
        app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        success, message = apply_update(update_file, app_dir)

        if success:
            self.status_label.setText("✅ 更新完成！请重启软件")
            self.update_btn.setText("完成")
            self.update_btn.setEnabled(True)
            self.update_btn.clicked.disconnect()
            self.update_btn.clicked.connect(self.accept)
            self.skip_btn.hide()
        else:
            self.status_label.setText(f"❌ {message}")
            self.update_btn.setEnabled(True)
            self.update_btn.setText("重试")
            self.skip_btn.setEnabled(True)

    def show_at_center(self):
        screen = QApplication.primaryScreen().geometry()
        x = screen.center().x() - self.width() // 2
        y = screen.center().y() - self.height() // 2
        self.move(x, y)
        self.show()
