import os
import sys
import subprocess
import json
from datetime import datetime
from PyQt5.QtCore import (
    Qt, QPoint, QSize, QTimer, QPropertyAnimation, QEasingCurve,
    pyqtSignal, QRect
)
from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout,
    QApplication, QMenu, QAction, QSystemTrayIcon, QSizePolicy, QToolTip,
    QFileDialog, QMessageBox, QInputDialog, QLineEdit
)
from PyQt5.QtGui import (
    QIcon, QPainter, QColor, QPixmap, QCursor, QFont, QBrush,
    QPainterPath, QLinearGradient, QRadialGradient, QPen, QPolygon
)
from PyQt5.QtCore import QRectF, QPointF
from .animations import BounceAnimation, DockMagnifyEffect
from .undo_panel import UndoButton


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
        """Liquid Glass Q弹点击 - Apple 风格弹性回弹"""
        # 停止之前的点击动画, 防止连续点击时动画冲突
        if hasattr(self, '_click_anim') and self._click_anim is not None:
            self._click_anim.stop()

        original_geo = self.geometry()

        # 按下效果 - 快速缩小
        anim1 = QPropertyAnimation(self, b"geometry")
        anim1.setDuration(80)
        expand = 4
        anim1.setStartValue(original_geo)
        anim1.setEndValue(original_geo.adjusted(-expand, -expand, expand, expand))
        anim1.setEasingCurve(QEasingCurve.OutQuad)

        # 弹回效果 - Q弹回弹 (OutElastic)
        anim2 = QPropertyAnimation(self, b"geometry")
        anim2.setDuration(350)
        anim2.setStartValue(original_geo.adjusted(-expand, -expand, expand, expand))
        anim2.setEndValue(original_geo)
        # 使用弹性曲线模拟液态Q弹
        curve = QEasingCurve(QEasingCurve.OutElastic)
        curve.setAmplitude(1.5)
        curve.setPeriod(0.35)
        anim2.setEasingCurve(curve)

        from PyQt5.QtCore import QSequentialAnimationGroup
        group = QSequentialAnimationGroup(self)
        group.addAnimation(anim1)
        group.addAnimation(anim2)
        # 保持引用防止被 GC, 连续点击时复用
        self._click_anim = group
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
    undo_triggered = pyqtSignal()

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

        self.pinned_apps = []  # 固定的应用列表
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

        self.setMouseTracking(True)

        # 加载固定的应用
        QTimer.singleShot(100, self._load_pinned_apps)

    def _setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(14, 9, 14, 9)
        layout.setSpacing(5)

        # Windows 徽标按钮（开始菜单）
        self.start_btn = self._create_start_button()
        layout.addWidget(self.start_btn)

        # 分隔符（Liquid Glass 风格）
        separator1 = QWidget()
        separator1.setFixedWidth(2)
        separator1.setStyleSheet("""
            background: transparent;
            max-width: 2px;
        """)
        self._separators = []
        self._separators.append(separator1)
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
        separator2.setFixedWidth(2)
        separator2.setStyleSheet("background: transparent; max-width: 2px;")
        self._separators.append(separator2)
        layout.addWidget(separator2)

        # App 区域
        self.apps_layout = QHBoxLayout()
        self.apps_layout.setSpacing(5)
        layout.addLayout(self.apps_layout)

        # 添加固定应用按钮
        self.add_pin_btn = self._create_system_button("➕", "添加常用软件/快捷方式")
        self.add_pin_btn.clicked.connect(self._on_add_pinned_app)
        layout.addWidget(self.add_pin_btn)

        layout.addStretch()

        # 分隔符
        separator3 = QWidget()
        separator3.setFixedWidth(2)
        separator3.setStyleSheet("background: transparent; max-width: 2px;")
        self._separators.append(separator3)
        layout.addWidget(separator3)

        # 撤销按钮
        self.undo_btn = UndoButton()
        self.undo_btn.undo_clicked.connect(self.undo_triggered.emit)
        layout.addWidget(self.undo_btn)

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
        for btn in [self.start_btn, self.search_btn, self.files_btn, self.organizer_btn, self.add_pin_btn, self.undo_btn, self.settings_btn]:
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

    # ============ 固定常用应用 ============

    def _load_pinned_apps(self):
        """加载固定的应用列表"""
        try:
            os.makedirs(os.path.dirname(self._pinned_config_path), exist_ok=True)
            if os.path.exists(self._pinned_config_path):
                with open(self._pinned_config_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.pinned_apps = data.get('apps', [])
                    # 添加到 Dock
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
        """点击添加固定应用按钮"""
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
                padding: 10px 20px;
                border-radius: 6px;
                font-size: 13px;
            }
            QMenu::item:hover {
                background: rgba(100, 150, 255, 0.35);
            }
        """)

        action_browse = QAction("📂  浏览程序...", self)
        action_browse.triggered.connect(self._browse_and_pin_app)
        menu.addAction(action_browse)

        action_shortcut = QAction("🔗  添加快捷方式...", self)
        action_shortcut.triggered.connect(self._add_shortcut_dialog)
        menu.addAction(action_shortcut)

        menu.addSeparator()

        # 推荐的常用软件
        common_apps = self._detect_common_apps()
        if common_apps:
            for app_name, app_path in common_apps[:6]:
                action = QAction(f"📌  {app_name}", self)
                action.triggered.connect(lambda checked, n=app_name, p=app_path: self._pin_app(n, p))
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
            if os.path.exists(expanded) or not os.path.sep in path:
                # 检查是否已经固定
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
            # 如果是快捷方式(.lnk)，尝试解析目标
            if filepath.lower().endswith('.lnk'):
                name = os.path.splitext(os.path.basename(filepath))[0]
            self._pin_app(name, filepath)

    def _add_shortcut_dialog(self):
        """通过对话框添加快捷方式"""
        dialog = QDialog(self)
        dialog.setWindowTitle("添加快捷方式")
        dialog.setFixedSize(400, 200)
        dialog.setStyleSheet("background: rgba(30, 30, 50, 0.98); color: white;")

        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        name_label = QLabel("名称:")
        name_label.setStyleSheet("font-size: 13px;")
        layout.addWidget(name_label)

        name_edit = QLineEdit()
        name_edit.setPlaceholderText("例如：我的常用工具")
        name_edit.setStyleSheet("""
            QLineEdit {
                background: rgba(255,255,255,0.08);
                border: 1px solid rgba(255,255,255,0.15);
                border-radius: 8px;
                padding: 8px 12px;
                color: white;
                font-size: 13px;
            }
        """)
        layout.addWidget(name_edit)

        path_label = QLabel("路径:")
        path_label.setStyleSheet("font-size: 13px;")
        layout.addWidget(path_label)

        path_layout = QHBoxLayout()
        path_edit = QLineEdit()
        path_edit.setPlaceholderText("例如：C:\\Program Files\\...\\app.exe")
        path_edit.setStyleSheet("""
            QLineEdit {
                background: rgba(255,255,255,0.08);
                border: 1px solid rgba(255,255,255,0.15);
                border-radius: 8px;
                padding: 8px 12px;
                color: white;
                font-size: 13px;
            }
        """)
        path_layout.addWidget(path_edit, 1)

        browse_btn = QPushButton("浏览")
        browse_btn.setFixedSize(60, 32)
        browse_btn.setCursor(Qt.PointingHandCursor)
        browse_btn.setStyleSheet("""
            QPushButton {
                background: rgba(100, 150, 255, 0.3);
                border: none;
                border-radius: 8px;
                color: white;
                font-size: 12px;
            }
            QPushButton:hover { background: rgba(100, 150, 255, 0.5); }
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
                background: rgba(255,255,255,0.08);
                border: none;
                border-radius: 8px;
                color: white;
                font-size: 13px;
            }
            QPushButton:hover { background: rgba(255,255,255,0.15); }
        """)
        cancel_btn.clicked.connect(dialog.reject)
        btn_layout.addWidget(cancel_btn)

        ok_btn = QPushButton("添加")
        ok_btn.setFixedSize(80, 36)
        ok_btn.setCursor(Qt.PointingHandCursor)
        ok_btn.setStyleSheet("""
            QPushButton {
                background: rgba(100, 150, 255, 0.5);
                border: none;
                border-radius: 8px;
                color: white;
                font-size: 13px;
                font-weight: 600;
            }
            QPushButton:hover { background: rgba(100, 150, 255, 0.7); }
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
        filepath, _ = QFileDialog.getOpenFileName(self, "选择程序", "", "程序 (*.exe *.lnk);;所有文件 (*.*)")
        if filepath:
            line_edit.setText(filepath)

    def _pin_app(self, name, path, icon_path=None):
        """固定一个应用到 Dock"""
        # 检查是否已经固定
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
        # 修改右键菜单，添加"取消固定"
        original_menu = item._show_context_menu

        def custom_menu(pos):
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
            open_action.triggered.connect(lambda: self._launch_app(path))
            menu.addAction(open_action)

            menu.addSeparator()

            unpin_action = QAction("📌  从 Dock 取消固定", self)
            unpin_action.triggered.connect(lambda: self._unpin_app(path, item))
            menu.addAction(unpin_action)

            menu.exec_(pos)

        item._show_context_menu = custom_menu

        self.apps_layout.addWidget(item)
        self._all_items.append(item)
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
        # 保持动画对象引用, 防止被 GC 中断
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
        if not self._is_hidden:
            return

        self._is_hidden = False
        target_y = self._screen_geo.bottom() - self.height() - 4
        # 保持动画对象引用, 防止被 GC 中断
        if not hasattr(self, '_show_anim') or self._show_anim is None:
            self._show_anim = QPropertyAnimation(self, b"pos")
        else:
            self._show_anim.stop()
        self._show_anim.setDuration(350)
        self._show_anim.setStartValue(self.pos())
        self._show_anim.setEndValue(QPoint(self.x(), target_y))
        self._show_anim.setEasingCurve(QEasingCurve.OutBack)
        self._show_anim.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        rect = self.rect()
        # 外发光（柔和阴影底托）
        glow_path = QPainterPath()
        glow_rect = QRectF(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
        glow_path.addRoundedRect(glow_rect, 26, 26)
        from PyQt5.QtGui import QRadialGradient, QPainterPath
        shadow = QRadialGradient(
            glow_rect.center().x(),
            glow_rect.bottom() - 2,
            glow_rect.width() * 0.55
        )
        shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
        shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
        shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(shadow))
        painter.drawPath(glow_path)

        # Liquid Glass 主体渐变
        from PyQt5.QtGui import QLinearGradient, QBrush
        body_path = QPainterPath()
        body_rect = QRectF(rect).adjusted(1.5, 1.5, -1.5, -1.5)
        body_path.addRoundedRect(body_rect, 24, 24)

        bg = QLinearGradient(0, 0, 0, rect.height())
        bg.setColorAt(0.0, QColor(58, 64, 92, 200))
        bg.setColorAt(0.35, QColor(38, 42, 62, 210))
        bg.setColorAt(1.0, QColor(22, 24, 38, 230))
        painter.fillPath(body_path, QBrush(bg))

        # 顶部高光（macOS 风格镜面反射）
        painter.setClipping(True)
        painter.setClipRect(2, 2, rect.width() - 4, rect.height() * 0.55)
        hl = QLinearGradient(0, 2, 0, rect.height() * 0.55 + 2)
        hl.setColorAt(0.0, QColor(255, 255, 255, 78))
        hl.setColorAt(0.6, QColor(255, 255, 255, 24))
        hl.setColorAt(1.0, QColor(255, 255, 255, 0))
        painter.fillPath(body_path, QBrush(hl))
        painter.setClipping(False)

        # 底部内阴影
        painter.setClipping(True)
        painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
        bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
        bs.setColorAt(0.0, QColor(0, 0, 0, 0))
        bs.setColorAt(1.0, QColor(0, 0, 0, 60))
        painter.fillPath(body_path, QBrush(bs))
        painter.setClipping(False)

        # 外边框（半透明白）
        painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(body_path)

        # 内部高光边框（Liquid Glass 内发光）
        inner_rect = QRectF(body_rect.x() + 1.5, body_rect.y() + 1.5,
                            body_rect.width() - 3, body_rect.height() - 3)
        inner_path = QPainterPath()
        inner_path.addRoundedRect(inner_rect, 22, 22)
        painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
        painter.drawPath(inner_path)

        # 顶部小反光条
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(255, 255, 255, 50))
        painter.drawRoundedRect(QRectF(5, 3, rect.width() - 10, 1.6), 1, 1)

        # 绘制分隔符（竖向发光条）
        if hasattr(self, '_separators'):
            for sep in self._separators:
                geo = sep.geometry()
                if geo.width() <= 0:
                    continue
                center_x = geo.center().x()
                sep_path = QPainterPath()
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                sep_rect = QRectF(center_x - 0.6, sep_top, 1.2, sep_bot - sep_top)
                sep_path.addRoundedRect(sep_rect, 0.6, 0.6)

                sep_grad = QLinearGradient(0, sep_top, 0, sep_bot)
                sep_grad.setColorAt(0.0, QColor(255, 255, 255, 0))
                sep_grad.setColorAt(0.5, QColor(255, 255, 255, 55))
                sep_grad.setColorAt(1.0, QColor(255, 255, 255, 0))
                painter.setBrush(QBrush(sep_grad))
                painter.setPen(Qt.NoPen)
                painter.drawPath(sep_path)
