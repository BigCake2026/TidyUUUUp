"""TidyUUUUp v1.1.0 — Centered Island Edition.

This edition keeps the Dock deliberately quiet: four useful desktop groups and
search are centred within the island. Less-frequent commands live in menus.
All indexing is local; files are never moved, renamed, uploaded, or deleted
unless the user explicitly invokes a file action.
"""
from __future__ import annotations

import ctypes
import os
import platform
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt6.QtCore import QEvent, QPoint, QPropertyAnimation, QStandardPaths, QThread, QTimer, Qt, QEasingCurve, pyqtProperty, pyqtSignal
from PyQt6.QtGui import QColor, QCursor, QFont, QIcon, QPainter, QPainterPath, QPen, QPixmap
from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem, QMenu, QMessageBox, QSystemTrayIcon, QVBoxLayout, QWidget

from settings import UserSettings
from update_dialog import UpdateDialog
from updater import CURRENT_VERSION, UpdateChecker

try:
    from send2trash import send2trash
except Exception:
    send2trash = None

APP_NAME = "TidyUUUUp"
APP_DIR = Path(__file__).resolve().parent
ICON_PATH = APP_DIR / "assets" / "tidyuuuup_app_icon.ico"
SHORTCUT_SCRIPT = APP_DIR / "create_shortcut.ps1"


def is_windows() -> bool:
    return platform.system() == "Windows"


def get_desktop_path() -> str:
    """Resolve the user Desktop through Qt first, which supports OneDrive paths."""
    location = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DesktopLocation)
    if location and os.path.isdir(location):
        return location
    for candidate in (os.path.join(os.path.expanduser("~"), "Desktop"), os.path.join(os.path.expanduser("~"), "桌面")):
        if os.path.isdir(candidate):
            return candidate
    fallback = os.path.join(os.path.expanduser("~"), "Desktop")
    os.makedirs(fallback, exist_ok=True)
    return fallback


def open_path(path: str) -> None:
    """Open the selected item using its system-default handler."""
    try:
        if not os.path.exists(path):
            return
        if sys.platform.startswith("win"):
            os.startfile(path)  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])
    except Exception as error:
        print(f"[Open] {error}")


def reveal_path(path: str) -> None:
    """Reveal an item in the operating-system file manager."""
    try:
        if not os.path.exists(path):
            return
        if sys.platform.startswith("win"):
            subprocess.Popen(["explorer", "/select,", os.path.abspath(path)])
        elif sys.platform == "darwin":
            subprocess.Popen(["open", "-R", path])
        else:
            subprocess.Popen(["xdg-open", os.path.dirname(path)])
    except Exception as error:
        print(f"[Reveal] {error}")


