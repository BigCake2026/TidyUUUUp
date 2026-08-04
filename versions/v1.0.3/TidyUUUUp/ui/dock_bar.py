import os
import sys
import subprocess
from datetime import datetime
from PyQt5.QtCore import (
    Qt, QPoint, QSize, QTimer, QPropertyAnimation, QEasingCurve,
    pyqtSignal, QRect
)
from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout,
    QApplication, QMenu, QAction, QSystemTrayIcon, QSizePolicy, QToolTip
)
from PyQt5.QtGui import QIcon, QPainter, QColor, QPixmap, QCursor, QFont
from .animations import BounceAnimation, DockMagnifyEffect


class DockItem(QPushButton):
    launched = pyqtSignal(str)

    def __init__(self, app_name, app_path, icon_path=None, parent=None):
        super().__init__(parent)
        self.app_name = app_name
        self.app_path = app_path
        self.setObjectName("DockItem")
        self.setFixedSize(56, 56)
        self.setCursor(Qt.PointingHandCursor)
        self.setToolTip(app_name)

        # 设置图标
        if icon_path and os.path.exists(icon_path):
            self.setIcon(QIcon(icon_path))
        else:
            self._create_default_icon()
        self.setIconSize(QSize(40, 40))

        self.clicked.connect(self._on_clicked)
        self._base_size = QSize(56, 56)
        self.setProperty("baseSize", self._base_size)

    def _create_default_icon(self):
        pixmap = QPixmap(40, 40)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制渐变背景
        gradient_colors = [
            QColor(120, 150, 255), QColor(150, 100, 255),
            QColor(255, 120, 180), QColor(100, 200, 255)
        ]
        import hashlib
        idx = int(hashlib.md5(self.app_name.encode()).hexdigest(), 16) % len(gradient_colors)
        color = gradient_colors[idx]

        painter.setBrush(color)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(0, 0, 40, 40, 10, 10)

        # 绘制首字母
        painter.setPen(QColor(255, 255, 255, 220))
        font = painter.font()
        font.setBold(True)
        font.setPointSize(18)
        painter.setFont(font)
        painter.drawText(pixmap.rect(), Qt.AlignCenter, self.app_name[0].upper() if self.app_name else "?")

        painter.end()
        self.setIcon(QIcon(pixmap))

    def _on_clicked(self):
        # Q弹点击动画
        self._bounce_click()
        QTimer.singleShot(150, lambda: self.launched.emit(self.app_path))

    def _bounce_click(self):
        original_geo = self.geometry()

        # 按下效果
        anim1 = QPropertyAnimation(self, b"geometry")
        anim1.setDuration(100)
        anim1.setStartValue(original_geo)
        expand = 3
        anim1.setEndValue(original_geo.adjusted(-expand, -expand, expand, expand))
        anim1.setEasingCurve(QEasingCurve.OutQuad)

        # 弹回效果
        anim2 = QPropertyAnimation(self, b"geometry")
        anim2.setDuration(200)
        anim2.setStartValue(original_geo.adjusted(-expand, -expand, expand, expand))
        anim2.setEndValue(original_geo)
        anim2.setEasingCurve(QEasingCurve.OutBack)

        from PyQt5.QtCore import QSequentialAnimationGroup
        group = QSequentialAnimationGroup(self)
        group.addAnimation(anim1)
        group.addAnimation(anim2)
        group.start()

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self._show_context_menu(event.globalPos())
        else:
            super().mousePressEvent(event)

    def _show_context_menu(self, pos):
        menu = QMenu(self)
        menu.setStyleSheet("""
            QMenu {
                background: rgba(35, 35, 50, 0.95);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 10px;
                padding: 6px;
                color: white;
            }
            QMenu::item {
                padding: 8px 20px;
                border-radius: 6px;
                font-size: 13px;
            }
            QMenu::item:hover {
                background: rgba(100, 150, 255, 0.35);
            }
        """)

        open_action = QAction("打开", self)
        open_action.triggered.connect(lambda: self.launched.emit(self.app_path))
        menu.addAction(open_action)

        menu.addSeparator()

        remove_action = QAction("从Dock移除", self)
        remove_action.triggered.connect(lambda: self._remove_from_dock())
        menu.addAction(remove_action)

        menu.exec_(pos)

    def _remove_from_dock(self):
        dock = self.window()
        if hasattr(dock, 'remove_dock_item'):
            dock.remove_dock_item(self)


