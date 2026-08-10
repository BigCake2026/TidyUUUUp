import os
import sys
import subprocess
import json
import hashlib
from datetime import datetime

from PyQt5.QtCore import (
    Qt, QPoint, QSize, QTimer, QPropertyAnimation, QEasingCurve,
    pyqtSignal, QRect, QRectF, QPointF
)
from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout,
    QApplication, QMenu, QAction, QSystemTrayIcon, QSizePolicy, QToolTip,
    QFileDialog, QMessageBox, QInputDialog, QLineEdit, QDialog
)
from PyQt5.QtGui import (
    QIcon, QPainter, QColor, QPixmap, QCursor, QFont, QBrush,
    QPainterPath, QLinearGradient, QRadialGradient, QPen, QPolygon
)
from .animations import BounceAnimation, DockMagnifyEffect
from .undo_panel import UndoButton


# ============================================================
#  Dock 常量 - macOS 风格紧凑型 Dock
# ============================================================
DOCK_BODY_HEIGHT = 44        # Dock 主体高度
DOCK_BOTTOM_GAP = 8          # 距屏幕底部间距
SHADOW_MARGIN = 4            # 阴影绘制边距
WIDGET_HEIGHT = DOCK_BODY_HEIGHT + SHADOW_MARGIN * 2  # 整个 widget 高度 = 52

BUTTON_WIDTH = 36            # 系统按钮宽度
BUTTON_HEIGHT = 32          # 系统按钮高度
BUTTON_RADIUS = 6            # 系统按钮圆角
LOGO_SIZE = 20               # Apple logo 尺寸
ITEM_SIZE = 32               # DockItem (固定应用) 尺寸

# 颜色常量
COLOR_BG = QColor(255, 255, 255, 184)         # rgba(255,255,255,0.72) ≈ 184
COLOR_BORDER = QColor(0, 0, 0, 13)            # rgba(0,0,0,0.05) ≈ 13
COLOR_SEPARATOR = QColor(0, 0, 0, 15)        # rgba(0,0,0,0.06) ≈ 15
COLOR_TEXT = QColor(29, 29, 31, 235)         # Apple near-black
COLOR_HOVER = QColor(0, 0, 0, 15)            # rgba(0,0,0,0.06) ≈ 15
COLOR_PRESSED = QColor(0, 0, 0, 26)          # rgba(0,0,0,0.10) ≈ 26