class DesktopIndex:
    """Fast, local extension index.  It never changes a user's Desktop files."""

    EXTENSIONS = {
        "工作": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".md", ".odt", ".xls", ".xlsx", ".csv", ".ods", ".ppt", ".pptx", ".odp"},
        "图片": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".ico", ".tiff", ".heic", ".psd", ".ai", ".fig", ".sketch", ".xd"},
        "媒体": {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v", ".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"},
        "代码": {".py", ".js", ".ts", ".html", ".css", ".java", ".cpp", ".c", ".h", ".go", ".rs", ".json", ".xml", ".yaml", ".yml", ".exe", ".msi", ".bat", ".cmd", ".ps1", ".sh", ".apk"},
        "归档": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso"},
    }
    GROUPS = ("工作", "图片", "媒体", "代码")
    SKIP_NAMES = {"desktop.ini", "thumbs.db", ".ds_store"}

    def __init__(self, desktop_path: str):
        self.desktop_path = desktop_path
        self.files: list[dict] = []
        self._last_mtime = 0.0
        self.scan()

    def category_for(self, filename: str) -> str:
        extension = os.path.splitext(filename)[1].lower()
        for category, extensions in self.EXTENSIONS.items():
            if extension in extensions:
                return category
        return "其他"

    def directory_mtime(self) -> float:
        try:
            return os.stat(self.desktop_path).st_mtime
        except OSError:
            return 0.0

    def changed(self) -> bool:
        return self.directory_mtime() != self._last_mtime

    def scan(self) -> None:
        self.files = []
        self._last_mtime = self.directory_mtime()
        try:
            with os.scandir(self.desktop_path) as entries:
                for entry in entries:
                    if not entry.is_file() or entry.name.lower() in self.SKIP_NAMES or entry.name.startswith("."):
                        continue
                    try:
                        size = entry.stat().st_size
                    except OSError:
                        size = 0
                    self.files.append({"name": entry.name, "path": entry.path, "category": self.category_for(entry.name), "size": size})
        except OSError as error:
            print(f"[Scan] {error}")
        self.files.sort(key=lambda item: item["name"].lower())

    def group_files(self, group: str) -> list[dict]:
        return list(self.files) if group == "全部" else [item for item in self.files if item["category"] == group]

    def search(self, query: str, limit: int = 30) -> list[tuple[int, dict]]:
        query = query.strip().lower()
        if not query:
            return []
        matches: list[tuple[int, dict]] = []
        for item in self.files:
            name = item["name"].lower()
            if query in name:
                score = 100 - min(name.find(query) * 2, 30)
            elif any(query in part for part in re.split(r"[._\-\s]+", name)):
                score = 35
            else:
                score = 0
            if score:
                matches.append((score, item))
        return sorted(matches, key=lambda row: (-row[0], row[1]["name"].lower()))[:limit]


class DesktopScanWorker(QThread):
    scanned = pyqtSignal(list)

    def __init__(self, index: DesktopIndex, parent: QWidget | None = None):
        super().__init__(parent)
        self.index = index

    def run(self) -> None:
        self.index.scan()
        self.scanned.emit(list(self.index.files))


class BrandMark(QWidget):
    """Text-free logo mark that keeps the visual weight small and centred."""

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setFixedSize(30, 30)
        self.setToolTip(APP_NAME)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor("#0A84FF"))
        painter.drawRoundedRect(1, 1, 28, 28, 9, 9)
        painter.setBrush(QColor(255, 255, 255, 230))
        for x, height in ((7, 9), (12, 14), (17, 19)):
            painter.drawRoundedRect(x, 24 - height, 3, height, 1.5, 1.5)


class CategoryButton(QWidget):
    """A folder glyph; text is intentionally exposed only in its tooltip."""

    clicked = pyqtSignal(str)

    def __init__(self, group: str, accent: QColor, parent: QWidget | None = None):
        super().__init__(parent)
        self.group, self.accent, self.hovered = group, accent, False
        self.setFixedSize(34, 34)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setToolTip(f"查看{group}文件")

    def enterEvent(self, event) -> None:
        self.hovered = True
        self.update()

    def leaveEvent(self, event) -> None:
        self.hovered = False
        self.update()

    def mouseReleaseEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton and self.rect().contains(event.pos()):
            self.clicked.emit(self.group)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        if self.hovered:
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(QColor(255, 255, 255, 25))
            painter.drawRoundedRect(1, 1, 32, 32, 9, 9)
        tab = QPainterPath()
        tab.addRoundedRect(6, 7, 13, 8, 3, 3)
        painter.fillPath(tab, self.accent.darker(120))
        folder = QPainterPath()
        folder.addRoundedRect(4, 11, 26, 17, 5, 5)
        painter.fillPath(folder, self.accent)
        painter.setPen(QPen(QColor(255, 255, 255, 115 if self.hovered else 55), 1))
        painter.drawPath(folder)


