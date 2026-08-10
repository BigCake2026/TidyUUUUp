"""
智能分类区域面板 - Smart Zone Panel
极简 macOS Finder 侧边栏风格：横向列表项 + 白色 popover 目录树
"""
import os
import sys
import subprocess

from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QTimer, QRectF
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QFrame, QTreeWidget, QTreeWidgetItem,
    QGraphicsDropShadowEffect, QSizePolicy, QHeaderView, QApplication
)
from PyQt5.QtGui import QPainter, QColor, QFont, QFontMetrics

from core.smart_engine import SmartRuleEngine


# 极简风格：不使用 emoji 图标，不使用 per-zone 多色，统一中性灰阶


class DirectoryTreePopup(QWidget):
    """
    白色 popover 风格目录树弹出面板
    鼠标悬停在 ZoneFolderButton 上时显示该分类下的文件目录树
    """

    file_activated = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(None)  # 独立窗口，Popup 类型
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Popup |
            Qt.NoDropShadowWindowHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setFixedWidth(280)
        self.setMaximumHeight(400)

        self._auto_hide_timer = QTimer(self)
        self._auto_hide_timer.setSingleShot(True)
        self._auto_hide_timer.timeout.connect(self.hide)

        self._setup_ui()

    def _setup_ui(self):
        outer = QVBoxLayout(self)
        outer.setContentsMargins(6, 6, 6, 6)
        outer.setSpacing(0)

        # 白色卡片容器（带极轻阴影 + 圆角 + hairline 边框）
        self.container = QFrame()
        self.container.setObjectName("PopoverContainer")
        self.container.setStyleSheet("""
            QFrame#PopoverContainer {
                background: #FFFFFF;
                border: 1px solid rgba(0,0,0,0.08);
                border-radius: 10px;
            }
        """)
        shadow = QGraphicsDropShadowEffect(self.container)
        shadow.setBlurRadius(4)
        shadow.setColor(QColor(0, 0, 0, 26))   # ~10% alpha
        shadow.setOffset(0, 0)
        self.container.setGraphicsEffect(shadow)

        inner = QVBoxLayout(self.container)
        inner.setContentsMargins(0, 0, 0, 0)
        inner.setSpacing(0)

        # 标题栏：区域名称 + 右上角 × 关闭按钮
        title_bar = QHBoxLayout()
        title_bar.setContentsMargins(14, 10, 6, 8)
        title_bar.setSpacing(0)

        self.title_label = QLabel()
        self.title_label.setStyleSheet(
            "color: #1D1D1F; font-size: 13px; font-weight: 600;"
            " background: transparent; border: none;"
        )
        title_bar.addWidget(self.title_label)
        title_bar.addStretch()

        self.close_btn = QPushButton("×")
        self.close_btn.setFixedSize(22, 22)
        self.close_btn.setCursor(Qt.PointingHandCursor)
        self.close_btn.setStyleSheet("""
            QPushButton {
                color: #86868B;
                font-size: 14px;
                background: transparent;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover { background: rgba(0,0,0,0.06); }
        """)
        self.close_btn.clicked.connect(self.hide)
        title_bar.addWidget(self.close_btn)
        inner.addLayout(title_bar)

        # hairline 分隔线
        sep = QFrame()
        sep.setFixedHeight(1)
        sep.setStyleSheet("background: rgba(0,0,0,0.06); border: none;")
        inner.addWidget(sep)

        # 目录树：纯文字，双列（文件名 / 大小）
        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderHidden(True)
        self.tree.setRootIsDecorated(True)
        self.tree.setIndentation(16)
        self.tree.setStyleSheet("""
            QTreeWidget {
                background: #FFFFFF;
                border: none;
                outline: none;
                color: #1D1D1F;
                font-size: 12px;
            }
            QTreeWidget::item {
                padding: 5px 14px;
                border: none;
            }
            QTreeWidget::item:hover {
                background: rgba(0,0,0,0.04);
            }
            QTreeWidget::item:selected {
                background: rgba(0,0,0,0.07);
                color: #1D1D1F;
            }
            QTreeWidget::branch {
                background: transparent;
            }
            QScrollBar:vertical {
                background: transparent;
                width: 6px;
                margin: 4px 2px;
            }
            QScrollBar::handle:vertical {
                background: rgba(0,0,0,0.18);
                border-radius: 3px;
                min-height: 24px;
            }
            QScrollBar::handle:vertical:hover {
                background: rgba(0,0,0,0.30);
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: transparent;
            }
        """)
        header = self.tree.header()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tree.itemDoubleClicked.connect(self._on_item_activated)
        self.tree.itemClicked.connect(self._on_item_single_click)
        inner.addWidget(self.tree, 1)

        # 空状态
        self.empty_label = QLabel("暂无文件")
        self.empty_label.setAlignment(Qt.AlignCenter)
        self.empty_label.setStyleSheet(
            "color: #AEAEB2; font-size: 13px;"
            " background: transparent; border: none; padding: 28px;"
        )
        self.empty_label.hide()
        inner.addWidget(self.empty_label)

        outer.addWidget(self.container)

    def populate_from_files(self, files, zone_name, zone_icon, zone_color):
        """
        根据文件列表填充目录树
        files: list of {name, path, size, modified, category}
        zone_icon / zone_color 参数保留以兼容调用方，极简风格下不使用
        """
        self.tree.clear()
        self.title_label.setText(zone_name)

        # 按目录分组
        dir_groups = {}
        for info in files:
            path = info.get('path', '')
            dirname = os.path.dirname(path)
            dir_groups.setdefault(dirname, []).append(info)

        sorted_dirs = sorted(dir_groups.keys())
        has_files = len(files) > 0
        self.tree.setVisible(has_files)
        self.empty_label.setVisible(not has_files)

        if not has_files:
            self.setFixedHeight(150)
            return

        if len(sorted_dirs) <= 1:
            # 单目录：扁平文件列表
            for info in sorted(files, key=lambda x: x.get('modified', 0), reverse=True):
                self._add_file_item(None, info)
        else:
            # 多目录：分组显示
            for dir_path in sorted_dirs:
                dir_name = os.path.basename(dir_path) or dir_path
                dir_item = QTreeWidgetItem([dir_name, ""])
                dir_item.setData(0, Qt.UserRole, dir_path)
                dir_item.setData(0, Qt.UserRole + 1, 'folder')
                dfont = dir_item.font(0)
                dfont.setPixelSize(12)
                dfont.setBold(True)
                dir_item.setFont(0, dfont)
                dir_item.setForeground(0, QColor(29, 29, 31))
                self.tree.addTopLevelItem(dir_item)

                for info in sorted(dir_groups[dir_path],
                                   key=lambda x: x.get('modified', 0), reverse=True):
                    self._add_file_item(dir_item, info)
            # 自动展开前 3 个目录
            for i in range(min(3, self.tree.topLevelItemCount())):
                self.tree.topLevelItem(i).setExpanded(True)

        self.tree.resizeColumnToContents(1)

        # 估算高度
        def _count_visible(item):
            cnt = 1
            if item.isExpanded():
                for i in range(item.childCount()):
                    cnt += _count_visible(item.child(i))
            return cnt

        total_vis = 0
        for i in range(self.tree.topLevelItemCount()):
            total_vis += _count_visible(self.tree.topLevelItem(i))

        title_h = 40
        item_h = 26
        calc_h = title_h + min(total_vis, 12) * item_h + 8
        self.setFixedHeight(max(160, min(calc_h, 400)))

    def _add_file_item(self, parent, info):
        name = info.get('name', '未知')
        size = info.get('size', 0)
        if size < 1024:
            size_str = f"{size} B"
        elif size < 1024 * 1024:
            size_str = f"{size / 1024:.0f} KB"
        else:
            size_str = f"{size / (1024 * 1024):.1f} MB"

        item = QTreeWidgetItem([name, size_str])
        item.setTextAlignment(1, Qt.AlignRight | Qt.AlignVCenter)
        item.setData(0, Qt.UserRole, info.get('path', ''))
        item.setData(0, Qt.UserRole + 1, 'file')

        nfont = item.font(0)
        nfont.setPixelSize(12)
        nfont.setBold(False)
        item.setFont(0, nfont)

        sfont = item.font(1)
        sfont.setPixelSize(11)
        item.setFont(1, sfont)
        item.setForeground(1, QColor(0x86, 0x86, 0x8B))

        item.setToolTip(0, f"{name}\n大小: {size_str}\n路径: {info.get('path', '')}")
        if parent is None:
            self.tree.addTopLevelItem(item)
        else:
            parent.addChild(item)

    def _on_item_activated(self, item, column):
        kind = item.data(0, Qt.UserRole + 1)
        path = item.data(0, Qt.UserRole)
        if kind == 'file' and path:
            self.file_activated.emit(path)
            try:
                if sys.platform == 'win32':
                    os.startfile(path)
                elif sys.platform == 'darwin':
                    subprocess.Popen(['open', path])
                else:
                    subprocess.Popen(['xdg-open', path])
            except Exception:
                pass

    def _on_item_single_click(self, item, column):
        kind = item.data(0, Qt.UserRole + 1)
        if kind == 'folder':
            item.setExpanded(not item.isExpanded())

    def show_above(self, anchor_global, offset_x=0):
        """显示在锚点上方居中"""
        w = self.width()
        h = self.height()
        x = anchor_global.x() - w // 2 - offset_x
        y = anchor_global.y() - h - 12

        screen = QApplication.primaryScreen().availableGeometry()
        if x < screen.left() + 4:
            x = screen.left() + 4
        if x + w > screen.right() - 4:
            x = screen.right() - w - 4
        if y < screen.top() + 4:
            y = anchor_global.y() + 12

        self.move(x, y)
        self.show()
        self.raise_()
        self._auto_hide_timer.stop()

    def fade_out(self):
        """隐藏面板（极简风格：直接隐藏，不做动画）"""
        self.hide()

    def restart_auto_hide(self, delay_ms=300):
        """鼠标离开按钮后启动自动隐藏；若鼠标又进入面板则取消"""
        self._auto_hide_timer.stop()
        self._auto_hide_timer.start(delay_ms)

    def enterEvent(self, event):
        # 鼠标在面板内部，停止自动隐藏
        self._auto_hide_timer.stop()

    def leaveEvent(self, event):
        # 离开面板，快速收起
        self._auto_hide_timer.start(180)


