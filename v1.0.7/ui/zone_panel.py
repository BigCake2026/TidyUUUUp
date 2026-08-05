"""
智能分类文件夹面板 - Smart Zone Panel
在Dock栏上显示虚拟分类文件夹，点击快速查看对应分类的文件
"""
import os
from PyQt5.QtCore import (
    Qt, QPoint, QSize, QPropertyAnimation, QEasingCurve,
    pyqtSignal, QTimer
)
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QListWidget, QListWidgetItem, QScrollArea, QFrame, QFileDialog
)
from PyQt5.QtGui import (
    QPainter, QColor, QIcon, QPixmap, QFont, QCursor, QLinearGradient, QBrush
)

from core.smart_engine import SmartRuleEngine


class ZoneFolderButton(QPushButton):
    """智能分类文件夹按钮（Dock栏上的）"""

    zone_clicked = pyqtSignal(str)

    def __init__(self, zone_name, zone_config, parent=None):
        super().__init__(parent)
        self.zone_name = zone_name
        self.config = zone_config
        self.file_count = 0

        self.setFixedSize(58, 58)
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet("background: transparent; border: none;")
        self.setProperty("baseSize", QSize(58, 58))

        self.setToolTip(f"{zone_name} ({zone_config.get('description', '')})")

        self.clicked.connect(lambda: self.zone_clicked.emit(self.zone_name))

    def set_file_count(self, count):
        self.file_count = count
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect()
        color = QColor(self.config.get('color', '#4A7FFF'))

        # 文件夹主体
        folder_gradient = QLinearGradient(0, 0, 0, rect.height())
        folder_gradient.setColorAt(0, color.lighter(130))
        folder_gradient.setColorAt(1, color)

        painter.setBrush(QBrush(folder_gradient))
        painter.setPen(QPen(color.darker(130), 1))

        # 画文件夹形状
        # 底部主体
        body_rect = QRect(6, 14, rect.width() - 12, rect.height() - 18)
        painter.drawRoundedRect(body_rect, 6, 6)

        # 顶部标签
        tab_rect = QRect(6, 8, 20, 10)
        painter.setBrush(QBrush(color.lighter(120)))
        painter.drawRoundedRect(tab_rect, 3, 3)

        # 图标
        icon = self.config.get('icon', '📁')
        painter.setPen(QColor(255, 255, 255, 230))
        font = painter.font()
        font.setPointSize(12)
        painter.setFont(font)
        painter.drawText(body_rect, Qt.AlignCenter, icon)

        # 文件数量角标
        if self.file_count > 0:
            badge_text = str(self.file_count) if self.file_count < 100 else "99+"
            badge_w = 18 if len(badge_text) == 1 else 24
            badge_rect = QRect(rect.width() - badge_w - 2, 2, badge_w, 16)

            painter.setBrush(QColor(255, 80, 80, 240))
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(badge_rect, 8, 8)

            painter.setPen(QColor(255, 255, 255))
            font = painter.font()
            font.setPointSize(9)
            font.setBold(True)
            painter.setFont(font)
            painter.drawText(badge_rect, Qt.AlignCenter, badge_text)