class FilePopover(QWidget):
    """A single purpose file-list popup for categories and search results."""

    file_activated = pyqtSignal(str)

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent, Qt.WindowType.Tool | Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating, True)
        self.setFixedSize(380, 274)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 14, 16, 14)
        layout.setSpacing(6)
        self.title = QLabel(self)
        self.title.setFont(QFont("Segoe UI", 10, QFont.Weight.DemiBold))
        self.title.setStyleSheet("color: rgba(255,255,255,0.96);")
        self.meta = QLabel(self)
        self.meta.setFont(QFont("Segoe UI", 8))
        self.meta.setStyleSheet("color: rgba(255,255,255,0.52);")
        self.items = QListWidget(self)
        self.items.setStyleSheet("""
            QListWidget { background: transparent; border: none; color: rgba(255,255,255,0.88); font-family: 'Segoe UI'; font-size: 12px; outline: 0; }
            QListWidget::item { padding: 7px 8px; border-radius: 7px; }
            QListWidget::item:hover, QListWidget::item:selected { background: rgba(10,132,255,0.30); color: white; }
        """)
        self.items.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.items.itemDoubleClicked.connect(self.activate)
        self.items.customContextMenuRequested.connect(self.show_item_menu)
        layout.addWidget(self.title)
        layout.addWidget(self.meta)
        layout.addWidget(self.items)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        path = QPainterPath()
        path.addRoundedRect(0.5, 0.5, self.width() - 1, self.height() - 1, 18, 18)
        painter.fillPath(path, QColor(28, 29, 34, 242))
        painter.setPen(QPen(QColor(255, 255, 255, 36), 1))
        painter.drawPath(path)

    def show_files(self, title: str, files: list[dict], anchor: QPoint) -> None:
        self.title.setText(title)
        self.meta.setText("未找到文件" if not files else f"{len(files)} 个文件")
        self.items.clear()
        for entry in files:
            item = QListWidgetItem(entry["name"])
            item.setData(Qt.ItemDataRole.UserRole, entry["path"])
            item.setToolTip(entry["path"])
            self.items.addItem(item)
        self.place(anchor)
        self.show()
        self.raise_()

    def place(self, anchor: QPoint) -> None:
        screen = QApplication.screenAt(anchor) or QApplication.primaryScreen()
        area = screen.availableGeometry()
        x = max(area.left() + 12, min(anchor.x() - self.width() // 2, area.right() - self.width() - 12))
        y = anchor.y() - self.height() - 14
        if y < area.top() + 12:
            y = min(anchor.y() + 14, area.bottom() - self.height() - 12)
        self.move(x, y)

    def activate(self, item: QListWidgetItem) -> None:
        path = item.data(Qt.ItemDataRole.UserRole)
        if path:
            self.file_activated.emit(path)

    def show_item_menu(self, position: QPoint) -> None:
        item = self.items.itemAt(position)
        if not item:
            return
        path = item.data(Qt.ItemDataRole.UserRole)
        if not path:
            return
        menu = QMenu(self)
        open_action = menu.addAction("打开")
        reveal_action = menu.addAction("在文件夹中显示")
        copy_action = menu.addAction("复制路径")
        trash_action = None
        if send2trash is not None:
            menu.addSeparator()
            trash_action = menu.addAction("移到回收站")
        selected = menu.exec(self.items.mapToGlobal(position))
        if selected == open_action:
            open_path(path)
        elif selected == reveal_action:
            reveal_path(path)
        elif selected == copy_action:
            QApplication.clipboard().setText(path)
        elif trash_action is not None and selected == trash_action:
            try:
                send2trash(path)
            except Exception as error:
                QMessageBox.warning(self, "操作失败", str(error))


class TidyDynamicIslandDock(QWidget):
    """The centered compact island and all user-facing desktop operations."""

    def __init__(self, settings: UserSettings):
        super().__init__()
        self.settings = settings
        custom = settings.get("desktop_path") or ""
        self.desktop_path = custom if os.path.isdir(custom) else get_desktop_path()
        self.index = DesktopIndex(self.desktop_path)
        self.compact_width, self.stretched_width, self.current_width, self.height_size = 470, 640, 470, 64
        self.drag_offset: QPoint | None = None
        self.scan_worker: DesktopScanWorker | None = None
        self.update_checker: UpdateChecker | None = None
        self.manual_update_check = False
        self.search_query = ""
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedHeight(self.height_size)
        self.setFixedWidth(self.compact_width)
        self.setup_ui()
        self.restore_position()
        self.enable_acrylic()
        self.width_animation = QPropertyAnimation(self, b"dockWidth", self)
        self.width_animation.setDuration(300)
        self.width_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.search_width_animation = QPropertyAnimation(self.search_input, b"maximumWidth", self)
        self.search_width_animation.setDuration(240)
        self.search_width_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.search_timer = QTimer(self)
        self.search_timer.setSingleShot(True)
        self.search_timer.setInterval(180)
        self.search_timer.timeout.connect(self.run_search)
        self.rescan_timer = QTimer(self)
        self.rescan_timer.timeout.connect(self.rescan_if_changed)
        self.rescan_timer.start(10000)

    def setup_ui(self) -> None:
        outer = QHBoxLayout(self)
        outer.setContentsMargins(14, 0, 14, 0)
        outer.setSpacing(0)
        outer.addStretch(1)
        content = QWidget(self)
        layout = QHBoxLayout(content)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)
        layout.addWidget(BrandMark(content))
        colors = {"工作": QColor("#3B82F6"), "图片": QColor("#8B5CF6"), "媒体": QColor("#EC4899"), "代码": QColor("#14B8A6")}
        for group in DesktopIndex.GROUPS:
            button = CategoryButton(group, colors[group], content)
            button.clicked.connect(self.open_group)
            layout.addWidget(button)
        divider = QFrame(content)
        divider.setFrameShape(QFrame.Shape.VLine)
        divider.setStyleSheet("color: rgba(255,255,255,0.14); margin: 14px 2px;")
        layout.addWidget(divider)
        self.search_input = QLineEdit(content)
        self.search_input.setPlaceholderText("搜索桌面")
        self.search_input.setMinimumWidth(116)
        self.search_input.setMaximumWidth(116)
        self.search_input.setFixedHeight(32)
        self.search_input.setStyleSheet("""
            QLineEdit { background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.13); border-radius: 15px; padding: 0 12px; color: white; font-family: 'Segoe UI'; font-size: 11px; }
            QLineEdit:focus { background: rgba(255,255,255,0.13); border: 1px solid rgba(10,132,255,0.80); }
        """)
        self.search_input.installEventFilter(self)
        self.search_input.textChanged.connect(self.on_search_changed)
        layout.addWidget(self.search_input)
        outer.addWidget(content, 0, Qt.AlignmentFlag.AlignCenter)
        outer.addStretch(1)
        self.popover = FilePopover(self)
        self.popover.file_activated.connect(open_path)

    def get_dock_width(self) -> int:
        return self.current_width

    def set_dock_width(self, width: int) -> None:
        self.current_width = int(width)
        self.setFixedWidth(self.current_width)
        if not self.settings.get("dock_position"):
            self.center_bottom_position()
        self.update()

    dockWidth = pyqtProperty(int, get_dock_width, set_dock_width)

    def center_bottom_position(self) -> None:
        area = QApplication.primaryScreen().availableGeometry()
        self.move(area.left() + (area.width() - self.current_width) // 2, area.bottom() - self.height_size - 18)

    def restore_position(self) -> None:
        position = self.settings.get("dock_position")
        if isinstance(position, list) and len(position) == 2:
            self.move(int(position[0]), int(position[1]))
        else:
            self.center_bottom_position()

    def reset_position(self) -> None:
        self.settings.set("dock_position", None)
        self.center_bottom_position()

    def animate_width(self, target: int) -> None:
        if target == self.current_width:
            return
        self.width_animation.stop()
        self.width_animation.setStartValue(self.current_width)
        self.width_animation.setEndValue(target)
        self.width_animation.start()

    def animate_search_width(self, target: int) -> None:
        current = self.search_input.maximumWidth()
        if target == current:
            return
        self.search_width_animation.stop()
        self.search_width_animation.setStartValue(current)
        self.search_width_animation.setEndValue(target)
        self.search_width_animation.start()

    def expand_search(self) -> None:
        self.animate_search_width(270)
        self.animate_width(self.stretched_width)

    def collapse_search(self) -> None:
        if self.search_input.text().strip():
            return
        self.animate_search_width(116)
        self.animate_width(self.compact_width)

    def eventFilter(self, watched, event) -> bool:
        if watched is self.search_input:
            if event.type() == QEvent.Type.FocusIn:
                self.expand_search()
            elif event.type() == QEvent.Type.KeyPress and event.key() == Qt.Key.Key_Escape:
                self.search_input.clear()
                self.search_input.clearFocus()
                self.popover.hide()
                self.collapse_search()
                return True
        return super().eventFilter(watched, event)

    def on_search_changed(self, text: str) -> None:
        self.search_query = text.strip()
        if not self.search_query:
            self.search_timer.stop()
            self.popover.hide()
            return
        self.search_timer.start()

    def run_search(self) -> None:
        if not self.search_query:
            return
        results = self.index.search(self.search_query)
        anchor = self.mapToGlobal(self.search_input.geometry().center())
        self.popover.show_files(f"搜索：{self.search_query}", [item for _, item in results], anchor)

    def open_group(self, group: str) -> None:
        sender = self.sender()
        anchor = self.mapToGlobal(sender.geometry().center()) if isinstance(sender, QWidget) else QCursor.pos()
        self.popover.show_files(group, self.index.group_files(group), anchor)

    def show_all(self) -> None:
        self.popover.show_files("全部文件", self.index.group_files("全部"), QCursor.pos())

    def rescan_if_changed(self) -> None:
        if self.index.changed():
            self.rescan()

    def rescan(self) -> None:
        if self.scan_worker is not None and self.scan_worker.isRunning():
            return
        self.scan_worker = DesktopScanWorker(self.index, self)
        self.scan_worker.scanned.connect(self.on_scan_complete)
        self.scan_worker.start()

    def on_scan_complete(self, files: list) -> None:
        if self.search_input.text().strip():
            self.run_search()

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.RightButton:
            self.show_context_menu(event.globalPosition().toPoint())
            return
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_offset = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            self.search_input.clearFocus()
            self.popover.hide()
            self.collapse_search()

    def mouseMoveEvent(self, event) -> None:
        if self.drag_offset is not None and event.buttons() & Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_offset)

    def mouseReleaseEvent(self, event) -> None:
        if self.drag_offset is not None:
            self.settings.set("dock_position", [self.x(), self.y()])
        self.drag_offset = None

    def show_context_menu(self, position: QPoint) -> None:
        menu = QMenu(self)
        all_files = menu.addAction("全部桌面文件")
        rescan = menu.addAction("重新扫描")
        reset = menu.addAction("恢复居中")
        menu.addSeparator()
        update = menu.addAction("检查更新")
        about = menu.addAction("关于")
        menu.addSeparator()
        quit_action = menu.addAction("退出")
        selected = menu.exec(position)
        if selected == all_files:
            self.show_all()
        elif selected == rescan:
            self.rescan()
        elif selected == reset:
            self.reset_position()
        elif selected == update:
            self.check_for_updates(force=True)
        elif selected == about:
            QMessageBox.about(self, "关于 TidyUUUUp", f"TidyUUUUp v{CURRENT_VERSION}\n\n本地索引桌面文件：{len(self.index.files)} 个\n数据目录：{self.settings.path}")
        elif selected == quit_action:
            QApplication.quit()

    def enable_acrylic(self) -> None:
        if not is_windows():
            return
        try:
            class AccentPolicy(ctypes.Structure):
                _fields_ = [("AccentState", ctypes.c_uint), ("AccentFlags", ctypes.c_uint), ("GradientColor", ctypes.c_uint), ("AnimationId", ctypes.c_uint)]
            class CompositionAttribute(ctypes.Structure):
                _fields_ = [("Attribute", ctypes.c_uint), ("Data", ctypes.c_void_p), ("SizeOfData", ctypes.c_size_t)]
            accent = AccentPolicy(4, 0, 0xD81C1D22, 0)
            data = CompositionAttribute(19, ctypes.cast(ctypes.pointer(accent), ctypes.c_void_p), ctypes.sizeof(accent))
            ctypes.windll.user32.SetWindowCompositionAttribute(int(self.winId()), ctypes.byref(data))
        except Exception as error:
            print(f"[Acrylic] {error}")

    def create_shortcut_if_needed(self) -> None:
        """Create or refresh the branded desktop link when a packaged EXE starts."""
        if not is_windows() or not getattr(sys, "frozen", False) or not SHORTCUT_SCRIPT.is_file():
            return
        executable = os.path.abspath(sys.executable)
        if self.settings.get("shortcut_target") == executable:
            return
        shortcut = os.path.join(get_desktop_path(), f"{APP_NAME}.lnk")
        try:
            result = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(SHORTCUT_SCRIPT), "-TargetPath", executable, "-ShortcutPath", shortcut, "-IconPath", executable], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=12, check=False)
            if result.returncode == 0 and os.path.isfile(shortcut):
                self.settings.set("shortcut_target", executable)
        except Exception as error:
            print(f"[Shortcut] {error}")

    def check_for_updates(self, force: bool = False) -> None:
        if self.update_checker is not None and self.update_checker.isRunning():
            return
        if not force and not self.settings.should_auto_check():
            return
        self.manual_update_check = force
        self.update_checker = UpdateChecker(self.settings.get("update_repo", "BigCake2026/TidyUUUUp"), CURRENT_VERSION, self)
        self.update_checker.check_finished.connect(lambda available, info: self.on_update_checked(available, info, force))
        self.update_checker.check_error.connect(self.on_update_error)
        self.update_checker.start()

    def on_update_checked(self, available: bool, info: dict, force: bool) -> None:
        self.settings.mark_checked()
        if not available:
            if force:
                QMessageBox.information(self, "检查更新", f"当前已是最新版本 v{CURRENT_VERSION}。")
            return
        version = info.get("latest_version", "")
        if not force and self.settings.is_skipped(version):
            return
        dialog = UpdateDialog(info, self.settings, self)
        dialog.show_centered()

    def on_update_error(self, message: str) -> None:
        if self.manual_update_check:
            QMessageBox.warning(self, "检查更新", f"检查更新失败：{message}")
        self.manual_update_check = False

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        body = QPainterPath()
        body.addRoundedRect(0.5, 0.5, self.width() - 1, self.height() - 1, 24, 24)
        painter.fillPath(body, QColor(26, 27, 31, 226))
        painter.setPen(QPen(QColor(255, 255, 255, 37), 1))
        painter.drawPath(body)


