#!/usr/bin/env python3
"""
TidyUUUUp - 智能工作台
Liquid Glass 设计的 Windows 任务栏替代品

支持：
  - 文件智能整理、快速索引搜索
  - 智能桌面监控，新文件1秒内自动分类
  - 虚拟分类文件夹（工作/娱乐/学习/图片/下载...）
  - 悬浮球模式（不使用时最小化为小圆球）
  - 全部功能永久免费使用
"""

import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QTimer, QPoint, QObject
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor, QFont

from ui.styles import apply_liquid_glass
from ui.dock_bar import DockBar
from ui.main_window import MainWindow
from ui.floating_ball import FloatingBall
from ui.zone_panel import ZonePanel, ZoneFolderButton, DirectoryTreePopup
from ui.undo_panel import UndoPanel
from ui.quick_look import QuickLookPanel

from core.smart_engine import SmartRuleEngine
from core.desktop_watcher import DesktopWatcher
from core.updater import UpdateChecker, CURRENT_VERSION
from core.system_integration import (
    create_desktop_shortcut, is_desktop_shortcut_exists, remove_desktop_shortcut,
    enable_autostart, disable_autostart, is_autostart_enabled,
    run_first_time_setup, is_windows
)


def create_app_icon():
    pixmap = QPixmap(64, 64)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)

    from PyQt5.QtGui import QLinearGradient
    gradient = QLinearGradient(0, 0, 64, 64)
    gradient.setColorAt(0, QColor(100, 150, 255))
    gradient.setColorAt(1, QColor(180, 100, 255))
    painter.setBrush(gradient)
    painter.setPen(Qt.NoPen)
    painter.drawRoundedRect(4, 4, 56, 56, 16, 16)

    painter.setPen(QColor(255, 255, 255, 230))
    font = QFont()
    font.setBold(True)
    font.setPointSize(28)
    painter.setFont(font)
    painter.drawText(pixmap.rect(), Qt.AlignCenter, "◇")

    painter.end()
    return QIcon(pixmap)


