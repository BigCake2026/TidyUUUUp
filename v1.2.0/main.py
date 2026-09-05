"""TidyUUUUp v1.2.0 — Liquid Glass Edition.
All v1.1.2 features preserved. UI re-skinned with Apple-style Liquid Glass:
translucent acrylic, specular top highlights, refractive edge borders.
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

from PyQt6.QtCore import QDate, QEvent, QPoint, QPropertyAnimation, QRectF, QStandardPaths, QThread, QTime, QTimer, Qt, QEasingCurve, pyqtProperty, pyqtSignal
from PyQt6.QtGui import QColor, QCursor, QFont, QIcon, QLinearGradient, QPainter, QPainterPath, QPen, QPixmap, QBrush
from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem, QMenu, QMessageBox, QPushButton, QSystemTrayIcon, QVBoxLayout, QWidget

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


class StackedLogoWidget(QWidget):
    """Classic two-line wordmark from the original island composition."""

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setFixedSize(64, 46)
        self.setToolTip(APP_NAME)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setFont(QFont("Segoe UI", 11, QFont.Weight.DemiBold))
        painter.setPen(QColor(255, 255, 255, 228))
        painter.drawText(self.rect().adjusted(0, 2, 0, -20), Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter, "Tidy")
        painter.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        painter.setPen(QColor(10, 132, 255, 245))
        painter.drawText(self.rect().adjusted(0, 19, 0, -3), Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter, "UUUUp")


class AppleVectorFolderIcon(QWidget):
    """Classic blue folder glyph connected to a real Desktop category."""

    clicked = pyqtSignal(str)

    def __init__(self, group: str, tooltip: str, parent: QWidget | None = None):
        super().__init__(parent)
        self.group, self.hovered = group, False
        self.setFixedSize(36, 36)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setToolTip(tooltip)

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
            hover_path = QPainterPath()
            hover_path.addRoundedRect(0, 0, 36, 36, 11, 11)
            painter.fillPath(hover_path, QColor(255, 255, 255, 30))
        # Glass folder body with depth
        body = QPainterPath()
        body.addRoundedRect(4, 11, 28, 19, 6, 6)
        grad = QLinearGradient(0, 11, 0, 30)
        grad.setColorAt(0.0, QColor(64, 168, 255, 235))
        grad.setColorAt(0.5, QColor(20, 132, 255, 240))
        grad.setColorAt(1.0, QColor(0, 110, 230, 245))
        painter.fillPath(body, QBrush(grad))
        # Folder tab
        tab = QPainterPath()
        tab.addRoundedRect(5, 6, 13, 8, 3, 3)
        painter.fillPath(tab, QColor(30, 140, 255, 240))
        # Glass top highlight
        top_highlight = QLinearGradient(0, 11, 0, 19)
        top_highlight.setColorAt(0.0, QColor(255, 255, 255, 70))
        top_highlight.setColorAt(1.0, QColor(255, 255, 255, 0))
        painter.fillPath(body, QBrush(top_highlight))
        # Refractive edge
        painter.setPen(QPen(QColor(255, 255, 255, 90 if self.hovered else 55), 1.1))
        painter.drawPath(body)


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
        self.title.setStyleSheet("color: rgba(255,255,255,0.95);")
        self.meta = QLabel(self)
        self.meta.setFont(QFont("Segoe UI", 8))
        self.meta.setStyleSheet("color: rgba(255,255,255,0.48);")
        self.items = QListWidget(self)
        self.items.setStyleSheet("""
            QListWidget { background: transparent; border: none; color: rgba(255,255,255,0.90); font-family: 'Segoe UI'; font-size: 12px; outline: 0; }
            QListWidget::item { padding: 8px 10px; border-radius: 8px; }
            QListWidget::item:hover, QListWidget::item:selected { background: rgba(10,132,255,0.35); color: white; }
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
        rect = QRectF(self.rect().adjusted(1, 1, -1, -1))
        path = QPainterPath()
        path.addRoundedRect(rect, 20, 20)
        # Liquid Glass base: vertical gradient (top brighter)
        grad = QLinearGradient(0, 0, 0, self.height())
        grad.setColorAt(0.0, QColor(50, 54, 66, 168))
        grad.setColorAt(0.5, QColor(34, 37, 46, 158))
        grad.setColorAt(1.0, QColor(26, 28, 36, 168))
        painter.fillPath(path, QBrush(grad))
        # Top specular highlight
        highlight = QLinearGradient(0, 2, 0, 22)
        highlight.setColorAt(0.0, QColor(255, 255, 255, 55))
        highlight.setColorAt(1.0, QColor(255, 255, 255, 0))
        painter.fillPath(path, QBrush(highlight))
        # Refractive edge border
        painter.setPen(QPen(QColor(255, 255, 255, 58), 1.2))
        painter.drawPath(path)
        # Inner subtle border
        inner = QPainterPath()
        inner.addRoundedRect(QRectF(rect.adjusted(2, 2, -2, -2)), 18, 18)
        painter.setPen(QPen(QColor(255, 255, 255, 18), 0.8))
        painter.drawPath(inner)

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
        self.compact_width, self.stretched_width, self.current_width, self.height_size = 620, 800, 620, 58
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
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.update_clock)
        self.clock_timer.start(1000)
        self.update_clock()

    def setup_ui(self) -> None:
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(16, 0, 16, 0)
        self.main_layout.setSpacing(8)
        self.logo = StackedLogoWidget(self)
        self.main_layout.addWidget(self.logo)

        pinned_container = QWidget(self)
        pinned_layout = QHBoxLayout(pinned_container)
        pinned_layout.setContentsMargins(0, 0, 0, 0)
        pinned_layout.setSpacing(8)
        all_files_button = self.create_pinned_button("▣", "全部桌面文件")
        all_files_button.clicked.connect(self.show_all)
        rescan_button = self.create_pinned_button("↻", "重新扫描桌面")
        rescan_button.clicked.connect(self.rescan)
        pinned_layout.addWidget(all_files_button)
        pinned_layout.addWidget(rescan_button)
        self.main_layout.addWidget(pinned_container)
        self.main_layout.addWidget(self.create_divider())

        folders_container = QWidget(self)
        folders_layout = QHBoxLayout(folders_container)
        folders_layout.setContentsMargins(0, 0, 0, 0)
        folders_layout.setSpacing(8)
        for group, tooltip in (("工作", "工作文件"), ("图片", "图片与设计文件"), ("代码", "代码与安装文件")):
            folder = AppleVectorFolderIcon(group, tooltip, self)
            folder.clicked.connect(self.open_group)
            folders_layout.addWidget(folder)
        self.main_layout.addWidget(folders_container)

        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Search content...")
        self.search_input.setMinimumWidth(174)
        self.search_input.setMaximumWidth(174)
        self.search_input.setFixedHeight(32)
        self.search_input.setStyleSheet("""
            QLineEdit { background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.18); border-radius: 15px; padding: 0 14px; color: rgba(255,255,255,0.92); font-family: 'Segoe UI'; font-size: 11px; }
            QLineEdit:focus { background: rgba(255,255,255,0.12); border: 1px solid rgba(10,132,255,0.7); }
            QLineEdit::placeholder { color: rgba(255,255,255,0.38); }
        """)
        self.search_input.installEventFilter(self)
        self.search_input.textChanged.connect(self.on_search_changed)
        self.main_layout.addWidget(self.search_input)
        self.main_layout.addWidget(self.create_divider())

        self.clock_widget = QWidget(self)
        clock_layout = QVBoxLayout(self.clock_widget)
        clock_layout.setContentsMargins(0, 10, 0, 10)
        clock_layout.setSpacing(0)
        self.time_label = QLabel(self)
        self.time_label.setFont(QFont("Segoe UI", 9, QFont.Weight.Bold))
        self.time_label.setStyleSheet("color: rgba(255,255,255,0.94);")
        self.date_label = QLabel(self)
        self.date_label.setFont(QFont("Segoe UI", 7))
        self.date_label.setStyleSheet("color: rgba(255,255,255,0.60);")
        clock_layout.addWidget(self.time_label, 0, Qt.AlignmentFlag.AlignRight)
        clock_layout.addWidget(self.date_label, 0, Qt.AlignmentFlag.AlignRight)
        self.main_layout.addWidget(self.clock_widget)

        self.popover = FilePopover(self)
        self.popover.file_activated.connect(open_path)

    def create_divider(self) -> QFrame:
        divider = QFrame(self)
        divider.setFrameShape(QFrame.Shape.VLine)
        divider.setStyleSheet("color: rgba(255,255,255,0.12); margin-top: 13px; margin-bottom: 13px;")
        return divider

    def create_pinned_button(self, label: str, tooltip: str) -> QPushButton:
        button = QPushButton(label, self)
        button.setFixedSize(32, 32)
        button.setToolTip(tooltip)
        button.setStyleSheet("""
            QPushButton { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.14); border-radius: 9px; color: rgba(255,255,255,0.88); font-size: 14px; font-family: 'Segoe UI Symbol'; }
            QPushButton:hover { background: rgba(255,255,255,0.16); border-color: rgba(255,255,255,0.28); color: white; }
        """)
        return button

    def update_clock(self) -> None:
        self.time_label.setText(QTime.currentTime().toString("hh:mm AP"))
        self.date_label.setText(QDate.currentDate().toString("MM/dd ddd"))

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
        self.move(area.left() + (area.width() - self.current_width) // 2, area.bottom() - self.height_size - 24)

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
        self.animate_search_width(360)
        self.animate_width(self.stretched_width)

    def collapse_search(self) -> None:
        if self.search_input.text().strip():
            return
        self.animate_search_width(174)
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
        self.popover.show_files(f"Search · {self.search_query}", [item for _, item in results], anchor)

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
            accent = AccentPolicy(4, 0, 0x771E2230, 0)  # Liquid Glass: alpha=119, blue-grey tint
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
        # 更新检查为产品必备能力：每次启动均检查 GitHub Release。
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
        dialog = UpdateDialog(info, self.settings, self)
        dialog.show_centered()

    def on_update_error(self, message: str) -> None:
        if self.manual_update_check:
            QMessageBox.warning(self, "检查更新", f"检查更新失败：{message}")
        self.manual_update_check = False

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        rect = QRectF(self.rect().adjusted(1, 1, -1, -1))
        body = QPainterPath()
        body.addRoundedRect(rect, 26, 26)
        # Liquid Glass base: vertical gradient with depth
        grad = QLinearGradient(0, 0, 0, self.height())
        grad.setColorAt(0.0, QColor(52, 56, 68, 148))
        grad.setColorAt(0.4, QColor(36, 40, 50, 138))
        grad.setColorAt(1.0, QColor(26, 28, 36, 152))
        painter.fillPath(body, QBrush(grad))
        # Top specular highlight (glass reflection)
        highlight = QLinearGradient(0, 2, 0, self.height() * 0.45)
        highlight.setColorAt(0.0, QColor(255, 255, 255, 62))
        highlight.setColorAt(0.5, QColor(255, 255, 255, 18))
        highlight.setColorAt(1.0, QColor(255, 255, 255, 0))
        painter.fillPath(body, QBrush(highlight))
        # Bottom inner shadow (depth)
        shadow = QLinearGradient(0, self.height() * 0.6, 0, self.height())
        shadow.setColorAt(0.0, QColor(0, 0, 0, 0))
        shadow.setColorAt(1.0, QColor(0, 0, 0, 35))
        painter.fillPath(body, QBrush(shadow))
        # Refractive edge border (outer)
        painter.setPen(QPen(QColor(255, 255, 255, 55), 1.2))
        painter.drawPath(body)
        # Inner subtle border
        inner = QPainterPath()
        inner.addRoundedRect(QRectF(rect.adjusted(2.5, 2.5, -2.5, -2.5)), 23, 23)
        painter.setPen(QPen(QColor(255, 255, 255, 16), 0.8))
        painter.drawPath(inner)


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