def application_icon() -> QIcon:
    icon = QIcon(str(ICON_PATH)) if ICON_PATH.is_file() else QIcon()
    if not icon.isNull():
        return icon
    pixmap = QPixmap(64, 64)
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.setPen(Qt.PenStyle.NoPen)
    painter.setBrush(QColor("#0A84FF"))
    painter.drawRoundedRect(6, 6, 52, 52, 16, 16)
    painter.end()
    return QIcon(pixmap)


def install_tray(dock: TidyDynamicIslandDock) -> QSystemTrayIcon | None:
    try:
        tray = QSystemTrayIcon(application_icon(), dock)
        tray.setToolTip(f"{APP_NAME} v{CURRENT_VERSION}")
        menu = QMenu()
        show = menu.addAction("显示小岛")
        all_files = menu.addAction("全部桌面文件")
        rescan = menu.addAction("重新扫描")
        menu.addSeparator()
        update = menu.addAction("检查更新")
        quit_action = menu.addAction("退出")
        show.triggered.connect(dock.show)
        all_files.triggered.connect(dock.show_all)
        rescan.triggered.connect(dock.rescan)
        update.triggered.connect(lambda: dock.check_for_updates(force=True))
        quit_action.triggered.connect(QApplication.quit)
        tray.setContextMenu(menu)
        tray.show()
        return tray
    except Exception as error:
        print(f"[Tray] {error}")
        return None


def main() -> int:
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setApplicationName(APP_NAME)
    app.setOrganizationName(APP_NAME)
    app.setWindowIcon(application_icon())
    settings = UserSettings()
    dock = TidyDynamicIslandDock(settings)
    dock.show()
    tray = install_tray(dock)
    QTimer.singleShot(650, dock.create_shortcut_if_needed)
    QTimer.singleShot(2200, dock.check_for_updates)
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
