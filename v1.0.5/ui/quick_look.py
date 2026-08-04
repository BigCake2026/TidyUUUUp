"""
空格键秒级预览 - Quick Look 增强版
对标 macOS 的空格键预览，支持图片、文档、代码等快速预览
集成智能标签 + AI 分类置信度
"""
import os
import sys
from PyQt5.QtCore import (
    Qt, QPoint, QSize, QPropertyAnimation, QEasingCurve,
    pyqtSignal, QTimer
)
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QFrame, QGraphicsOpacityEffect, QScrollArea, QTextEdit
)
from PyQt5.QtGui import (
    QPainter, QColor, QIcon, QPixmap, QFont, QCursor,
    QLinearGradient, QBrush, QPen
)


IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.svg', '.ico', '.tiff'}
TEXT_EXTENSIONS = {'.txt', '.md', '.py', '.js', '.ts', '.java', '.cpp', '.c', '.h', '.go', '.rs',
                    '.html', '.css', '.vue', '.jsx', '.tsx', '.json', '.xml', '.yaml', '.yml',
                    '.csv', '.log', '.ini', '.cfg', '.conf', '.bat', '.sh', '.bash', '.zsh'}
CODE_EXTENSIONS = {'.py', '.js', '.ts', '.java', '.cpp', '.c', '.h', '.go', '.rs',
                   '.html', '.css', '.vue', '.jsx', '.tsx', '.json', '.xml', '.yaml', '.yml',
                   '.bat', '.sh', '.bash', '.zsh'}