class DockBar(QWidget):
    search_triggered = pyqtSignal()
    files_triggered = pyqtSignal()
    organizer_triggered = pyqtSignal()
    settings_triggered = pyqtSignal()

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

        self._setup_ui()
        self._setup_position()
        self._setup_magnify_effect()

        self._is_hidden = False
        self._auto_hide_timer = QTimer(self)
        self._auto_hide_timer.setSingleShot(True)
        self._auto_hide_timer.timeout.connect(self._auto_hide)

        self.setMouseTracking(True)

    def _setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(6)

        # Windows 徽标按钮（开始菜单）
        self.start_btn = self._create_start_button()
        layout.addWidget(self.start_btn)

        # 分隔符
        separator1 = QWidget()
        separator1.setFixedWidth(1)
        separator1.setStyleSheet("background: rgba(255, 255, 255, 0.15);")
        layout.addWidget(separator1)

        # 系统功能按钮
        self.search_btn = self._create_system_button("🔍", "搜索")
        self.search_btn.clicked.connect(self.search_triggered.emit)
        layout.addWidget(self.search_btn)

        self.files_btn = self._create_system_button("📁", "文件")
        self.files_btn.clicked.connect(self.files_triggered.emit)
        layout.addWidget(self.files_btn)

        self.organizer_btn = self._create_system_button("🧹", "整理")
        self.organizer_btn.clicked.connect(self.organizer_triggered.emit)
        layout.addWidget(self.organizer_btn)

        # 分隔符
        separator2 = QWidget()
        separator2.setFixedWidth(1)
        separator2.setStyleSheet("background: rgba(255, 255, 255, 0.15);")
        layout.addWidget(separator2)

        # App 区域
        self.apps_layout = QHBoxLayout()
        self.apps_layout.setSpacing(6)
        layout.addLayout(self.apps_layout)

        layout.addStretch()

        # 系统托盘区域 - 时间显示
        self.time_widget = self._create_time_widget()
        layout.addWidget(self.time_widget)

        # 系统设置按钮
        self.settings_btn = self._create_system_button("⚙️", "设置")
        self.settings_btn.clicked.connect(self.settings_triggered.emit)
        layout.addWidget(self.settings_btn)

    def _create_system_button(self, emoji, tooltip):
        btn = QPushButton(emoji)
        btn.setObjectName("DockItem")
        btn.setFixedSize(56, 56)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setToolTip(tooltip)
        btn.setStyleSheet("font-size: 26px;")
        btn.setProperty("baseSize", QSize(56, 56))
        return btn

    def _create_start_button(self):
        btn = QPushButton()
        btn.setObjectName("StartButton")
        btn.setFixedSize(56, 56)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setToolTip("开始菜单")
        btn.setProperty("baseSize", QSize(56, 56))

        # 绘制 Windows 11 风格的徽标（四个蓝色方块）
        pixmap = QPixmap(36, 36)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        # Windows 蓝色渐变
        from PyQt5.QtGui import QLinearGradient
        gradient = QLinearGradient(0, 0, 36, 36)
        gradient.setColorAt(0, QColor(0, 120, 215))
        gradient.setColorAt(1, QColor(0, 180, 255))
        painter.setBrush(gradient)

        # 四个方块（Windows 徽标）
        gap = 3
        size = 15
        # 左上
        painter.drawRoundedRect(0, 0, size, size, 3, 3)
        # 右上
        painter.drawRoundedRect(size + gap, 0, size, size, 3, 3)
        # 左下
        painter.drawRoundedRect(0, size + gap, size, size, 3, 3)
        # 右下
        painter.drawRoundedRect(size + gap, size + gap, size, size, 3, 3)

        painter.end()
        btn.setIcon(QIcon(pixmap))
        btn.setIconSize(QSize(36, 36))

        btn.clicked.connect(self._toggle_windows_start)
        return btn

    def _toggle_windows_start(self):
        # 直接调用 Windows 原生开始菜单（模拟 Win 键按下）
        try:
            if sys.platform == 'win32':
                import ctypes
                from ctypes import wintypes

                # 定义键盘事件常量
                KEYEVENTF_KEYUP = 0x0002
                VK_LWIN = 0x5B  # 左 Win 键

                user32 = ctypes.windll.user32
                # 按下 Win 键
                user32.keybd_event(VK_LWIN, 0, 0, 0)
                # 释放 Win 键
                user32.keybd_event(VK_LWIN, 0, KEYEVENTF_KEYUP, 0)
            elif sys.platform == 'darwin':
                # macOS 上打开 Spotlight / Launchpad
                subprocess.Popen(['osascript', '-e', 'tell application "System Events" to keystroke space using command down'])
            else:
                # Linux 上显示开始菜单的 fallback
                self._show_start_menu()
        except Exception as e:
            print(f"打开开始菜单失败: {e}")
            # 失败则回退到自定义菜单
            self._show_start_menu()

    def _create_time_widget(self):
        widget = QWidget()
        widget.setFixedHeight(56)
        widget.setObjectName("TimeWidget")
        widget.setCursor(Qt.PointingHandCursor)

        layout = QVBoxLayout(widget)
        layout.setContentsMargins(10, 4, 10, 4)
        layout.setSpacing(0)

        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("""
            color: white;
            font-size: 13px;
            font-weight: 600;
        """)

        self.date_label = QLabel()
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setStyleSheet("""
            color: rgba(255, 255, 255, 0.7);
            font-size: 10px;
        """)

        layout.addWidget(self.time_label)
        layout.addWidget(self.date_label)

        # 每秒更新时间
        self._time_timer = QTimer(self)
        self._time_timer.timeout.connect(self._update_time)
        self._time_timer.start(1000)
        self._update_time()

        # 点击显示日历/设置
        widget.mousePressEvent = self._on_time_clicked

        return widget

    def _update_time(self):
        now = datetime.now()
        self.time_label.setText(now.strftime("%H:%M:%S"))
        self.date_label.setText(now.strftime("%Y年%m月%d日"))

    def _on_time_clicked(self, event):
        if event.button() == Qt.LeftButton:
            self._show_calendar_menu(event.globalPos())

    def _show_start_menu(self):
        menu = QMenu(self)
        menu.setStyleSheet("""
            QMenu {
                background: rgba(35, 35, 50, 0.97);
                backdrop-filter: blur(30px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 14px;
                padding: 8px;
                color: white;
                min-width: 240px;
            }
            QMenu::item {
                padding: 10px 18px;
                border-radius: 8px;
                font-size: 14px;
            }
            QMenu::item:hover {
                background: rgba(100, 150, 255, 0.35);
            }
            QMenu::separator {
                height: 1px;
                background: rgba(255, 255, 255, 0.1);
                margin: 6px 10px;
            }
        """)

        # 常用程序
        explorer_action = QAction("📁  文件资源管理器", self)
        explorer_action.triggered.connect(lambda: self._run_system_cmd("explorer"))
        menu.addAction(explorer_action)

        settings_action = QAction("⚙️  设置", self)
        settings_action.triggered.connect(lambda: self._run_system_cmd("ms-settings:"))
        menu.addAction(settings_action)

        cmd_action = QAction("💻  命令提示符", self)
        cmd_action.triggered.connect(lambda: self._run_system_cmd("cmd"))
        menu.addAction(cmd_action)

        taskmgr_action = QAction("📊  任务管理器", self)
        taskmgr_action.triggered.connect(lambda: self._run_system_cmd("taskmgr"))
        menu.addAction(taskmgr_action)

        menu.addSeparator()

        # 系统操作
        run_action = QAction("🔍  运行 (Win+R)", self)
        run_action.triggered.connect(lambda: self._run_system_cmd("shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}"))
        menu.addAction(run_action)

        menu.addSeparator()

        # 电源操作
        shutdown_action = QAction("⏻  关机", self)
        shutdown_action.triggered.connect(lambda: self._run_system_cmd("shutdown /s /t 0"))
        menu.addAction(shutdown_action)

        restart_action = QAction("↻  重启", self)
        restart_action.triggered.connect(lambda: self._run_system_cmd("shutdown /r /t 0"))
        menu.addAction(restart_action)

        sleep_action = QAction("⏾  睡眠", self)
        sleep_action.triggered.connect(lambda: self._run_system_cmd("rundll32.exe powrprof.dll,SetSuspendState 0,1,0"))
        menu.addAction(sleep_action)

        menu.exec_(self.start_btn.mapToGlobal(QPoint(0, -menu.sizeHint().height())))

    def _show_calendar_menu(self, pos):
        now = datetime.now()
        weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

        QToolTip.showText(
            pos,
            f"<div style='padding: 8px; font-size: 13px;'>"
            f"<b style='font-size: 16px;'>{now.strftime('%H:%M:%S')}</b><br>"
            f"<span style='color: #888;'>{now.strftime('%Y年%m月%d日')} {weekdays[now.weekday()]}</span>"
            f"</div>"
        )

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

    def _setup_position(self):
        dock_width = min(900, int(self._screen_geo.width() * 0.6))
        dock_height = 72
        x = (self._screen_geo.width() - dock_width) // 2
        y = self._screen_geo.bottom() - dock_height - 4

        self.setGeometry(x, y, dock_width, dock_height)

    def _setup_magnify_effect(self):
        self._all_items = []
        self._magnify = DockMagnifyEffect(self, self._all_items, magnify_scale=1.4, radius=100)
        # 系统按钮也加入放大效果
        QTimer.singleShot(100, self._register_system_buttons)

    def _register_system_buttons(self):
        for btn in [self.start_btn, self.search_btn, self.files_btn, self.organizer_btn, self.settings_btn]:
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
        item.setParent(None)
        item.deleteLater()

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

    def mouseMoveEvent(self, event):
        self._magnify.update_magnification(event.pos())
        if self._is_hidden:
            self._show_dock()
        self._auto_hide_timer.stop()

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
        if self._is_hidden:
            return

        self._is_hidden = True
        target_y = self._screen_geo.bottom() - 8
        anim = QPropertyAnimation(self, b"pos")
        anim.setDuration(300)
        anim.setStartValue(self.pos())
        anim.setEndValue(QPoint(self.x(), target_y))
        anim.setEasingCurve(QEasingCurve.InOutCubic)
        anim.start()

    def _show_dock(self):
        if not self._is_hidden:
            return

        self._is_hidden = False
        target_y = self._screen_geo.bottom() - self.height() - 4
        anim = QPropertyAnimation(self, b"pos")
        anim.setDuration(350)
        anim.setStartValue(self.pos())
        anim.setEndValue(QPoint(self.x(), target_y))
        anim.setEasingCurve(QEasingCurve.OutBack)
        anim.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制磨砂玻璃背景
        rect = self.rect()

        # 渐变背景
        from PyQt5.QtGui import QLinearGradient, QBrush
        gradient = QLinearGradient(0, 0, 0, rect.height())
        gradient.setColorAt(0, QColor(30, 30, 45, 180))
        gradient.setColorAt(1, QColor(20, 20, 35, 200))
        painter.setBrush(QBrush(gradient))
        painter.setPen(QColor(255, 255, 255, 25))
        painter.drawRoundedRect(rect, 24, 24)

        # 高光
        painter.setBrush(QColor(255, 255, 255, 15))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(2, 2, rect.width() - 4, 2, 2, 2)