class ZonePanel(QWidget):
    """智能分类面板 - 点击Dock上的文件夹后弹出"""

    open_folder = pyqtSignal(str)
    open_file = pyqtSignal(str)

    def __init__(self, smart_engine=None, file_index=None, parent=None):
        super().__init__(parent)
        self.engine = smart_engine or SmartRuleEngine()
        self.file_index = file_index
        self.current_zone = None

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Popup |
            Qt.NoDropShadowWindowHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedWidth(380)
        self.setMaximumHeight(480)

        self._setup_ui()

    def _setup_ui(self):
        # 背景容器
        container = QWidget(self)
        container.setStyleSheet("""
            QWidget {
                background: rgba(25, 25, 45, 0.95);
                backdrop-filter: blur(30px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 18px;
            }
        """)

        layout = QVBoxLayout(container)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        # 标题栏
        header = QHBoxLayout()
        self.icon_label = QLabel("📁")
        self.icon_label.setStyleSheet("font-size: 24px; background: transparent; border: none;")
        header.addWidget(self.icon_label)

        self.title_label = QLabel("智能分类")
        self.title_label.setStyleSheet("font-size: 18px; font-weight: 700; color: white; background: transparent; border: none;")
        header.addWidget(self.title_label)
        header.addStretch()

        self.count_label = QLabel("0 个文件")
        self.count_label.setStyleSheet("font-size: 12px; color: rgba(255,255,255,0.5); background: transparent; border: none;")
        header.addWidget(self.count_label)

        layout.addLayout(header)

        # 分隔线
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background: rgba(255,255,255,0.08); border: none; max-height: 1px;")
        layout.addWidget(line)

        # 文件列表
        self.file_list = QListWidget()
        self.file_list.setStyleSheet("""
            QListWidget {
                background: transparent;
                border: none;
                outline: none;
                color: white;
            }
            QListWidget::item {
                background: rgba(255,255,255,0.04);
                border-radius: 8px;
                padding: 6px 8px;
                margin: 2px 0;
            }
            QListWidget::item:hover {
                background: rgba(255,255,255,0.1);
            }
        """)
        self.file_list.itemDoubleClicked.connect(self._on_file_double_clicked)
        layout.addWidget(self.file_list, 1)

        # 底部操作
        footer = QHBoxLayout()
        open_folder_btn = QPushButton("📂  打开文件夹")
        open_folder_btn.setFixedHeight(36)
        open_folder_btn.setCursor(Qt.PointingHandCursor)
        open_folder_btn.setStyleSheet("""
            QPushButton {
                background: rgba(100, 150, 255, 0.25);
                border: 1px solid rgba(100, 150, 255, 0.4);
                border-radius: 8px;
                color: white;
                font-size: 13px;
                font-weight: 500;
            }
            QPushButton:hover {
                background: rgba(120, 170, 255, 0.4);
            }
        """)
        open_folder_btn.clicked.connect(self._on_open_folder)
        footer.addWidget(open_folder_btn)

        layout.addLayout(footer)

        # 调整容器大小
        container.setGeometry(0, 0, 380, 480)

    def show_zone(self, zone_name, pos):
        """显示某个分类的面板"""
        self.current_zone = zone_name

        zone_config = self.engine.get_all_zones().get(zone_name, {})
        color = zone_config.get('color', '#4A7FFF')
        icon = zone_config.get('icon', '📁')

        self.icon_label.setText(icon)
        self.title_label.setText(zone_name)

        # 加载文件列表
        self._load_files(zone_name)

        # 定位
        self.move(pos.x() - 380 // 2, pos.y() - 480 - 10)

        # 淡入动画
        self.show()

    def _load_files(self, zone_name):
        """加载某个分类下的文件（从桌面扫描，虚拟分类）"""
        self.file_list.clear()

        files = []

        # 优先从文件索引获取
        if self.file_index:
            all_files = self.file_index.index
            for filepath, info in all_files.items():
                zone, _ = self.engine.classify(filepath)
                if zone == zone_name:
                    files.append(info)
        else:
            # 直接从桌面扫描（虚拟分类模式）
            from core.desktop_watcher import DesktopWatcher
            watcher = DesktopWatcher(self.engine)
            desktop_path = watcher.desktop_path
            if os.path.exists(desktop_path):
                for filename in os.listdir(desktop_path):
                    filepath = os.path.join(desktop_path, filename)
                    if os.path.isfile(filepath) and not filename.startswith('.') and not filename.startswith('~$'):
                        zone, _ = self.engine.classify(filepath)
                        if zone == zone_name:
                            try:
                                stat = os.stat(filepath)
                                files.append({
                                    'name': filename,
                                    'path': filepath,
                                    'size': stat.st_size,
                                    'modified': stat.st_mtime,
                                })
                            except OSError:
                                pass

        # 按修改时间排序
        files.sort(key=lambda x: x.get('modified', 0), reverse=True)

        self.count_label.setText(f"{len(files)} 个文件")

        # 显示前30个
        for info in files[:30]:
            item = QListWidgetItem()
            item.setText(f"  {info.get('name', '未知')}")
            item.setData(Qt.UserRole, info.get('path', ''))
            self.file_list.addItem(item)

    def _on_file_double_clicked(self, item):
        filepath = item.data(Qt.UserRole)
        if filepath and os.path.exists(filepath):
            self.open_file.emit(filepath)
            # 打开文件
            try:
                if sys.platform == 'win32':
                    os.startfile(filepath)
            except Exception:
                pass

    def _on_open_folder(self):
        # 虚拟模式下打开桌面（文件都在桌面上）
        from core.desktop_watcher import DesktopWatcher
        watcher = DesktopWatcher(self.engine)
        open_path = watcher.desktop_path
        try:
            if sys.platform == 'win32':
                os.startfile(open_path)
        except Exception:
            pass

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), Qt.transparent)


import sys