class ZoneFolderButton(QPushButton):
    """
    极简 macOS Finder 侧边栏列表项
    - 横向列表项，宽度填满父容器，高度 32px
    - 左侧：区域名称（13px #1D1D1F）
    - 右侧：极小文件计数 badge（灰色背景，10px 字体）
    - hover / selected / pressed 使用极轻中性灰背景
    """

    zone_clicked = pyqtSignal(str)
    zone_hovered = pyqtSignal(object, QPoint)   # (self, anchor_global)
    zone_left = pyqtSignal()

    def __init__(self, zone_name, zone_config, parent=None):
        super().__init__(parent)
        self.zone_name = zone_name
        self.config = zone_config
        self.file_count = 0
        self._hovered = False
        self._pressed = False
        self._selected = False

        self.setFixedHeight(32)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setCursor(Qt.PointingHandCursor)
        self.setMouseTracking(True)
        self.setStyleSheet("background: transparent; border: none;")
        self.setToolTip(f"{zone_name} · {zone_config.get('description', '')}")

        self.clicked.connect(lambda: self.zone_clicked.emit(self.zone_name))

    def set_file_count(self, count):
        self.file_count = count
        self.update()

    def set_selected(self, selected):
        self._selected = selected
        self.update()

    def enterEvent(self, event):
        self._hovered = True
        self.update()
        center = self.mapToGlobal(QPoint(self.width() // 2, 0))
        self.zone_hovered.emit(self, center)

    def leaveEvent(self, event):
        self._hovered = False
        self.update()
        self.zone_left.emit()

    def mousePressEvent(self, event):
        self._pressed = True
        self.update()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self._pressed = False
        self.update()
        super().mouseReleaseEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)

        rect = QRectF(self.rect())

        # 状态背景（中性灰阶，无渐变 / 无蓝色描边）
        if self._pressed:
            bg = QColor(0, 0, 0, 26)      # rgba(0,0,0,0.10)
        elif self._selected:
            bg = QColor(0, 0, 0, 18)      # rgba(0,0,0,0.07)
        elif self._hovered:
            bg = QColor(0, 0, 0, 10)      # rgba(0,0,0,0.04)
        else:
            bg = QColor(0, 0, 0, 0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(bg)
        painter.drawRoundedRect(rect, 6, 6)

        # 右侧 badge 宽度（用于给文字留出空间）
        badge_w = 0
        badge_text = ""
        if self.file_count > 0:
            badge_text = str(self.file_count) if self.file_count < 100 else "99+"
            badge_font = QFont()
            badge_font.setPixelSize(10)
            bfm = QFontMetrics(badge_font)
            badge_w = bfm.horizontalAdvance(badge_text) + 12   # 6px padding each side

        # 左侧区域名称
        name_font = QFont()
        name_font.setPixelSize(13)
        painter.setFont(name_font)
        painter.setPen(QColor(0x1D, 0x1D, 0x1F))
        nfm = QFontMetrics(name_font)

        left_pad = 10.0
        right_reserve = badge_w + 10.0 if badge_w > 0 else 10.0
        text_max = rect.width() - left_pad - right_reserve
        if text_max < 0:
            text_max = 0
        elided = nfm.elidedText(self.zone_name, Qt.ElideRight, int(text_max))
        painter.drawText(
            QRectF(left_pad, 0, text_max, rect.height()),
            Qt.AlignLeft | Qt.AlignVCenter,
            elided
        )

        # 右侧文件计数 badge
        if badge_w > 0:
            badge_font = QFont()
            badge_font.setPixelSize(10)
            bfm = QFontMetrics(badge_font)
            bh = bfm.height() + 2     # 1px padding top/bottom
            bx = rect.width() - badge_w - 8.0
            by = (rect.height() - bh) / 2.0
            badge_rect = QRectF(bx, by, badge_w, bh)

            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(0, 0, 0, 20))   # rgba(0,0,0,0.08)
            painter.drawRoundedRect(badge_rect, 4, 4)

            painter.setPen(QColor(0x1D, 0x1D, 0x1F))
            painter.setFont(badge_font)
            painter.drawText(badge_rect, Qt.AlignCenter, badge_text)


class ZonePanel(QWidget):
    """
    智能分类区域面板 - 极简垂直列表容器
    顶部标题 + ZoneFolderButton 列表 + 底部"打开文件夹"文字按钮
    容器背景透明，不画背景
    """

    open_folder = pyqtSignal(str)
    open_file = pyqtSignal(str)

    def __init__(self, smart_engine=None, file_index=None, parent=None):
        super().__init__(parent)
        self.engine = smart_engine or SmartRuleEngine()
        self.file_index = file_index
        self.current_zone = None
        self._zone_buttons = []

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Popup |
            Qt.NoDropShadowWindowHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedWidth(240)
        self.setMaximumHeight(400)

        self._setup_ui()
        self._populate_zones()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(2)

        # 顶部标题
        self.title_label = QLabel("智能分类")
        self.title_label.setStyleSheet(
            "color: #86868B; font-size: 11px; font-weight: 600;"
            " background: transparent; border: none; padding: 4px 6px;"
        )
        layout.addWidget(self.title_label)

        # 可滚动列表容器
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QFrame.NoFrame)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setStyleSheet("""
            QScrollArea {
                background: transparent;
                border: none;
            }
            QScrollBar:vertical {
                background: transparent;
                width: 6px;
                margin: 4px 0;
            }
            QScrollBar::handle:vertical {
                background: rgba(0,0,0,0.18);
                border-radius: 3px;
                min-height: 24px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: transparent;
            }
        """)

        self.list_container = QWidget()
        self.list_container.setStyleSheet("background: transparent;")
        self.list_layout = QVBoxLayout(self.list_container)
        self.list_layout.setContentsMargins(0, 0, 0, 0)
        self.list_layout.setSpacing(2)
        self.list_layout.addStretch()

        self.scroll.setWidget(self.list_container)
        layout.addWidget(self.scroll, 1)

        # 底部"打开文件夹"文字按钮
        self.open_folder_btn = QPushButton("打开文件夹")
        self.open_folder_btn.setCursor(Qt.PointingHandCursor)
        self.open_folder_btn.setStyleSheet("""
            QPushButton {
                color: #1D1D1F;
                font-size: 13px;
                background: transparent;
                border: none;
                padding: 6px 8px;
                text-align: left;
            }
            QPushButton:hover {
                color: #0A84FF;
            }
        """)
        self.open_folder_btn.clicked.connect(self._on_open_folder)
        layout.addWidget(self.open_folder_btn)

    def _populate_zones(self):
        zones = self.engine.get_all_zones()
        for zone_name, zone_config in zones.items():
            self.add_zone(zone_name, zone_config)

    def add_zone(self, zone_name, zone_config):
        """添加一个区域列表项"""
        btn = ZoneFolderButton(zone_name, zone_config)
        btn.zone_clicked.connect(self._on_zone_clicked)
        # 在 stretch 之前插入，保持底部弹性空间
        self.list_layout.insertWidget(self.list_layout.count() - 1, btn)
        self._zone_buttons.append(btn)
        return btn

    def _on_zone_clicked(self, zone_name):
        self.current_zone = zone_name
        for b in self._zone_buttons:
            b.set_selected(b.zone_name == zone_name)

    def update_file_counts(self):
        """从 file_index 重新计算并刷新所有区域按钮的文件计数"""
        if not self.file_index:
            return

        counts = {b.zone_name: 0 for b in self._zone_buttons}
        try:
            with self.file_index._lock:
                filepaths = list(self.file_index.index.keys())
        except Exception:
            filepaths = list(self.file_index.index.keys())

        for filepath in filepaths:
            zone, _ = self.engine.classify(filepath)
            if zone in counts:
                counts[zone] += 1

        for b in self._zone_buttons:
            b.set_file_count(counts.get(b.zone_name, 0))

    def show_zone(self, zone_name, pos):
        """显示面板并高亮指定区域"""
        self.current_zone = zone_name

        # 若该区域尚未加入列表，则补充加入
        if not any(b.zone_name == zone_name for b in self._zone_buttons):
            zones = self.engine.get_all_zones()
            if zone_name in zones:
                self.add_zone(zone_name, zones[zone_name])

        for b in self._zone_buttons:
            b.set_selected(b.zone_name == zone_name)

        self.adjustSize()
        w = self.width()
        h = self.height()
        x = pos.x() - w // 2
        y = pos.y() - h - 10

        screen = QApplication.primaryScreen().availableGeometry()
        if x < screen.left() + 4:
            x = screen.left() + 4
        if x + w > screen.right() - 4:
            x = screen.right() - w - 4
        if y < screen.top() + 4:
            y = pos.y() + 12

        self.move(x, y)
        self.show()
        self.raise_()

    def populate_from_files(self, files, zone_name, zone_icon=None, zone_color=None):
        """
        兼容接口：将文件列表填充到内部目录树弹出面板
        本面板自身为区域列表，文件浏览由 DirectoryTreePopup 负责；
        此方法保留以兼容外部调用，内部委托给一个共享 DirectoryTreePopup。
        """
        if not hasattr(self, '_shared_tree_popup'):
            self._shared_tree_popup = DirectoryTreePopup(self)
        self._shared_tree_popup.populate_from_files(
            files, zone_name, zone_icon, zone_color
        )

    def _on_open_folder(self):
        # 虚拟模式下打开桌面（文件都位于桌面）
        from core.desktop_watcher import DesktopWatcher
        watcher = DesktopWatcher(self.engine)
        open_path = watcher.desktop_path
        self.open_folder.emit(open_path)
        try:
            if sys.platform == 'win32':
                os.startfile(open_path)
            elif sys.platform == 'darwin':
                subprocess.Popen(['open', open_path])
            else:
                subprocess.Popen(['xdg-open', open_path])
        except Exception:
            pass