class TidyUUUUpApp(QObject):
    def __init__(self):
        super().__init__()
        self.app = QApplication(sys.argv)
        self.app.setQuitOnLastWindowClosed(False)
        self.app.setApplicationName("TidyUUUUp")

        apply_liquid_glass(self.app)

        self.icon = create_app_icon()
        self.app.setWindowIcon(self.icon)

        # 核心模块
        self.smart_engine = SmartRuleEngine()

        # 窗口
        self.main_window = MainWindow()
        screen = self.app.primaryScreen().geometry()
        self.dock = DockBar(screen)

        # 桌面监控
        self.desktop_watcher = DesktopWatcher(self.smart_engine)
        self.desktop_watcher.file_detected.connect(self._on_file_detected)
        self.desktop_watcher.organize_completed.connect(self._on_organize_completed)

        # 撤销面板
        self.undo_panel = UndoPanel(self.desktop_watcher.undo_manager)
        self.undo_panel.undo_performed.connect(self._on_undo_performed)

        # 撤销记录数更新
        self.desktop_watcher.undo_manager.undo_record_added.connect(self._on_undo_record_added)

        # Quick Look 预览面板
        self.quick_look = QuickLookPanel()
        self._selected_file_for_preview = None

        # 安装全局事件过滤器，捕获空格键
        self.app.installEventFilter(self)

        # 悬浮球
        self.floating_ball = FloatingBall()
        self.floating_ball.clicked.connect(self._toggle_ball_mode)
        self.floating_ball.double_clicked.connect(self.main_window.show)
        self.floating_ball.right_clicked.connect(self._show_ball_menu)
        self._ball_mode = 'dock'

        # 智能分类面板
        self.zone_panel = ZonePanel(self.smart_engine, self.main_window.file_index)
        self._zone_buttons = []

        # 悬停目录树弹出面板
        self._tree_popup = DirectoryTreePopup()
        self._tree_popup.file_activated.connect(self._on_tree_file_activated)
        self._current_hovered_zone = None

        # 信号连接
        self.dock.search_triggered.connect(self._show_main_and_focus_search)
        self.dock.files_triggered.connect(self.main_window.show)
        self.dock.organizer_triggered.connect(self._show_organizer_tab)
        self.dock.undo_triggered.connect(self._show_undo_panel)
        self.main_window.show_dock.connect(self.dock._show_dock)

        # 系统托盘
        self._setup_tray()

        # 默认应用
        self._load_default_apps()

        # 智能分类文件夹按钮
        self._load_zone_buttons()

        # 启动桌面监控
        QTimer.singleShot(2000, self._start_desktop_watcher)

        # 初始化撤销按钮状态
        QTimer.singleShot(2500, self._refresh_undo_button)

        # 启动后 3 秒检查更新（不影响启动速度）
        QTimer.singleShot(3000, self._check_updates)

        # 首次运行：创建桌面快捷方式
        QTimer.singleShot(1000, self._first_time_setup)

    def _setup_tray(self):
        self.tray = QSystemTrayIcon(self.icon)
        self.tray.setToolTip("TidyUUUUp")

        menu = QMenu()
        menu.setStyleSheet("""
            QMenu {
                background: rgba(35, 35, 50, 0.95);
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
            QMenu::separator {
                height: 1px;
                background: rgba(255,255,255,0.1);
                margin: 4px 8px;
            }
        """)

        show_main = QAction("📋 打开主界面", self.app)
        show_main.triggered.connect(self.main_window.show)
        menu.addAction(show_main)

        show_dock = QAction("🪟 显示Dock栏", self.app)
        show_dock.triggered.connect(self._show_dock_and_ball)
        menu.addAction(show_dock)

        toggle_ball = QAction("🟢 悬浮球模式", self.app)
        toggle_ball.triggered.connect(self._toggle_ball_mode)
        menu.addAction(toggle_ball)

        menu.addSeparator()

        organize_action = QAction("🧹 整理桌面", self.app)
        organize_action.triggered.connect(self._organize_desktop)
        menu.addAction(organize_action)

        rescan = QAction("🔄 重新扫描文件", self.app)
        rescan.triggered.connect(self._rescan_files)
        menu.addAction(rescan)

        menu.addSeparator()

        about_action = QAction(f"ℹ️  关于 (v{CURRENT_VERSION})", self.app)
        about_action.triggered.connect(self._show_about)
        menu.addAction(about_action)

        check_update_action = QAction("🔄  检查更新", self.app)
        check_update_action.triggered.connect(lambda: self._check_updates(force=True))
        menu.addAction(check_update_action)

        menu.addSeparator()

        # 桌面快捷方式
        if is_desktop_shortcut_exists():
            shortcut_action = QAction("🗑️  删除桌面快捷方式", self.app)
            shortcut_action.triggered.connect(self._on_remove_desktop_shortcut)
        else:
            shortcut_action = QAction("📌  创建桌面快捷方式", self.app)
            shortcut_action.triggered.connect(self._on_create_desktop_shortcut)
        menu.addAction(shortcut_action)

        # 开机自启
        if is_autostart_enabled():
            autostart_action = QAction("🚫  禁用开机自启", self.app)
            autostart_action.triggered.connect(self._on_disable_autostart)
        else:
            autostart_action = QAction("⚡  开机自动启动", self.app)
            autostart_action.triggered.connect(self._on_enable_autostart)
        menu.addAction(autostart_action)

        menu.addSeparator()

        quit_action = QAction("退出", self.app)
        quit_action.triggered.connect(self._quit)
        menu.addAction(quit_action)

        self.tray.setContextMenu(menu)
        self.tray.activated.connect(self._on_tray_activated)
        self.tray.show()

    def _on_tray_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            if self._ball_mode == 'ball':
                self._toggle_ball_mode()
            else:
                if self.main_window.isVisible():
                    self.main_window.hide()
                else:
                    self.main_window.show()

    def _show_main_and_focus_search(self):
        self.main_window.show()
        self.main_window.raise_()
        self.main_window.activateWindow()
        QTimer.singleShot(100, lambda: self.main_window.search_box.setFocus())

    def _show_organizer_tab(self):
        self.main_window.show()
        self.main_window.raise_()
        self.main_window.activateWindow()
        self.main_window.tabs.setCurrentIndex(1)

    def _rescan_files(self):
        self.main_window._initial_scan()
        self._update_zone_file_counts()

    def _show_toast(self, msg):
        self.main_window.toast.show_toast(msg, 3000)

    def _load_default_apps(self):
        default_apps = [
            ("文件资源管理器", "explorer.exe"),
            ("Chrome", r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
            ("Edge", r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
            ("VS Code", r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe"),
            ("设置", "ms-settings:"),
        ]

        config_path = os.path.join(os.path.expanduser('~'), '.nexus_dock', 'dock_config.json')
        apps_to_load = default_apps

        if os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    apps_to_load = config.get('apps', default_apps)
            except Exception:
                pass

        for name, path in apps_to_load:
            expanded_path = os.path.expandvars(path)
            self.dock.add_app(name, expanded_path)

    # ============ 智能分类文件夹 ============

    def _load_zone_buttons(self):
        zones = self.smart_engine.get_all_zones()

        for zone_name, zone_config in zones.items():
            btn = ZoneFolderButton(zone_name, zone_config)
            btn.zone_clicked.connect(self._on_zone_clicked)
            btn.zone_hovered.connect(self._on_zone_hovered)
            btn.zone_left.connect(self._on_zone_left)
            self._zone_buttons.append(btn)
            self.dock.apps_layout.addWidget(btn)
            self.dock._all_items.append(btn)

        self.dock._magnify.items = self.dock._all_items
        QTimer.singleShot(3000, self._update_zone_file_counts)

    def _on_zone_hovered(self, btn, anchor_global):
        """鼠标悬停在 ZoneFolderButton 上 → 显示该分类的目录树"""
        self._current_hovered_zone = btn.zone_name
        zone_config = self.smart_engine.get_all_zones().get(btn.zone_name, {})
        zone_color = zone_config.get('color', '#4A7FFF')
        zone_icon = zone_config.get('icon', '📁')

        # 获取文件列表（从 file_index 扫描该 zone）
        files = self._collect_zone_files(btn.zone_name)
        self._tree_popup.populate_from_files(files, btn.zone_name, zone_icon, zone_color)
        self._tree_popup.show_above(anchor_global)

    def _on_zone_left(self):
        """鼠标离开 ZoneFolderButton → 启动延迟自动隐藏（鼠标进入 popup 时会被取消）"""
        self._tree_popup.restart_auto_hide(delay_ms=280)

    def _collect_zone_files(self, zone_name):
        """收集某个 zone 下的文件列表，用于目录树显示"""
        files = []
        if self.main_window.file_index:
            try:
                with self.main_window.file_index._lock:
                    all_items = list(self.main_window.file_index.index.items())
            except Exception:
                all_items = list(self.main_window.file_index.index.items())
            for filepath, info in all_items:
                classified_zone, _ = self.smart_engine.classify(filepath)
                if classified_zone == zone_name:
                    files.append(dict(info, path=filepath, name=os.path.basename(filepath)))
        # 按修改时间倒序，取前 80 个，避免目录树过大
        files.sort(key=lambda x: x.get('modified', 0), reverse=True)
        return files[:80]

    def _on_tree_file_activated(self, filepath):
        """目录树中双击文件 → 发送 toast 通知"""
        try:
            name = os.path.basename(filepath)
            self._show_toast(f"📄 已打开: {name[:26]}")
        except Exception:
            pass

    def _update_zone_file_counts(self):
        if not self.main_window.file_index:
            return

        # 一次遍历计算所有 zone 计数, 而非每个 zone 遍历一次 (O(n) vs O(n*m))
        # 同时在锁内取文件列表快照, 避免迭代时 watchdog 线程修改 dict 抛 RuntimeError
        counts = {btn.zone_name: 0 for btn in self._zone_buttons}
        try:
            with self.main_window.file_index._lock:
                filepaths = list(self.main_window.file_index.index.keys())
        except Exception:
            filepaths = list(self.main_window.file_index.index.keys())

        for filepath in filepaths:
            zone, _ = self.smart_engine.classify(filepath)
            if zone in counts:
                counts[zone] += 1

        for btn in self._zone_buttons:
            btn.set_file_count(counts.get(btn.zone_name, 0))

    def _on_zone_clicked(self, zone_name):
        btn = self.sender()
        if btn:
            global_pos = btn.mapToGlobal(btn.rect().center())
            self.zone_panel.show_zone(zone_name, global_pos)

    # ============ 桌面监控 ============

    def _start_desktop_watcher(self):
        self.desktop_watcher.start()
        self.desktop_watcher.ensure_zone_folders()
        self._show_toast("👀 桌面实时监控已启动，新文件将自动虚拟分类")

    def _on_file_detected(self, filepath, zone):
        filename = os.path.basename(filepath)
        self._show_toast(f"📁 已自动分类: {filename[:20]} → {zone}")
        self._update_zone_file_counts()

    def _on_organize_completed(self, results):
        total = results.get('total', 0)
        organized = results.get('organized', {})
        is_virtual = results.get('virtual_mode', True)

        if is_virtual:
            msg = f"✅ 虚拟分类完成！共分类 {total} 个文件\n\n"
            msg += "📁 点击 Dock 栏上的分类文件夹查看对应文件\n"
            msg += "📌 桌面文件保持原样，未被移动\n\n"
        else:
            msg = f"✅ 桌面整理完成！共处理 {total} 个文件\n"

        for zone, files in organized.items():
            msg += f"  {zone}: {len(files)} 个\n"
        QMessageBox.information(self.main_window, "整理完成", msg)
        self._update_zone_file_counts()

    def _organize_desktop(self):
        reply = QMessageBox.question(
            self.main_window, "整理桌面",
            "是否对桌面上所有文件进行虚拟分类？\n\n"
            "✅ 文件不会被移动，桌面保持原样\n"
            "✅ 只在 Dock 栏上创建虚拟分类文件夹\n"
            "✅ 点击虚拟文件夹可快速查看对应类型的文件",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )

        if reply == QMessageBox.Yes:
            self._show_toast("🔄 正在虚拟分类桌面文件...")
            QTimer.singleShot(100, self._do_virtual_organize)

    def _do_virtual_organize(self):
        """执行虚拟整理（只分类，不移动）"""
        # 确保先扫描桌面文件
        if self.main_window.file_index:
            desktop_path = self.desktop_watcher.desktop_path
            if os.path.exists(desktop_path):
                self.main_window.file_index.scan_directory(desktop_path, recursive=False)

        # 执行虚拟整理
        results = self.desktop_watcher.organize_all()

        # 更新分类文件计数
        self._update_zone_file_counts()

    # ============ 悬浮球模式 ============

    def _toggle_ball_mode(self):
        if self._ball_mode == 'dock':
            self.dock.hide()
            self.floating_ball.show()
            self._ball_mode = 'ball'
            self._show_toast("🟢 已切换到悬浮球模式，双击展开")
        else:
            self.floating_ball.hide()
            self.dock.show()
            self._ball_mode = 'dock'
            self._show_toast("🪟 已切换到Dock栏模式")

    def _show_dock_and_ball(self):
        if self._ball_mode == 'ball':
            self._toggle_ball_mode()
        else:
            self.dock._show_dock()

    def _show_ball_menu(self, pos):
        menu = QMenu()
        menu.setStyleSheet("""
            QMenu {
                background: rgba(35, 35, 50, 0.95);
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

        show_main = QAction("📋 打开主界面", self.app)
        show_main.triggered.connect(self.main_window.show)
        menu.addAction(show_main)

        toggle = QAction("🪟 切换到Dock栏", self.app)
        toggle.triggered.connect(self._toggle_ball_mode)
        menu.addAction(toggle)

        menu.addSeparator()

        organize = QAction("🧹 整理桌面", self.app)
        organize.triggered.connect(self._organize_desktop)
        menu.addAction(organize)

        menu.exec_(pos)

    # ============ 撤销功能 ============

    def _show_undo_panel(self):
        global_pos = self.dock.undo_btn.mapToGlobal(self.dock.undo_btn.rect().center())
        self.undo_panel.show_panel(global_pos)

    def _refresh_undo_button(self):
        count = self.desktop_watcher.undo_manager.get_record_count()
        self.dock.undo_btn.set_record_count(count)

    def _on_undo_record_added(self, count):
        self.dock.undo_btn.set_record_count(count)

    def _on_undo_performed(self, restored, skipped):
        self._refresh_undo_button()
        self._update_zone_file_counts()
        if restored > 0:
            self._show_toast(f"↩ 已撤销！恢复了 {restored} 个文件")

    # ============ 自动更新 ============

    def _check_updates(self, force=False):
        """检查更新"""
        # 若旧检查线程仍在运行 (网络慢/超时), 先优雅终止并等待退出,
        # 避免直接覆盖引用导致 QThread 被销毁时报 "Destroyed while still running"
        if hasattr(self, 'update_checker') and self.update_checker is not None:
            try:
                if self.update_checker.isRunning():
                    self.update_checker.quit()
                    self.update_checker.wait(2000)
            except Exception:
                pass

        self.update_checker = UpdateChecker()
        self.update_checker.check_finished.connect(lambda has_update, info: self._on_update_checked(has_update, info, force))
        self.update_checker.error_occurred.connect(lambda err: self._on_update_error(err, force))
        self.update_checker.start()

    def _on_update_checked(self, has_update, info, force=False):
        if has_update:
            if force:
                # 手动检查才弹窗
                from ui.update_dialog import UpdateDialog
                self.update_dialog = UpdateDialog(info)
                self.update_dialog.show_at_center()
            else:
                # 自动检查只显示 toast 提示，不弹窗打扰
                self._show_toast(f"🔄 发现新版本 v{info.get('latest_version','')}，右键托盘 → 检查更新 可更新")
        elif force:
            # 手动检查但没有更新
            self._show_toast(f"✅ 当前已是最新版本 (v{CURRENT_VERSION})")

    def _on_update_error(self, error, force=False):
        if force:
            self._show_toast(f"❌ 检查更新失败: {error}")

    def _show_about(self):
        from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton
        dialog = QDialog()
        dialog.setWindowTitle("关于 TidyUUUUp")
        dialog.setFixedSize(400, 240)
        dialog.setStyleSheet("background: rgba(30, 30, 50, 0.98); color: white; border-radius: 16px;")

        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(30, 30, 30, 20)

        title = QLabel("✨  TidyUUUUp")
        title.setStyleSheet("font-size: 22px; font-weight: 700;")
        title.setAlignment(Qt.AlignCenter)

        version = QLabel(f"版本 v{CURRENT_VERSION}")
        version.setStyleSheet("color: rgba(255,255,255,0.5); font-size: 13px;")
        version.setAlignment(Qt.AlignCenter)

        desc = QLabel("Liquid Glass 设计的智能工作台\n文件自动整理 · 桌面实时监控")
        desc.setStyleSheet("color: rgba(255,255,255,0.7); font-size: 13px;")
        desc.setAlignment(Qt.AlignCenter)

        close_btn = QPushButton("关闭")
        close_btn.setFixedHeight(38)
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.setStyleSheet("""
            QPushButton {
                background: rgba(255, 255, 255, 0.1);
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 13px;
                font-weight: 600;
            }
            QPushButton:hover { background: rgba(255, 255, 255, 0.18); }
        """)
        close_btn.clicked.connect(dialog.accept)

        layout.addWidget(title)
        layout.addWidget(version)
        layout.addSpacing(10)
        layout.addWidget(desc)
        layout.addStretch()
        layout.addWidget(close_btn)

        dialog.exec_()

    def _quit(self):
        self.dock.close()
        self.main_window.close()
        self.floating_ball.close()
        self.zone_panel.close()
        self.undo_panel.close()
        self.quick_look.close()
        self.tray.hide()
        try:
            self.desktop_watcher.stop()
        except Exception:
            pass
        QApplication.quit()

    def eventFilter(self, obj, event):
        """全局事件过滤器 - 捕获空格键实现 Quick Look"""
        from PyQt5.QtCore import QEvent
        from PyQt5.QtGui import QKeyEvent

        if event.type() == QEvent.KeyPress:
            key_event = QKeyEvent(event)
            if key_event.key() == Qt.Key_Space:
                # 如果 Quick Look 已显示，按空格关闭
                if self.quick_look.isVisible():
                    self.quick_look.close()
                    return True

                # 尝试从主窗口获取选中的文件
                selected_file = self._get_selected_file()
                if selected_file and os.path.exists(selected_file):
                    # 获取鼠标位置或屏幕中心
                    from PyQt5.QtGui import QCursor
                    pos = QCursor.pos()
                    self.quick_look.preview_file(selected_file, self.smart_engine)
                    self.quick_look.show_panel(pos)
                    return True

        return super().eventFilter(obj, event)

    def _get_selected_file(self):
        """获取当前选中的文件路径"""
        # 从主窗口的文件列表获取选中项
        if self.main_window and self.main_window.file_list:
            current_item = self.main_window.file_list.currentItem()
            if current_item:
                widget = self.main_window.file_list.itemWidget(current_item)
                if widget and hasattr(widget, 'file_info'):
                    return widget.file_info.get('path', '')
        return None

    def _first_time_setup(self):
        """首次运行设置"""
        try:
            setup_marker = os.path.join(
                os.path.expanduser('~'), '.nexus_dock', 'setup_completed'
            )
            os.makedirs(os.path.dirname(setup_marker), exist_ok=True)

            if not os.path.exists(setup_marker):
                # 首次运行
                if is_windows():
                    # Windows 系统：创建桌面快捷方式
                    ok = create_desktop_shortcut()
                    if ok:
                        self.main_window.toast.show_toast("📌 桌面快捷方式已创建！", 4000)

                # 标记设置已完成
                with open(setup_marker, 'w') as f:
                    f.write('v1.0.7')
        except Exception as e:
            print(f"首次设置失败: {e}")

    def _on_create_desktop_shortcut(self):
        """创建桌面快捷方式"""
        ok = create_desktop_shortcut()
        if ok:
            self.main_window.toast.show_toast("✅ 桌面快捷方式已创建！", 3000)
        else:
            self.main_window.toast.show_toast("❌ 创建失败，请检查权限", 3000)
        # 刷新托盘菜单
        self._setup_tray()

    def _on_remove_desktop_shortcut(self):
        """删除桌面快捷方式"""
        ok = remove_desktop_shortcut()
        if ok:
            self.main_window.toast.show_toast("🗑️ 桌面快捷方式已删除", 3000)
        else:
            self.main_window.toast.show_toast("❌ 删除失败", 3000)
        # 刷新托盘菜单
        self._setup_tray()

    def _on_enable_autostart(self):
        """启用开机自启"""
        ok = enable_autostart()
        if ok:
            self.main_window.toast.show_toast("⚡ 开机自启已启用！", 3000)
        else:
            self.main_window.toast.show_toast("❌ 设置失败，请检查权限", 3000)
        # 刷新托盘菜单
        self._setup_tray()

    def _on_disable_autostart(self):
        """禁用开机自启"""
        ok = disable_autostart()
        if ok:
            self.main_window.toast.show_toast("🚫 开机自启已禁用", 3000)
        else:
            self.main_window.toast.show_toast("❌ 删除失败", 3000)
        # 刷新托盘菜单
        self._setup_tray()

    def run(self):
        self.dock.show()

        QTimer.singleShot(
            1000,
            lambda: self.main_window.toast.show_toast("✨ TidyUUUUp 已启动！", 5000)
        )

        sys.exit(self.app.exec_())


def main():
    app = TidyUUUUpApp()
    app.run()


if __name__ == "__main__":
    main()