# ============================================================
#  DockItem - 固定应用项（仅显示首字母图标，无底部文字标签）
# ============================================================
class DockItem(QPushButton):
    """固定在 Dock 上的应用项。只显示首字母图标，无底部应用名标签。"""
    launched = pyqtSignal(str)

    def __init__(self, app_name, app_path, icon_path=None, parent=None):
        super().__init__(parent)
        self.app_name = app_name
        self.app_path = app_path
        self.setObjectName("DockItem")
        self.setFixedSize(ITEM_SIZE, ITEM_SIZE)
        self.setCursor(Qt.PointingHandCursor)
        self.setToolTip(app_name)

        # 设置图标
        if icon_path and os.path.exists(icon_path):
            self.setIcon(QIcon(icon_path))
        else:
            self._create_default_icon()
        self.setIconSize(QSize(ITEM_SIZE - 6, ITEM_SIZE - 6))

        self.clicked.connect(self._on_clicked)
        self._base_size = QSize(ITEM_SIZE, ITEM_SIZE)
        self.setProperty("baseSize", self._base_size)

        # 极简样式：透明底，hover 微灰
        self.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background: rgba(0, 0, 0, 0.06);
            }
            QPushButton:pressed {
                background: rgba(0, 0, 0, 0.10);
            }
        """)

    def _create_default_icon(self):
        """极简 Apple 风：纯色磨砂圆角方块 + 首字母（不显示底部应用名）"""
        size = ITEM_SIZE - 4
        pixmap = QPixmap(size, size)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHints(
            QPainter.Antialiasing | QPainter.SmoothPixmapTransform | QPainter.TextAntialiasing
        )

        tint_palette = [
            QColor("#0A84FF"), QColor("#FF375F"), QColor("#30D158"),
            QColor("#FF9F0A"), QColor("#BF5AF2"), QColor("#64D2FF"),
        ]
        idx = int(hashlib.md5(self.app_name.encode()).hexdigest(), 16) % len(tint_palette)
        base = tint_palette[idx]

        icon_rect = QRectF(1.0, 1.0, size - 2.0, size - 2.0)
        radius = 6.0

        # 1. 主体：白底 + 极淡 tint
        def mix(a, b, t):
            t = max(0.0, min(1.0, t))
            return QColor(
                int(a.red() + (b.red() - a.red()) * t),
                int(a.green() + (b.green() - a.green()) * t),
                int(a.blue() + (b.blue() - a.blue()) * t),
            )
        bg = QLinearGradient(0.0, icon_rect.top(), 0.0, icon_rect.bottom())
        bg.setColorAt(0.0, mix(QColor(255, 255, 255), base, 0.06))
        bg.setColorAt(1.0, mix(QColor(242, 244, 250), base, 0.22))
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(bg))
        painter.drawRoundedRect(icon_rect, radius, radius)

        # 2. 单层细描边
        painter.setPen(QPen(QColor(base.red(), base.green(), base.blue(), 40), 0.7))
        painter.setBrush(Qt.NoBrush)
        painter.drawRoundedRect(icon_rect, radius, radius)

        # 3. 首字母（深色，无底部标签）
        first_char = self.app_name[0].upper() if self.app_name else "?"
        f = QFont()
        f.setPointSizeF(12.0)
        f.setWeight(QFont.DemiBold)
        f.setStyleStrategy(QFont.PreferAntialias)
        painter.setFont(f)
        painter.setPen(QColor(base.red(), base.green(), base.blue(), 230))
        painter.drawText(icon_rect, Qt.AlignCenter, first_char)

        painter.end()
        self.setIcon(QIcon(pixmap))

    def _on_clicked(self):
        # 轻微的弹性点击反馈（很克制）
        self._bounce_click()
        QTimer.singleShot(120, lambda: self.launched.emit(self.app_path))

    def _bounce_click(self):
        """克制的 Q 弹点击 - 仅 2px 缩放"""
        if hasattr(self, '_click_anim') and self._click_anim is not None:
            self._click_anim.stop()

        original_geo = self.geometry()
        expand = 2

        anim1 = QPropertyAnimation(self, b"geometry")
        anim1.setDuration(60)
        anim1.setStartValue(original_geo)
        anim1.setEndValue(original_geo.adjusted(-expand, -expand, expand, expand))
        anim1.setEasingCurve(QEasingCurve.OutQuad)

        anim2 = QPropertyAnimation(self, b"geometry")
        anim2.setDuration(220)
        anim2.setStartValue(original_geo.adjusted(-expand, -expand, expand, expand))
        anim2.setEndValue(original_geo)
        curve = QEasingCurve(QEasingCurve.OutCubic)
        anim2.setEasingCurve(curve)

        from PyQt5.QtCore import QSequentialAnimationGroup
        group = QSequentialAnimationGroup(self)
        group.addAnimation(anim1)
        group.addAnimation(anim2)
        self._click_anim = group
        group.start()

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self._show_context_menu(event.globalPos())
        else:
            super().mousePressEvent(event)

    def _apply_menu_style(self, menu):
        """统一菜单样式（无 emoji）"""
        menu.setStyleSheet("""
            QMenu {
                background: rgba(250, 251, 252, 0.96);
                border: 1px solid rgba(0, 0, 0, 0.08);
                border-radius: 8px;
                padding: 4px;
                color: #1D1D1F;
            }
            QMenu::item {
                padding: 6px 14px;
                border-radius: 4px;
                font-size: 12px;
            }
            QMenu::item:hover {
                background: rgba(0, 0, 0, 0.06);
                color: #1D1D1F;
            }
            QMenu::item:disabled {
                color: rgba(0, 0, 0, 0.35);
            }
            QMenu::separator {
                height: 1px;
                background: rgba(0, 0, 0, 0.06);
                margin: 4px 8px;
            }
        """)

    def _show_context_menu(self, pos):
        menu = QMenu(self)
        self._apply_menu_style(menu)

        open_action = QAction("打开", self)
        open_action.triggered.connect(lambda: self.launched.emit(self.app_path))
        menu.addAction(open_action)

        menu.addSeparator()

        remove_action = QAction("从 Dock 移除", self)
        remove_action.triggered.connect(lambda: self._remove_from_dock())
        menu.addAction(remove_action)

        menu.exec_(pos)

    def _remove_from_dock(self):
        dock = self.window()
        if hasattr(dock, 'remove_dock_item'):
            dock.remove_dock_item(self)


# ============================================================
#  CompactUndoButton - 紧凑版撤销按钮（适配 44px Dock）
# ============================================================
class CompactUndoButton(UndoButton):
    """适配紧凑型 Dock 的撤销按钮 - 重写 paintEvent 使用更小的图标"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(ITEM_SIZE, ITEM_SIZE)
        self.setStyleSheet("background: transparent; border: none;")
        self.setProperty("baseSize", QSize(ITEM_SIZE, ITEM_SIZE))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect()

        # 极简的橙色 tint 背景
        gradient = QLinearGradient(0, 0, 0, rect.height())
        gradient.setColorAt(0, QColor(255, 204, 0, 22))
        gradient.setColorAt(1, QColor(255, 159, 10, 36))

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(gradient))
        body = QRectF(3.0, 3.0, rect.width() - 6.0, rect.height() - 6.0)
        painter.drawRoundedRect(body, 6.0, 6.0)

        painter.setPen(QPen(QColor(255, 159, 10, 45), 0.6))
        painter.setBrush(Qt.NoBrush)
        painter.drawRoundedRect(body, 6.0, 6.0)

        # 撤销箭头图标（更小）
        painter.setPen(QColor(255, 149, 0, 230))
        font = painter.font()
        font.setPointSize(13)
        painter.setFont(font)
        painter.drawText(rect, Qt.AlignCenter, "↩")

        # 红点提示（更小）
        if self.has_undo:
            dot_rect = QRectF(rect.width() - 11.0, 2.0, 9.0, 9.0)
            painter.setBrush(QColor(255, 59, 48, 235))
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(dot_rect)

            if self.record_count > 1:
                badge_text = str(self.record_count) if self.record_count < 10 else "9+"
                painter.setPen(QColor(255, 255, 255))
                font = painter.font()
                font.setPointSize(6)
                font.setBold(True)
                painter.setFont(font)
                painter.drawText(dot_rect, Qt.AlignCenter, badge_text)