class QuickLookPanel(QWidget):
    """快速预览面板 - 对标 macOS Quick Look"""

    closed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_file = None
        self.smart_engine = None

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Popup |
            Qt.NoDropShadowWindowHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(720, 560)

        self._setup_ui()
        self._setup_animation()

    def _setup_ui(self):
        # 背景容器
        container = QWidget(self)
        container.setStyleSheet("""
            QWidget {
                background: rgba(20, 20, 35, 0.95);
                backdrop-filter: blur(40px);
                border: 1px solid rgba(255, 255, 255, 0.12);
                border-radius: 20px;
            }
        """)

        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(14)

        # 顶部：标题栏
        header = QHBoxLayout()
        header.setSpacing(12)

        # 文件图标
        self.file_icon = QLabel()
        self.file_icon.setFixedSize(44, 44)
        self.file_icon.setAlignment(Qt.AlignCenter)
        self.file_icon.setStyleSheet("background: rgba(255,255,255,0.08); border-radius: 10px; font-size: 24px;")
        header.addWidget(self.file_icon)

        # 文件名和路径
        info_layout = QVBoxLayout()
        info_layout.setSpacing(2)

        self.filename_label = QLabel("未选择文件")
        self.filename_label.setStyleSheet("color: white; font-size: 15px; font-weight: 600; background: transparent;")
        self.filename_label.setWordWrap(True)
        info_layout.addWidget(self.filename_label)

        self.filepath_label = QLabel("")
        self.filepath_label.setStyleSheet("color: rgba(255,255,255,0.4); font-size: 11px; background: transparent;")
        self.filepath_label.setWordWrap(True)
        info_layout.addWidget(self.filepath_label)

        header.addLayout(info_layout, 1)

        # 关闭按钮
        close_btn = QPushButton("✕")
        close_btn.setFixedSize(32, 32)
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.setStyleSheet("""
            QPushButton {
                background: rgba(255,255,255,0.08);
                border: none;
                border-radius: 16px;
                color: rgba(255,255,255,0.7);
                font-size: 14px;
                font-weight: 600;
            }
            QPushButton:hover {
                background: rgba(255,100,100,0.3);
                color: white;
            }
        """)
        close_btn.clicked.connect(self.close)
        header.addWidget(close_btn)

        main_layout.addLayout(header)

        # 分隔线
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background: rgba(255,255,255,0.08); border: none; max-height: 1px;")
        main_layout.addWidget(line)

        # 内容区域
        self.content_stack = {}

        # 图片预览
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("background: rgba(0,0,0,0.3); border-radius: 12px;")
        self.image_label.setMinimumHeight(320)
        self.content_stack['image'] = self.image_label

        # 文本预览
        self.text_preview = QTextEdit()
        self.text_preview.setReadOnly(True)
        self.text_preview.setStyleSheet("""
            QTextEdit {
                background: rgba(0,0,0,0.3);
                border: none;
                border-radius: 12px;
                color: rgba(220,220,240,0.95);
                font-family: 'Consolas', 'Monaco', 'Cascadia Mono', monospace;
                font-size: 12px;
                padding: 16px;
            }
        """)
        self.text_preview.setMinimumHeight(320)
        self.content_stack['text'] = self.text_preview

        # 默认/不支持预览
        self.default_view = QWidget()
        default_layout = QVBoxLayout(self.default_view)
        default_layout.setContentsMargins(0, 0, 0, 0)

        default_icon = QLabel("📁")
        default_icon.setAlignment(Qt.AlignCenter)
        default_icon.setStyleSheet("font-size: 64px; background: transparent;")
        default_layout.addWidget(default_icon)

        default_text = QLabel("此文件类型暂不支持预览\n双击文件可使用默认程序打开")
        default_text.setAlignment(Qt.AlignCenter)
        default_text.setStyleSheet("color: rgba(255,255,255,0.5); font-size: 13px; background: transparent;")
        default_text.setWordWrap(True)
        default_layout.addWidget(default_text)

        default_layout.addStretch()
        self.default_view.setMinimumHeight(320)
        self.content_stack['default'] = self.default_view

        # 把所有视图添加到布局
        main_layout.addWidget(self.image_label)
        main_layout.addWidget(self.text_preview)
        main_layout.addWidget(self.default_view)

        # 底部：智能标签 + AI 分类置信度
        footer = QHBoxLayout()
        footer.setSpacing(10)

        # 智能标签区域
        self.tags_container = QHBoxLayout()
        self.tags_container.setSpacing(6)
        footer.addLayout(self.tags_container, 1)

        # AI 分类置信度
        self.confidence_label = QLabel("")
        self.confidence_label.setStyleSheet("""
            background: rgba(100, 150, 255, 0.15);
            border: 1px solid rgba(100, 150, 255, 0.3);
            border-radius: 8px;
            padding: 4px 12px;
            color: rgba(150, 180, 255, 0.95);
            font-size: 11px;
            font-weight: 500;
        """)
        footer.addWidget(self.confidence_label)

        main_layout.addLayout(footer)

        # 文件大小和修改时间
        meta_row = QHBoxLayout()
        self.size_label = QLabel("")
        self.size_label.setStyleSheet("color: rgba(255,255,255,0.35); font-size: 11px; background: transparent;")
        meta_row.addWidget(self.size_label)

        self.mtime_label = QLabel("")
        self.mtime_label.setStyleSheet("color: rgba(255,255,255,0.35); font-size: 11px; background: transparent;")
        meta_row.addWidget(self.mtime_label)

        meta_row.addStretch()

        # 提示
        tip_label = QLabel("按 空格键 或 ESC 关闭")
        tip_label.setStyleSheet("color: rgba(255,255,255,0.25); font-size: 11px; background: transparent;")
        meta_row.addWidget(tip_label)

        main_layout.addLayout(meta_row)

        container.setGeometry(0, 0, 720, 560)

    def _setup_animation(self):
        self._opacity_effect = QGraphicsOpacityEffect(self)
        self._opacity_effect.setOpacity(0.0)
        self.setGraphicsEffect(self._opacity_effect)

        self._fade_in = QPropertyAnimation(self._opacity_effect, b"opacity")
        self._fade_in.setDuration(180)
        self._fade_in.setStartValue(0.0)
        self._fade_in.setEndValue(1.0)
        self._fade_in.setEasingCurve(QEasingCurve.OutCubic)

        self._fade_out = QPropertyAnimation(self._opacity_effect, b"opacity")
        self._fade_out.setDuration(150)
        self._fade_out.setStartValue(1.0)
        self._fade_out.setEndValue(0.0)
        self._fade_out.setEasingCurve(QEasingCurve.InCubic)
        self._fade_out.finished.connect(self._on_fade_out_finished)

    def preview_file(self, filepath, smart_engine=None):
        """预览指定文件"""
        if not filepath or not os.path.exists(filepath):
            return

        self.current_file = filepath
        self.smart_engine = smart_engine

        filename = os.path.basename(filepath)
        ext = os.path.splitext(filename)[1].lower()

        # 更新标题
        self.filename_label.setText(filename)
        self.filepath_label.setText(filepath)

        # 更新文件图标
        self.file_icon.setText(self._get_file_icon(ext))

        # 更新元数据
        try:
            stat = os.stat(filepath)
            size = self._format_size(stat.st_size)
            from datetime import datetime
            mtime = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M')
            self.size_label.setText(f"📦 {size}")
            self.mtime_label.setText(f"🕐 {mtime}")
        except Exception:
            self.size_label.setText("")
            self.mtime_label.setText("")

        # 显示对应预览
        self._show_preview(filepath, ext)

        # 智能标签 + AI 置信度
        self._show_smart_tags(filepath)

    def _show_preview(self, filepath, ext):
        # 先隐藏所有
        self.image_label.hide()
        self.text_preview.hide()
        self.default_view.hide()

        # 图片预览
        if ext in IMAGE_EXTENSIONS:
            try:
                pixmap = QPixmap(filepath)
                if not pixmap.isNull():
                    scaled = pixmap.scaled(
                        680, 320,
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )
                    self.image_label.setPixmap(scaled)
                    self.image_label.show()
                    return
            except Exception:
                pass
            self.default_view.show()
            return

        # 文本/代码预览
        if ext in TEXT_EXTENSIONS:
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(8192)
                if len(content) >= 8192:
                    content += "\n\n... (文件过长，仅显示前 8KB)"
                self.text_preview.setPlainText(content)
                self.text_preview.show()
                return
            except Exception:
                pass
            self.default_view.show()
            return

        # 默认视图
        self.default_view.show()

    def _show_smart_tags(self, filepath):
        # 清空旧标签
        while self.tags_container.count():
            item = self.tags_container.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        if not self.smart_engine:
            self.confidence_label.setText("")
            return

        # AI 分类
        zone, confidence = self.smart_engine.classify(filepath)

        if zone:
            # 置信度
            conf_pct = int(confidence * 100)
            self.confidence_label.setText(f"🤖 AI 置信度 {conf_pct}%")

            # 分类标签
            tag = QLabel(f"🏷️ {zone}")
            tag.setStyleSheet("""
                background: rgba(100, 200, 100, 0.15);
                border: 1px solid rgba(100, 200, 100, 0.3);
                border-radius: 8px;
                padding: 4px 12px;
                color: rgba(150, 240, 150, 0.95);
                font-size: 11px;
                font-weight: 500;
            """)
            self.tags_container.addWidget(tag)

            # 文件类型标签
            filename = os.path.basename(filepath)
            ext = os.path.splitext(filename)[1].lower()
            if ext in CODE_EXTENSIONS:
                type_tag = QLabel("💻 代码文件")
            elif ext in IMAGE_EXTENSIONS:
                type_tag = QLabel("🖼️ 图片文件")
            elif ext == '.pdf':
                type_tag = QLabel("📄 PDF 文档")
            elif ext in {'.doc', '.docx'}:
                type_tag = QLabel("📝 Word 文档")
            elif ext in {'.xls', '.xlsx'}:
                type_tag = QLabel("📊 Excel 表格")
            elif ext in {'.ppt', '.pptx'}:
                type_tag = QLabel("📽️ PPT 演示")
            elif ext in {'.mp4', '.avi', '.mkv', '.mov'}:
                type_tag = QLabel("🎬 视频文件")
            elif ext in {'.mp3', '.wav', '.flac'}:
                type_tag = QLabel("🎵 音频文件")
            elif ext in {'.zip', '.rar', '.7z'}:
                type_tag = QLabel("📦 压缩包")
            else:
                type_tag = QLabel(f"📁 {ext.upper() if ext else '未知'}")

            type_tag.setStyleSheet("""
                background: rgba(255, 180, 100, 0.15);
                border: 1px solid rgba(255, 180, 100, 0.3);
                border-radius: 8px;
                padding: 4px 12px;
                color: rgba(255, 200, 120, 0.95);
                font-size: 11px;
                font-weight: 500;
            """)
            self.tags_container.addWidget(type_tag)
        else:
            self.confidence_label.setText("🤖 无法分类")

        self.tags_container.addStretch()

    def _get_file_icon(self, ext):
        if ext in IMAGE_EXTENSIONS:
            return "🖼️"
        elif ext in CODE_EXTENSIONS:
            return "💻"
        elif ext == '.pdf':
            return "📕"
        elif ext in {'.doc', '.docx'}:
            return "📘"
        elif ext in {'.xls', '.xlsx'}:
            return "📗"
        elif ext in {'.ppt', '.pptx'}:
            return "📙"
        elif ext in {'.mp4', '.avi', '.mkv', '.mov'}:
            return "🎬"
        elif ext in {'.mp3', '.wav', '.flac'}:
            return "🎵"
        elif ext in {'.zip', '.rar', '.7z'}:
            return "📦"
        elif ext in {'.exe', '.msi', '.apk'}:
            return "⚙️"
        elif ext == '.txt':
            return "📄"
        else:
            return "📁"

    def _format_size(self, size):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} PB"

    def show_panel(self, pos=None):
        """显示预览面板"""
        if pos:
            screen = QApplication.primaryScreen().geometry() if hasattr(QApplication, 'primaryScreen') else None
            x = pos.x() - self.width() // 2
            y = pos.y() - self.height() - 20
            if screen:
                x = max(screen.left() + 20, min(x, screen.right() - self.width() - 20))
                y = max(screen.top() + 20, min(y, screen.bottom() - self.height() - 20))
            self.move(x, y)

        self._opacity_effect.setOpacity(0.0)
        self.show()
        self._fade_in.start()

    def closeEvent(self, event):
        if self._opacity_effect.opacity() > 0.1:
            self._fade_out.start()
            event.ignore()
        else:
            self.closed.emit()
            event.accept()

    def _on_fade_out_finished(self):
        self.hide()
        self.closed.emit()

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Space, Qt.Key_Escape):
            self.close()
        else:
            super().keyPressEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), Qt.transparent)