# ============================================================
#  DockBar - macOS 风格底部 Dock 栏
# ============================================================
class DockBar(QWidget):
    # ===== 既有信号（保持 main.py 兼容）=====
    search_triggered = pyqtSignal()
    files_triggered = pyqtSignal()
    organizer_triggered = pyqtSignal()
    settings_triggered = pyqtSignal()
    undo_triggered = pyqtSignal()
    categories_triggered = pyqtSignal()

    # ===== 新增信号（按规格要求）=====
    show_main_window = pyqtSignal()
    show_organize_dialog = pyqtSignal()
    toggle_main_window = pyqtSignal()

    def __init__(self, screen_geometry=None):
        super().__init__()
        self.setObjectName("DockBar")
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)

        if screen_geometry:
            self._screen_geo = screen_geometry
        else:
            self._screen_geo = QApplication.primaryScreen().geometry()

        # 固定应用数据
        self.pinned_apps = []           # 数据列表 (dict: name/path/icon)
        self._pinned_items = []          # DockItem widget 列表（按规格要求保留）
        self._pinned_config_path = os.path.join(
            os.path.expanduser('~'), '.nexus_dock', 'pinned_apps.json'
        )

        self._setup_ui()
        self._setup_position()
        self._setup_magnify_effect()

        self._is_hidden = False
        self._auto_hide_timer = QTimer(self)
        self._auto_hide_timer.setSingleShot(True)
        self._auto_hide_timer.timeout.connect(self._auto_hide)

        # 拖动状态
        self._dragging = False
        self._drag_offset = QPoint()

        self.setMouseTracking(True)

        # 加载固定的应用
        QTimer.singleShot(100, self._load_pinned_apps)

    # ============ UI 搭建 ============

    def _setup_ui(self):
        layout = QHBoxLayout(self)
        # 4px 边距留给阴影绘制；内容居中
        layout.setContentsMargins(SHADOW_MARGIN, SHADOW_MARGIN, SHADOW_MARGIN, SHADOW_MARGIN)
        layout.setSpacing(4)

        self._separators = []

        # 1. Apple logo 启动按钮 (20x20)
        self.start_btn = self._create_start_button()
        layout.addWidget(self.start_btn)

        # 分隔线 1
        sep1 = self._create_separator()
        self._separators.append(sep1)
        layout.addWidget(sep1)

        # 系统功能按钮（纯文字，无 emoji）
        self.search_btn = self._create_system_button("搜索", "搜索文件")
        self.search_btn.clicked.connect(self.search_triggered.emit)
        layout.addWidget(self.search_btn)

        self.files_btn = self._create_system_button("文件", "文件资源管理器")
        self.files_btn.clicked.connect(self.files_triggered.emit)
        layout.addWidget(self.files_btn)

        self.organizer_btn = self._create_system_button("整理", "智能整理")
        self.organizer_btn.clicked.connect(self.organizer_triggered.emit)
        layout.addWidget(self.organizer_btn)

        self.categories_btn = self._create_system_button("分类", "分类区域")
        self.categories_btn.clicked.connect(self.categories_triggered.emit)
        layout.addWidget(self.categories_btn)

        # 分隔线 2
        sep2 = self._create_separator()
        self._separators.append(sep2)
        layout.addWidget(sep2)

        # 固定应用区域
        self.apps_layout = QHBoxLayout()
        self.apps_layout.setSpacing(4)
        layout.addLayout(self.apps_layout)

        # 分隔线 3
        sep3 = self._create_separator()
        self._separators.append(sep3)
        layout.addWidget(sep3)

        # 添加固定应用按钮
        self.add_pin_btn = self._create_system_button("添加", "添加常用应用")
        self.add_pin_btn.clicked.connect(self._on_add_pinned_app)
        layout.addWidget(self.add_pin_btn)

        # 撤销按钮（紧凑版）
        self.undo_btn = CompactUndoButton()
        self.undo_btn.undo_clicked.connect(self.undo_triggered.emit)
        layout.addWidget(self.undo_btn)

        # 设置按钮
        self.settings_btn = self._create_system_button("设置", "设置")
        self.settings_btn.clicked.connect(self.settings_triggered.emit)
        layout.addWidget(self.settings_btn)

    def _create_separator(self):
        """1px 极淡竖线（实际线由 paintEvent 绘制，此处只是占位）"""
        sep = QWidget()
        sep.setFixedWidth(1)
        sep.setStyleSheet("background: transparent;")
        return sep

    def _create_system_button(self, label_text, tooltip):
        """macOS 风文字按钮：透明底，hover 微灰，pressed 稍深"""
        btn = QPushButton(label_text)
        btn.setObjectName("DockSystemButton")
        btn.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setToolTip(tooltip)
        btn.setProperty("baseSize", QSize(BUTTON_WIDTH, BUTTON_HEIGHT))
        btn.setStyleSheet(f"""
            QPushButton {{
                background: transparent;
                border: none;
                border-radius: {BUTTON_RADIUS}px;
                color: #1D1D1F;
                font-size: 11px;
                font-weight: 500;
                padding: 0;
            }}
            QPushButton:hover {{
                background: rgba(0, 0, 0, 0.06);
            }}
            QPushButton:pressed {{
                background: rgba(0, 0, 0, 0.10);
            }}
        """)
        return btn

    def _create_start_button(self):
        """极简 Apple logo 启动按钮 (20x20)"""
        btn = QPushButton()
        btn.setObjectName("StartButton")
        btn.setFixedSize(LOGO_SIZE, LOGO_SIZE)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setToolTip("打开开始菜单")
        btn.setProperty("baseSize", QSize(LOGO_SIZE, LOGO_SIZE))

        pixmap = self._create_apple_logo_pixmap(LOGO_SIZE)
        btn.setIcon(QIcon(pixmap))
        btn.setIconSize(QSize(LOGO_SIZE, LOGO_SIZE))
        btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background: rgba(0, 0, 0, 0.06);
            }
            QPushButton:pressed {
                background: rgba(0, 0, 0, 0.10);
            }
        """)
        btn.clicked.connect(self._toggle_windows_start)
        return btn

    def _create_apple_logo_pixmap(self, size=20):
        """用 QPainter 画一个简单的 Apple 剪影"""
        # 用 2x 尺寸渲染再缩小，让小图标更清晰
        render_size = size * 2
        pixmap = QPixmap(render_size, render_size)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        # 在 20x20 坐标空间内绘制，再缩放
        scale = render_size / 20.0
        painter.scale(scale, scale)

        apple_color = QColor(29, 29, 31, 235)

        # Apple 主体路径（手调贝塞尔曲线近似）
        path = QPainterPath()
        path.moveTo(10.0, 5.5)
        # 右侧曲线下绕
        path.cubicTo(11.6, 3.6, 14.0, 4.0, 15.0, 6.0)
        path.cubicTo(16.4, 8.0, 16.4, 11.5, 15.4, 14.0)
        path.cubicTo(14.4, 16.0, 13.0, 17.4, 11.5, 17.4)
        path.cubicTo(10.7, 17.4, 10.3, 16.9, 9.5, 16.9)
        path.cubicTo(8.7, 16.9, 8.3, 17.4, 7.5, 17.4)
        path.cubicTo(6.0, 17.4, 4.6, 16.0, 3.6, 14.0)
        path.cubicTo(2.6, 11.5, 2.6, 8.0, 4.0, 6.0)
        path.cubicTo(5.0, 4.0, 7.4, 3.6, 9.0, 5.5)
        path.closeSubpath()

        # 右侧咬一口
        bite = QPainterPath()
        bite.addEllipse(QPointF(15.0, 10.5), 1.8, 2.2)
        path = path.subtracted(bite)

        painter.setPen(Qt.NoPen)
        painter.setBrush(apple_color)
        painter.drawPath(path)

        # 叶子
        leaf = QPainterPath()
        leaf.moveTo(10.0, 5.0)
        leaf.cubicTo(10.3, 3.0, 11.8, 2.2, 13.5, 2.5)
        leaf.cubicTo(13.2, 4.0, 11.8, 5.2, 10.0, 5.0)
        leaf.closeSubpath()
        painter.setBrush(apple_color)
        painter.drawPath(leaf)

        painter.end()

        # 缩小到目标尺寸
        return pixmap.scaled(
            size, size,
            Qt.KeepAspectRatio, Qt.SmoothTransformation
        )

    # ============ Start 菜单 ============

    def _toggle_windows_start(self):
        # 直接调用系统原生开始菜单
        try:
            if sys.platform == 'win32':
                import ctypes
                from ctypes import wintypes

                KEYEVENTF_KEYUP = 0x0002
                VK_LWIN = 0x5B

                user32 = ctypes.windll.user32
                user32.keybd_event(VK_LWIN, 0, 0, 0)
                user32.keybd_event(VK_LWIN, 0, KEYEVENTF_KEYUP, 0)
            elif sys.platform == 'darwin':
                subprocess.Popen([
                    'osascript', '-e',
                    'tell application "System Events" to keystroke space using command down'
                ])
            else:
                self._show_start_menu()
        except Exception as e:
            print(f"打开开始菜单失败: {e}")
            self._show_start_menu()

    def _show_start_menu(self):
        menu = QMenu(self)
        self._apply_menu_style(menu)
        menu.setMinimumWidth(220)

        # 常用程序（菜单项无 emoji）
        explorer_action = QAction("文件资源管理器", self)
        explorer_action.triggered.connect(lambda: self._run_system_cmd("explorer"))
        menu.addAction(explorer_action)

        settings_action = QAction("设置", self)
        settings_action.triggered.connect(lambda: self._run_system_cmd("ms-settings:"))
        menu.addAction(settings_action)

        cmd_action = QAction("命令提示符", self)
        cmd_action.triggered.connect(lambda: self._run_system_cmd("cmd"))
        menu.addAction(cmd_action)

        taskmgr_action = QAction("任务管理器", self)
        taskmgr_action.triggered.connect(lambda: self._run_system_cmd("taskmgr"))
        menu.addAction(taskmgr_action)

        menu.addSeparator()

        run_action = QAction("运行 (Win+R)", self)
        run_action.triggered.connect(
            lambda: self._run_system_cmd("shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}")
        )
        menu.addAction(run_action)

        menu.addSeparator()

        # 电源操作
        shutdown_action = QAction("关机", self)
        shutdown_action.triggered.connect(lambda: self._run_system_cmd("shutdown /s /t 0"))
        menu.addAction(shutdown_action)

        restart_action = QAction("重启", self)
        restart_action.triggered.connect(lambda: self._run_system_cmd("shutdown /r /t 0"))
        menu.addAction(restart_action)

        sleep_action = QAction("睡眠", self)
        sleep_action.triggered.connect(
            lambda: self._run_system_cmd("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        )
        menu.addAction(sleep_action)

        menu.exec_(self.start_btn.mapToGlobal(QPoint(0, -menu.sizeHint().height())))

    def _apply_menu_style(self, menu):
        """统一菜单样式（无 emoji）"""
        menu.setStyleSheet("""
            QMenu {
                background: rgba(250, 251, 252, 0.96);
                border: 1px solid rgba(0, 0, 0, 0.08);
                border-radius: 8px;
                padding: 4px;
                color: #1D1D1F;
            }
            QMenu::item {
                padding: 6px 16px;
                border-radius: 4px;
                font-size: 12px;
            }
            QMenu::item:hover {
                background: rgba(0, 0, 0, 0.06);
                color: #1D1D1F;
            }
            QMenu::item:disabled {
                color: rgba(0, 0, 0, 0.35);
            }
            QMenu::separator {
                height: 1px;
                background: rgba(0, 0, 0, 0.06);
                margin: 4px 8px;
            }
        """)

    def _run_system_cmd(self, cmd):
        try:
            if sys.platform == 'win32':
                os.system(f'start "" "{cmd}"' if ':' in cmd else f'start "" {cmd}')
            elif sys.platform == 'darwin':
                subprocess.Popen(['open', '-a', cmd] if not cmd.startswith('/') else [cmd])
            else:
                subprocess.Popen(cmd if isinstance(cmd, list) else cmd.split(), shell=True)
        except Exception as e:
            print(f"运行命令失败: {e}")

    # ============ 定位 ============

    def _setup_position(self):
        """横向居中在屏幕底部，留 8px 间距"""
        # 让 layout 算出内容自然宽度
        self.adjustSize()
        dock_width = self.sizeHint().width()

        # 内容太少时给一个最小宽度；太多时限制最大宽度
        min_width = 360
        max_width = int(self._screen_geo.width() * 0.8)
        if dock_width < min_width:
            dock_width = min_width
        if dock_width > max_width:
            dock_width = max_width

        dock_height = WIDGET_HEIGHT  # 52 = 44 body + 4*2 shadow margin

        x = (self._screen_geo.width() - dock_width) // 2
        # 让 body 底部距屏幕底部 8px
        # body_bottom = widget_top + SHADOW_MARGIN + DOCK_BODY_HEIGHT
        # => widget_top = body_bottom - SHADOW_MARGIN - DOCK_BODY_HEIGHT
        # => widget_top = screen.bottom() - 8 - 4 - 44 = screen.bottom() - 56
        y = self._screen_geo.bottom() - DOCK_BOTTOM_GAP - SHADOW_MARGIN - DOCK_BODY_HEIGHT

        self.setGeometry(x, y, dock_width, dock_height)

    # ============ 放大效果 ============

    def _setup_magnify_effect(self):
        self._all_items = []
        # 非常克制：1.05x 而非 1.3x；半径也缩小
        self._magnify = DockMagnifyEffect(self, self._all_items, magnify_scale=1.05, radius=60)
        QTimer.singleShot(100, self._register_system_buttons)

    def _register_system_buttons(self):
        for btn in [
            self.start_btn, self.search_btn, self.files_btn,
            self.organizer_btn, self.categories_btn,
            self.add_pin_btn, self.undo_btn, self.settings_btn
        ]:
            if btn not in self._all_items:
                self._all_items.append(btn)
        self._magnify.items = self._all_items

    def add_app(self, app_name, app_path, icon_path=None):
        item = DockItem(app_name, app_path, icon_path, self)
        item.launched.connect(self._launch_app)
        self.apps_layout.addWidget(item)
        self._all_items.append(item)
        self._magnify.items = self._all_items
        return item

    def remove_dock_item(self, item):
        if item in self._all_items:
            self._all_items.remove(item)
            self._magnify.items = self._all_items
        if item in self._pinned_items:
            self._pinned_items.remove(item)
        item.setParent(None)
        item.deleteLater()

    # ============ 固定常用应用 ============

    def _load_pinned_apps(self):
        """加载固定的应用列表"""
        try:
            os.makedirs(os.path.dirname(self._pinned_config_path), exist_ok=True)
            if os.path.exists(self._pinned_config_path):
                with open(self._pinned_config_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.pinned_apps = data.get('apps', [])
                    for app in self.pinned_apps:
                        self._add_pinned_item(
                            app.get('name', ''),
                            app.get('path', ''),
                            app.get('icon', None)
                        )
        except Exception as e:
            print(f"加载固定应用失败: {e}")

    def _save_pinned_apps(self):
        """保存固定的应用列表"""
        try:
            os.makedirs(os.path.dirname(self._pinned_config_path), exist_ok=True)
            with open(self._pinned_config_path, 'w', encoding='utf-8') as f:
                json.dump({'apps': self.pinned_apps}, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存固定应用失败: {e}")

    def _on_add_pinned_app(self):
        """点击添加固定应用按钮（菜单项无 emoji）"""
        menu = QMenu(self)
        self._apply_menu_style(menu)

        action_browse = QAction("浏览程序...", self)
        action_browse.triggered.connect(self._browse_and_pin_app)
        menu.addAction(action_browse)

        action_shortcut = QAction("添加快捷方式...", self)
        action_shortcut.triggered.connect(self._add_shortcut_dialog)
        menu.addAction(action_shortcut)

        menu.addSeparator()

        # 推荐的常用软件
        common_apps = self._detect_common_apps()
        if common_apps:
            for app_name, app_path in common_apps[:6]:
                action = QAction(app_name, self)
                action.triggered.connect(
                    lambda checked, n=app_name, p=app_path: self._pin_app(n, p)
                )
                menu.addAction(action)

        global_pos = self.add_pin_btn.mapToGlobal(QPoint(0, -10))
        menu.exec_(global_pos)

    def _detect_common_apps(self):
        """检测系统中常用的软件"""
        apps = []
        candidates = [
            ("Chrome", r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
            ("Chrome", r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
            ("Edge", r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
            ("VS Code", r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe"),
            ("微信", r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe"),
            ("QQ", r"C:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe"),
            ("钉钉", r"C:\Program Files (x86)\DingDing\main\current\DingTalk.exe"),
            ("飞书", r"C:\Users\%USERNAME%\AppData\Local\Feishu\Feishu.exe"),
            ("WPS", r"C:\Program Files\Kingsoft\WPS Office\11.1.0.15120\office6\wps.exe"),
            ("Office", r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"),
            ("记事本", "notepad.exe"),
            ("计算器", "calc.exe"),
            ("画图", "mspaint.exe"),
        ]

        for name, path in candidates:
            expanded = os.path.expandvars(path)
            if os.path.exists(expanded) or os.path.sep not in path:
                already_pinned = any(a.get('path') == expanded for a in self.pinned_apps)
                if not already_pinned:
                    apps.append((name, expanded))
        return apps

    def _browse_and_pin_app(self):
        """浏览并添加程序"""
        file_filter = "程序 (*.exe *.lnk);;所有文件 (*.*)"
        filepath, _ = QFileDialog.getOpenFileName(
            self, "选择要固定的程序或快捷方式", "", file_filter
        )
        if filepath:
            name = os.path.splitext(os.path.basename(filepath))[0]
            if filepath.lower().endswith('.lnk'):
                name = os.path.splitext(os.path.basename(filepath))[0]
            self._pin_app(name, filepath)

    def _add_shortcut_dialog(self):
        """通过对话框添加快捷方式"""
        dialog = QDialog(self)
        dialog.setWindowTitle("添加快捷方式")
        dialog.setFixedSize(400, 200)
        dialog.setStyleSheet("background: rgba(250, 251, 252, 0.98); color: #1D1D1F;")

        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        name_label = QLabel("名称:")
        name_label.setStyleSheet("font-size: 13px; color: #1D1D1F;")
        layout.addWidget(name_label)

        name_edit = QLineEdit()
        name_edit.setPlaceholderText("例如：我的常用工具")
        name_edit.setStyleSheet("""
            QLineEdit {
                background: rgba(255, 255, 255, 0.95);
                border: 1px solid rgba(0, 0, 0, 0.10);
                border-radius: 6px;
                padding: 8px 12px;
                color: #1D1D1F;
                font-size: 13px;
            }
            QLineEdit:focus {
                border: 1px solid rgba(10, 132, 255, 0.50);
                background: rgba(255, 255, 255, 1.0);
            }
        """)
        layout.addWidget(name_edit)

        path_label = QLabel("路径:")
        path_label.setStyleSheet("font-size: 13px; color: #1D1D1F;")
        layout.addWidget(path_label)

        path_layout = QHBoxLayout()
        path_edit = QLineEdit()
        path_edit.setPlaceholderText("例如：C:\\Program Files\\...\\app.exe")
        path_edit.setStyleSheet("""
            QLineEdit {
                background: rgba(255, 255, 255, 0.95);
                border: 1px solid rgba(0, 0, 0, 0.10);
                border-radius: 6px;
                padding: 8px 12px;
                color: #1D1D1F;
                font-size: 13px;
            }
            QLineEdit:focus {
                border: 1px solid rgba(10, 132, 255, 0.50);
                background: rgba(255, 255, 255, 1.0);
            }
        """)
        path_layout.addWidget(path_edit, 1)

        browse_btn = QPushButton("浏览")
        browse_btn.setFixedSize(60, 32)
        browse_btn.setCursor(Qt.PointingHandCursor)
        browse_btn.setStyleSheet("""
            QPushButton {
                background: rgba(250, 251, 252, 0.80);
                border: 1px solid rgba(0, 0, 0, 0.10);
                border-radius: 6px;
                color: #1D1D1F;
                font-size: 12px;
            }
            QPushButton:hover {
                background: rgba(255, 255, 255, 0.95);
                border: 1px solid rgba(0, 0, 0, 0.16);
            }
        """)
        browse_btn.clicked.connect(lambda: self._browse_for_path(path_edit))
        path_layout.addWidget(browse_btn)
        layout.addLayout(path_layout)

        layout.addStretch()

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()

        cancel_btn = QPushButton("取消")
        cancel_btn.setFixedSize(80, 36)
        cancel_btn.setCursor(Qt.PointingHandCursor)
        cancel_btn.setStyleSheet("""
            QPushButton {
                background: rgba(250, 251, 252, 0.75);
                border: 1px solid rgba(0, 0, 0, 0.10);
                border-radius: 6px;
                color: #1D1D1F;
                font-size: 13px;
            }
            QPushButton:hover {
                background: rgba(255, 255, 255, 0.95);
                border: 1px solid rgba(0, 0, 0, 0.16);
            }
        """)
        cancel_btn.clicked.connect(dialog.reject)
        btn_layout.addWidget(cancel_btn)

        ok_btn = QPushButton("添加")
        ok_btn.setFixedSize(80, 36)
        ok_btn.setCursor(Qt.PointingHandCursor)
        ok_btn.setStyleSheet("""
            QPushButton {
                background: rgba(10, 132, 255, 0.18);
                border: 1px solid rgba(10, 132, 255, 0.32);
                border-radius: 6px;
                color: #0A84FF;
                font-size: 13px;
                font-weight: 600;
            }
            QPushButton:hover {
                background: rgba(10, 132, 255, 0.28);
                border: 1px solid rgba(10, 132, 255, 0.45);
            }
            QPushButton:pressed {
                background: rgba(10, 132, 255, 0.40);
            }
        """)
        ok_btn.clicked.connect(dialog.accept)
        btn_layout.addWidget(ok_btn)
        layout.addLayout(btn_layout)

        if dialog.exec_() == QDialog.Accepted:
            name = name_edit.text().strip()
            path = path_edit.text().strip()
            if name and path:
                self._pin_app(name, path)

    def _browse_for_path(self, line_edit):
        filepath, _ = QFileDialog.getOpenFileName(
            self, "选择程序", "", "程序 (*.exe *.lnk);;所有文件 (*.*)"
        )
        if filepath:
            line_edit.setText(filepath)

    def _pin_app(self, name, path, icon_path=None):
        """固定一个应用到 Dock"""
        if any(a.get('path') == path for a in self.pinned_apps):
            return

        app_info = {
            'name': name,
            'path': path,
            'icon': icon_path
        }
        self.pinned_apps.append(app_info)
        self._save_pinned_apps()
        self._add_pinned_item(name, path, icon_path)

    def _add_pinned_item(self, name, path, icon_path=None):
        """添加固定项到 Dock UI"""
        item = DockItem(name, path, icon_path, self)
        item.launched.connect(self._launch_app)

        # 重写右键菜单：含"从 Dock 取消固定"（无 emoji）
        def custom_menu(pos):
            menu = QMenu(self)
            self._apply_menu_style(menu)

            open_action = QAction("打开", self)
            open_action.triggered.connect(lambda: self._launch_app(path))
            menu.addAction(open_action)

            menu.addSeparator()

            unpin_action = QAction("从 Dock 取消固定", self)
            unpin_action.triggered.connect(lambda: self._unpin_app(path, item))
            menu.addAction(unpin_action)

            menu.exec_(pos)

        item._show_context_menu = custom_menu

        self.apps_layout.addWidget(item)
        self._all_items.append(item)
        self._pinned_items.append(item)
        self._magnify.items = self._all_items
        return item

    def _unpin_app(self, path, item):
        """取消固定一个应用"""
        self.pinned_apps = [a for a in self.pinned_apps if a.get('path') != path]
        self._save_pinned_apps()
        self.remove_dock_item(item)

    def _launch_app(self, app_path):
        try:
            if os.path.exists(app_path):
                if sys.platform == 'win32':
                    os.startfile(app_path)
                elif sys.platform == 'darwin':
                    subprocess.Popen(['open', app_path])
                else:
                    subprocess.Popen(['xdg-open', app_path])
            else:
                subprocess.Popen(app_path, shell=True)
        except Exception as e:
            print(f"无法启动: {e}")

    # ============ 鼠标事件：拖动 + 放大 + 自动隐藏 ============

    def mousePressEvent(self, event):
        """左键点击 Dock 空白处可以拖动"""
        if event.button() == Qt.LeftButton:
            # 仅在点击 Dock 背景区域（非按钮）时启用拖动
            child = self.childAt(event.pos())
            if child is None:
                self._dragging = True
                self._drag_offset = event.globalPos() - self.pos()
            else:
                self._dragging = False
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        # 拖动 Dock
        if self._dragging and event.buttons() & Qt.LeftButton:
            new_pos = event.globalPos() - self._drag_offset
            self.move(new_pos)
        else:
            # 放大效果
            self._magnify.update_magnification(event.pos())

        if self._is_hidden:
            self._show_dock()
        self._auto_hide_timer.stop()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._dragging = False
        super().mouseReleaseEvent(event)

    def leaveEvent(self, event):
        self._magnify.reset()
        self._auto_hide_timer.start(2000)

    def enterEvent(self, event):
        if self._is_hidden:
            self._show_dock()

    def _auto_hide(self):
        if not self.rect().contains(self.mapFromGlobal(QCursor.pos())):
            self._hide_dock()

    def _hide_dock(self):
        """滑出屏幕底部"""
        if self._is_hidden:
            return

        self._is_hidden = True
        # 让 body 完全滑出屏幕底部
        # body_bottom = widget_top + SHADOW_MARGIN + DOCK_BODY_HEIGHT
        # 想让 body_top = screen.bottom() => widget_top = screen.bottom() - SHADOW_MARGIN
        target_y = self._screen_geo.bottom() - SHADOW_MARGIN

        if not hasattr(self, '_hide_anim') or self._hide_anim is None:
            self._hide_anim = QPropertyAnimation(self, b"pos")
        else:
            self._hide_anim.stop()
        self._hide_anim.setDuration(300)
        self._hide_anim.setStartValue(self.pos())
        self._hide_anim.setEndValue(QPoint(self.x(), target_y))
        self._hide_anim.setEasingCurve(QEasingCurve.InOutCubic)
        self._hide_anim.start()

    def _show_dock(self):
        """从屏幕底部滑入"""
        if not self._is_hidden:
            return

        self._is_hidden = False
        target_y = self._screen_geo.bottom() - DOCK_BOTTOM_GAP - SHADOW_MARGIN - DOCK_BODY_HEIGHT

        if not hasattr(self, '_show_anim') or self._show_anim is None:
            self._show_anim = QPropertyAnimation(self, b"pos")
        else:
            self._show_anim.stop()
        self._show_anim.setDuration(350)
        self._show_anim.setStartValue(self.pos())
        self._show_anim.setEndValue(QPoint(self.x(), target_y))
        self._show_anim.setEasingCurve(QEasingCurve.OutCubic)
        self._show_anim.start()

    # ============ 绘制 ============

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        rect = self.rect()

        # Dock 主体区域（inset 出 SHADOW_MARGIN 给阴影留位置）
        body_rect = QRectF(
            SHADOW_MARGIN, SHADOW_MARGIN,
            rect.width() - 2 * SHADOW_MARGIN,
            DOCK_BODY_HEIGHT
        )
        body_radius = 10.0

        # ===== 1. 柔和阴影（4px blur，~10% alpha，不用 QGraphicsDropShadowEffect）=====
        # 用多层叠加的圆角矩形 + 递减 alpha 模拟 4px 模糊
        # 阴影向下偏移一点（模拟顶光）
        shadow_layers = [
            (4, 5),   # 最外层，alpha 最低
            (3, 7),
            (2, 9),
            (1, 11),  # 最内层（紧贴 body），alpha 最高
        ]
        for offset, alpha in shadow_layers:
            shadow_rect = QRectF(body_rect).adjusted(
                -offset, -offset * 0.4, offset, offset
            )
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(0, 0, 0, alpha))
            painter.drawRoundedRect(
                shadow_rect,
                body_radius + offset,
                body_radius + offset
            )

        # ===== 2. Dock 主体背景：rgba(255,255,255,0.72) =====
        body_path = QPainterPath()
        body_path.addRoundedRect(body_rect, body_radius, body_radius)

        painter.setPen(Qt.NoPen)
        painter.setBrush(COLOR_BG)
        painter.drawPath(body_path)

        # ===== 3. 边框：1px solid rgba(0,0,0,0.05) =====
        painter.setPen(QPen(COLOR_BORDER, 1.0))
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(body_path)

        # ===== 4. 分隔线（竖线，1px，rgba(0,0,0,0.06)）=====
        if hasattr(self, '_separators'):
            for sep in self._separators:
                geo = sep.geometry()
                if geo.width() <= 0:
                    continue
                center_x = geo.center().x()
                # 限制在 body 内部
                sep_top = body_rect.top() + 8
                sep_bot = body_rect.bottom() - 8
                painter.setPen(QPen(COLOR_SEPARATOR, 1.0))
                painter.drawLine(
                    QPointF(center_x, sep_top),
                    QPointF(center_x, sep_bot)
                )
