"""
TidyUUUUp v1.0.11 - Dynamic Island Dock (Functional Edition)
灵动岛风格桌面整理 Dock，基于 PyQt6

本版本相对原始展示版的核心改进（让 UI 真正可用）：
  1. 真正扫描物理桌面文件（QStandardPaths），而非全部 mock 数据；
     在 Windows 上自动识别桌面路径，其它平台回退到用户主目录下的
     `Desktop`（无则创建空目录）。
  2. 文件夹 Popover 展示真实桌面文件（按扩展名/关键词分类），
     双击可直接在文件管理器中打开该文件（跨平台）。
  3. 搜索框基于真实文件名做模糊匹配 + 相似度评分，实时显示结果。
  4. 固定应用按钮真正可用（系统默认浏览器 / 默认终端打开）。
  5. 修正聚焦逻辑：使用 FocusIn 事件触发弹簧拉伸，按 Esc / 点击空白
     收起，避免原来 selectionChanged 误触发的问题。
  6. 跨平台安全：Windows Acrylic API 优雅降级；非 Windows 平台用
     QPainter 绘制半透明深色玻璃底板（功能不受影响）。
  7. 提供 tray icon + 右键菜单（退出 / 重新扫描 / 关于），
     无边框窗口可拖动，修复"无法移动窗口"的可用性问题。
  8. 健壮性：clipboard 用安全降级、subprocess 用 Popen 避免阻塞、
     全部异常捕获不使 UI 崩溃。
"""
import os
import sys
import re
import subprocess
import ctypes
import platform
from functools import partial
from PyQt6.QtCore import (Qt, QTimer, QTime, QDate, QPropertyAnimation,
                          QEasingCurve, QRect, QSize, pyqtSignal, pyqtProperty,
                          QPoint, QStandardPaths, QEvent)
from PyQt6.QtGui import (QPainter, QColor, QFont, QPen, QBrush,
                         QPainterPath, QLinearGradient, QAction, QIcon, QCursor,
                         QGuiApplication, QKeyEvent)
from PyQt6.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
                             QLabel, QLineEdit, QPushButton, QFrame,
                             QGraphicsDropShadowEffect, QListWidget,
                             QListWidgetItem, QMenu, QSystemTrayIcon,
                             QMessageBox)

try:
    from send2trash import send2trash  # 可选依赖：移到回收站
except Exception:  # pragma: no cover
    send2trash = None


# ==========================================
# 平台 / 桌面路径工具
# ==========================================
def is_windows() -> bool:
    return platform.system() == "Windows"


def get_desktop_path() -> str:
    """返回当前用户的桌面目录，跨平台安全。"""
    # Windows: 通常 %USERPROFILE%\Desktop
    if is_windows():
        # 优先用 SHGetKnownFolderPath 获取真实的桌面路径（含 OneDrive 重定向）
        try:
            import ctypes.wintypes as wt
            FOLDERID_Desktop = ctypes.c_char * 16
            # GUID for Desktop: B4BFCC3A-DB2C-424C-B029-7FE99A87C641
            guid = (wt.BYTE * 16)(
                0xB4, 0xBF, 0xCC, 0x3A, 0xDB, 0x2C, 0x42, 0x4C,
                0xB0, 0x29, 0x7F, 0xE9, 0x9A, 0x87, 0xC6, 0x41)
            buf = ctypes.c_wchar_p()
            if ctypes.windll.shell32.SHGetKnownFolderPath(
                    ctypes.byref(guid), 0, None, ctypes.byref(buf)) == 0:
                return buf.value
        except Exception:
            pass
        return os.path.join(os.path.expanduser("~"), "Desktop")

    # Linux / macOS: 各桌面环境的桌面目录
    home = os.path.expanduser("~")
    candidates = [
        os.path.join(home, "Desktop"),
        os.path.join(home, "桌面"),
    ]
    for c in candidates:
        if os.path.isdir(c):
            return c
    # XDG user-dirs
    try:
        cfg = os.path.join(home, ".config", "user-dirs.dirs")
        if os.path.isfile(cfg):
            with open(cfg, "r", encoding="utf-8") as f:
                for line in f:
                    if "XDG_DESKTOP_DIR" in line:
                        val = line.split("=", 1)[1].strip().strip('"')
                        if val.startswith("$HOME"):
                            val = os.path.join(home, val[5:])
                        if os.path.isdir(val):
                            return val
    except Exception:
        pass
    fallback = os.path.join(home, "Desktop")
    os.makedirs(fallback, exist_ok=True)
    return fallback


def open_in_file_manager(path: str) -> None:
    """在系统文件管理器中打开文件 / 文件夹，跨平台安全。"""
    try:
        path = os.path.abspath(path)
        if not os.path.exists(path):
            return
        if sys.platform.startswith("win"):
            if os.path.isdir(path):
                os.startfile(path)  # type: ignore[attr-defined]
            else:
                # 选中该文件
                subprocess.Popen(["explorer", "/select,", os.path.basename(path)],
                                 cwd=os.path.dirname(path))
        elif sys.platform == "darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])
    except Exception as e:
        print(f"[Open] {e}")


def open_default_app(app_kind: str) -> None:
    """打开默认浏览器 / 终端，跨平台。"""
    try:
        if app_kind == "Browser":
            url = "https://github.com/BigCake2026/TidyUUUUp"
            if sys.platform.startswith("win"):
                os.startfile(url)  # type: ignore[attr-defined]
            elif sys.platform == "darwin":
                subprocess.Popen(["open", url])
            else:
                subprocess.Popen(["xdg-open", url])
        elif app_kind == "Terminal":
            term = os.environ.get("TERMINAL", "")
            candidates = (["wt.exe"] if is_windows() else []) + \
                         (["open", "-a", "Terminal"] if sys.platform == "darwin" else []) + \
                         [term, "gnome-terminal", "konsole", "xterm"]
            for c in candidates:
                if not c:
                    continue
                try:
                    subprocess.Popen([c] if not c.startswith("open") else c.split())
                    return
                except FileNotFoundError:
                    continue
            QMessageBox.information(None, "Terminal", "未找到可用的终端程序。")
    except Exception as e:
        print(f"[OpenApp] {e}")


# ==========================================
# 桌面扫描与分类（轻量本地索引）
# ==========================================
class DesktopIndex:
    """扫描桌面文件并按本地规则分类（无需 AI / 联网）。"""

    # 扩展名 -> 类别（与 v1.0.10 file_index.py 对齐，精简常用项）
    EXT_CATEGORIES = {
        "图片": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".ico", ".tiff", ".heic"},
        "视频": {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v"},
        "音频": {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"},
        "文档": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".md", ".odt"},
        "表格": {".xls", ".xlsx", ".csv", ".ods"},
        "演示": {".ppt", ".pptx", ".odp"},
        "压缩包": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso"},
        "代码": {".py", ".js", ".ts", ".html", ".css", ".java", ".cpp", ".c", ".h", ".go", ".rs", ".json", ".xml", ".yaml", ".yml"},
        "可执行": {".exe", ".msi", ".bat", ".cmd", ".ps1", ".sh", ".apk"},
        "设计": {".psd", ".ai", ".fig", ".sketch", ".xd"},
        "字体": {".ttf", ".otf", ".woff", ".woff2"},
        "临时文件": {".tmp", ".temp", ".log", ".crdownload", ".part", ".bak", ".old"},
    }

    # Dock 上展示的虚拟目录名 -> 该目录所收纳的类别集合（语义映射）
    VIRTUAL_FOLDERS = {
        "Finance AI": ["表格", "文档"],
        "Design Spec": ["图片", "设计"],
        "Code Engine": ["代码", "可执行"],
        "Media": ["视频", "音频"],
        "Archives": ["压缩包"],
    }

    SKIP_NAMES = {"desktop.ini", "thumbs.db", ".ds_store"}

    def __init__(self, desktop_path: str):
        self.desktop_path = desktop_path
        self.files: list[dict] = []
        self.scan()

    def _category_for(self, name: str) -> str:
        ext = os.path.splitext(name)[1].lower()
        for cat, exts in self.EXT_CATEGORIES.items():
            if ext in exts:
                return cat
        return "其他"

    def scan(self) -> None:
        self.files = []
        try:
            with os.scandir(self.desktop_path) as it:
                for entry in it:
                    if not entry.is_file():
                        continue
                    if entry.name.lower() in self.SKIP_NAMES or entry.name.startswith("."):
                        continue
                    self.files.append({
                        "name": entry.name,
                        "path": entry.path,
                        "category": self._category_for(entry.name),
                        "size": entry.stat().st_size,
                    })
        except Exception as e:
            print(f"[Scan] {e}")

    def files_for_folder(self, folder_name: str) -> list[dict]:
        cats = self.VIRTUAL_FOLDERS.get(folder_name, [])
        if not cats:
            return self.files
        return [f for f in self.files if f["category"] in cats]

    def search(self, query: str, limit: int = 20) -> list[tuple[int, dict]]:
        """模糊匹配，返回 (相似度 0-100, file) 列表，按相似度降序。"""
        q = query.strip().lower()
        if not q:
            return []
        scored = []
        for f in self.files:
            name = f["name"].lower()
            if q in name:
                # 子串命中给高分，越靠前越高
                score = 90 - (name.find(q) * 2)
            else:
                # 词元重合度
                tokens = re.split(r"[._\-\s]+", name)
                hits = sum(1 for t in tokens if q in t)
                score = hits * 35 if hits else 0
            if score > 0:
                scored.append((max(score, 1), f))
        scored.sort(key=lambda x: x[0], reverse=True)
        return scored[:limit]


# ==========================================
# Windows Native Acrylic / DWM Blur Helper
# ==========================================
class ACCENT_POLICY(ctypes.Structure):
    _fields_ = [
        ('AccentState', ctypes.c_uint),
        ('AccentFlags', ctypes.c_uint),
        ('GradientColor', ctypes.c_uint),
        ('AnimationId', ctypes.c_uint)
    ]


class WINDOWCOMPOSITIONATTRIBDATA(ctypes.Structure):
    _fields_ = [
        ('Attribute', ctypes.c_uint),
        ('Data', ctypes.c_void_p),
        ('SizeOfData', ctypes.c_ulong)
    ]


def enable_windows_acrylic(hwnd: int, dark: bool = True):
    """开启 Windows 10/11 原生 API 的 Acrylic 深度毛玻璃效果（非 Windows 自动降级）。"""
    try:
        user32 = ctypes.windll.user32  # type: ignore[attr-defined]
        ACCENT_ENABLE_ACRYLICBLURBEHIND = 4
        bg_color = 0xCC1E1E20 if dark else 0xCCF5F5F7

        accent = ACCENT_POLICY()
        accent.AccentState = ACCENT_ENABLE_ACRYLICBLURBEHIND
        accent.GradientColor = bg_color

        data = WINDOWCOMPOSITIONATTRIBDATA()
        data.Attribute = 19  # WCA_ACCENT_POLICY
        data.Data = ctypes.cast(ctypes.pointer(accent), ctypes.c_void_p)
        data.SizeOfData = ctypes.sizeof(accent)

        user32.SetWindowCompositionAttribute(hwnd, ctypes.byref(data))
    except Exception as e:
        # 非 Windows 或 API 不可用，静默降级到 QPainter 玻璃底板
        print("Acrylic API Notice:", e)


# ==========================================
# 1. 品牌 Stacked Logo (Tidy / UUUUp)
# ==========================================
class StackedLogoWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(64)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setFont(QFont("Segoe UI", 9, QFont.Weight.DemiBold))
        painter.setPen(QColor(255, 255, 255, 210))
        painter.drawText(QRect(0, 8, 64, 16), Qt.AlignmentFlag.AlignLeft, "Tidy")
        painter.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        painter.setPen(QColor(10, 132, 255, 240))  # Apple Accent Blue
        painter.drawText(QRect(0, 22, 64, 18), Qt.AlignmentFlag.AlignLeft, "UUUUp")


# ==========================================
# 2. Apple 原生矢量蓝文件夹图标 (No Emoji)
# ==========================================
class AppleVectorFolderIcon(QWidget):
    clicked = pyqtSignal(str)

    def __init__(self, folder_name="Documents", parent=None):
        super().__init__(parent)
        self.folder_name = folder_name
        self.setFixedSize(36, 36)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self._hover = False

    def enterEvent(self, event):
        self._hover = True
        self.update()

    def leaveEvent(self, event):
        self._hover = False
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(self.folder_name)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # 文件夹后背板 (Back tab)
        tab_path = QPainterPath()
        tab_path.addRoundedRect(4, 6, 14, 8, 3, 3)
        painter.fillPath(tab_path, QColor(0, 102, 204))

        # 文件夹主体 (Front cover)
        body_path = QPainterPath()
        body_path.addRoundedRect(3, 10, 30, 20, 5, 5)
        gradient = QLinearGradient(0, 10, 0, 30)
        gradient.setColorAt(0.0, QColor(51, 153, 255))
        gradient.setColorAt(1.0, QColor(0, 122, 255))
        painter.fillPath(body_path, QBrush(gradient))

        # hover 高光
        if self._hover:
            painter.setPen(QPen(QColor(255, 255, 255, 140), 1.4))
        else:
            painter.setPen(QPen(QColor(255, 255, 255, 70), 1))
        painter.drawPath(body_path)


# ==========================================
# 3. 顶部 Popover 悬浮毛玻璃面板
# ==========================================
class TopPopoverPanel(QWidget):
    file_activated = pyqtSignal(str)  # 双击/回车打开文件

    def __init__(self, parent=None):
        super().__init__(parent, Qt.WindowType.ToolTip | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(360, 240)
        self.setWindowFlag(Qt.WindowType.WindowDoesNotAcceptFocus, False)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(8)

        self.title_label = QLabel("AI Virtual Directory", self)
        self.title_label.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        self.title_label.setStyleSheet("color: #FFFFFF;")
        layout.addWidget(self.title_label)

        self.subtitle_label = QLabel("", self)
        self.subtitle_label.setFont(QFont("Segoe UI", 8))
        self.subtitle_label.setStyleSheet("color: rgba(255,255,255,0.55);")
        layout.addWidget(self.subtitle_label)

        self.list_widget = QListWidget(self)
        self.list_widget.setStyleSheet("""
            QListWidget {
                background: transparent;
                border: none;
                color: #E0E0E0;
                font-family: 'Segoe UI';
                font-size: 12px;
            }
            QListWidget::item {
                padding: 6px;
                border-radius: 6px;
            }
            QListWidget::item:hover {
                background: rgba(255, 255, 255, 0.12);
                color: #FFFFFF;
            }
            QListWidget::item:selected {
                background: rgba(10, 132, 255, 0.35);
                color: #FFFFFF;
            }
        """)
        self.list_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.list_widget.itemDoubleClicked.connect(self._on_item_activated)
        self.list_widget.customContextMenuRequested.connect(self._on_context_menu)
        layout.addWidget(self.list_widget)

        self.footer_label = QLabel("双击打开 · 右键在文件夹中显示", self)
        self.footer_label.setFont(QFont("Segoe UI", 7))
        self.footer_label.setStyleSheet("color: rgba(255,255,255,0.4);")
        layout.addWidget(self.footer_label)

        self._paths: dict[str, str] = {}  # item_text -> real path

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), 18, 18)
        painter.fillPath(path, QColor(30, 30, 32, 235))
        painter.setPen(QPen(QColor(255, 255, 255, 30), 1.2))
        painter.drawPath(path)

    # ---- 真实数据展示 ----
    def show_folder_content(self, folder_name, global_pos, files=None):
        self.title_label.setText(f"📁 {folder_name}")
        self.list_widget.clear()
        self._paths.clear()

        if files is None:
            files = []

        if not files:
            self.subtitle_label.setText("（该分类下暂无桌面文件）")
            self.list_widget.addItem(QListWidgetItem("— 空目录 —"))
        else:
            self.subtitle_label.setText(f"{len(files)} 个文件 · 来自桌面")
            for f in files:
                size_kb = f.get("size", 0) / 1024
                size_str = f"{size_kb:.0f} KB" if size_kb < 1024 else f"{size_kb/1024:.1f} MB"
                label = f"{f['name']}  ·  {f['category']}  ·  {size_str}"
                item = QListWidgetItem(label)
                self.list_widget.addItem(item)
                self._paths[label] = f["path"]

        self.move(max(0, global_pos.x() - 140), max(0, global_pos.y() - self.height() - 12))
        self.show()
        self.raise_()

    def show_search_results(self, query, global_pos, results=None):
        self.title_label.setText("🔍 语义搜索匹配")
        self.list_widget.clear()
        self._paths.clear()
        if not query:
            self.hide()
            return
        if results is None:
            results = []
        if not results:
            self.subtitle_label.setText(f"未找到匹配 “{query}” 的桌面文件")
            self.list_widget.addItem(QListWidgetItem("— 无匹配结果 —"))
        else:
            self.subtitle_label.setText(f"{len(results)} 项匹配 “{query}”")
            for score, f in results:
                label = f"Match {min(score, 99)}% · {f['name']}"
                item = QListWidgetItem(label)
                self.list_widget.addItem(item)
                self._paths[label] = f["path"]
        self.move(max(0, global_pos.x() - 100), max(0, global_pos.y() - self.height() - 12))
        self.show()
        self.raise_()

    def _on_item_activated(self, item):
        path = self._paths.get(item.text())
        if path:
            self.file_activated.emit(path)

    def _on_context_menu(self, pos):
        item = self.list_widget.itemAt(pos)
        if not item:
            return
        path = self._paths.get(item.text())
        if not path:
            return
        menu = QMenu(self)
        act_open = menu.addAction("打开")
        act_reveal = menu.addAction("在文件夹中显示")
        act_copy = menu.addAction("复制路径")
        if send2trash is not None:
            menu.addSeparator()
            act_trash = menu.addAction("移到回收站")
        chosen = menu.exec(self.list_widget.mapToGlobal(pos))
        if chosen == act_open:
            open_in_file_manager(path)
        elif chosen == act_reveal:
            open_in_file_manager(path if os.path.isdir(path) else os.path.dirname(path))
        elif chosen == act_copy:
            QGuiApplication.clipboard().setText(path)
        elif send2trash is not None and chosen == act_trash:
            try:
                send2trash(path)
            except Exception as e:
                QMessageBox.warning(self, "删除失败", str(e))


# ==========================================
# 4. 主灵动岛 Window (Dynamic Island Dock)
# ==========================================
class TidyDynamicIslandDock(QWidget):
    request_rescan = pyqtSignal()

    def __init__(self, desktop_path: str = None):
        super().__init__()
        self.desktop_path = desktop_path or get_desktop_path()
        self.index = DesktopIndex(self.desktop_path)

        self.compact_width = 560
        self.stretched_width = 780
        self.current_width = self.compact_width
        self.height_size = 58

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint |
                            Qt.WindowType.WindowStaysOnTopHint |
                            Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self._drag_offset: QPoint | None = None

        self.setup_ui()
        self.center_bottom_position()

        enable_windows_acrylic(int(self.winId()), dark=True)

        self.spring_anim = QPropertyAnimation(self, b"dockWidth")
        self.spring_anim.setDuration(450)
        self.spring_anim.setEasingCurve(QEasingCurve.Type.OutBack)

        # 定时重新扫描桌面（每 15 秒，低成本）
        self._scan_timer = QTimer(self)
        self._scan_timer.timeout.connect(self.rescan)
        self._scan_timer.start(15000)

    # ---- dockWidth 属性（动画用） ----
    def get_dock_width(self):
        return self.current_width

    def set_dock_width(self, w):
        self.current_width = w
        self.setFixedWidth(w)
        self.center_bottom_position()
        self.update()

    dockWidth = pyqtProperty(int, get_dock_width, set_dock_width)

    def setup_ui(self):
        self.setFixedHeight(self.height_size)
        self.setFixedWidth(self.compact_width)

        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(16, 0, 16, 0)
        self.main_layout.setSpacing(12)

        # 1. 品牌 Logo
        self.logo = StackedLogoWidget(self)
        self.main_layout.addWidget(self.logo)

        # 2. Pinned Apps（真实可点击）
        self.pinned_container = QWidget(self)
        pinned_layout = QHBoxLayout(self.pinned_container)
        pinned_layout.setContentsMargins(0, 0, 0, 0)
        pinned_layout.setSpacing(8)

        btn_browser = self.create_pinned_button("🌐", "Browser")
        btn_terminal = self.create_pinned_button("💻", "Terminal")
        btn_browser.clicked.connect(partial(open_default_app, "Browser"))
        btn_terminal.clicked.connect(partial(open_default_app, "Terminal"))
        pinned_layout.addWidget(btn_browser)
        pinned_layout.addWidget(btn_terminal)
        self.main_layout.addWidget(self.pinned_container)

        self.main_layout.addWidget(self.create_divider())

        # 3. AI 虚拟目录（矢量文件夹）
        self.folders_container = QWidget(self)
        folders_layout = QHBoxLayout(self.folders_container)
        folders_layout.setContentsMargins(0, 0, 0, 0)
        folders_layout.setSpacing(8)

        self.folders = {}
        for name in DesktopIndex.VIRTUAL_FOLDERS:
            icon = AppleVectorFolderIcon(name, self)
            icon.clicked.connect(self.open_folder_popover)
            self.folders[name] = icon
            folders_layout.addWidget(icon)
        self.main_layout.addWidget(self.folders_container)

        # Popover
        self.popover = TopPopoverPanel(self)
        self.popover.file_activated.connect(open_in_file_manager)

        # 4. 药丸型嵌入式搜索框
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Search desktop files...")
        self.search_input.setFixedHeight(32)
        self.search_input.setStyleSheet("""
            QLineEdit {
                background: rgba(255, 255, 255, 0.08);
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 14px;
                padding-left: 12px;
                padding-right: 12px;
                color: #FFFFFF;
                font-family: 'Segoe UI';
                font-size: 11px;
            }
            QLineEdit:focus {
                background: rgba(255, 255, 255, 0.14);
                border: 1px solid #0A84FF;
            }
        """)
        self.search_input.installEventFilter(self)
        self.search_input.textChanged.connect(self.on_search_text_changed)
        self.main_layout.addWidget(self.search_input)

        self.main_layout.addWidget(self.create_divider())

        # 5. 常驻时钟
        self.clock_widget = QWidget(self)
        clock_layout = QVBoxLayout(self.clock_widget)
        clock_layout.setContentsMargins(0, 10, 0, 10)
        clock_layout.setSpacing(0)

        self.time_label = QLabel(self)
        self.time_label.setFont(QFont("Segoe UI", 9, QFont.Weight.Bold))
        self.time_label.setStyleSheet("color: #FFFFFF;")

        self.date_label = QLabel(self)
        self.date_label.setFont(QFont("Segoe UI", 7))
        self.date_label.setStyleSheet("color: rgba(255, 255, 255, 0.6);")

        clock_layout.addWidget(self.time_label, 0, Qt.AlignmentFlag.AlignRight)
        clock_layout.addWidget(self.date_label, 0, Qt.AlignmentFlag.AlignRight)
        self.main_layout.addWidget(self.clock_widget)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)
        self.update_clock()

    def create_divider(self):
        divider = QFrame(self)
        divider.setFrameShape(QFrame.Shape.VLine)
        divider.setStyleSheet("color: rgba(255, 255, 255, 0.15); margin-top: 12px; margin-bottom: 12px;")
        return divider

    def create_pinned_button(self, icon_str, tooltip):
        btn = QPushButton(icon_str, self)
        btn.setFixedSize(32, 32)
        btn.setToolTip(f"Pinned: {tooltip}")
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setStyleSheet("""
            QPushButton {
                background: rgba(255, 255, 255, 0.06);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 8px;
                color: #FFFFFF;
                font-size: 14px;
            }
            QPushButton:hover { background: rgba(255, 255, 255, 0.18); }
            QPushButton:pressed { background: rgba(255, 255, 255, 0.26); }
        """)
        return btn

    def update_clock(self):
        self.time_label.setText(QTime.currentTime().toString("hh:mm A"))
        self.date_label.setText(QDate.currentDate().toString("MM/dd ddd"))

    def center_bottom_position(self):
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.current_width) // 2
        y = screen.height() - self.height_size - 24
        self.move(x, y)

    # ---- 桌面重扫 ----
    def rescan(self):
        self.index.scan()

    # ---- 弹簧动画 ----
    def trigger_spring_animation(self, target_width):
        if self.current_width == target_width:
            return
        self.spring_anim.stop()
        self.spring_anim.setStartValue(self.current_width)
        self.spring_anim.setEndValue(target_width)
        self.spring_anim.start()

    def stretch(self):
        self.trigger_spring_animation(self.stretched_width)

    def collapse(self):
        self.trigger_spring_animation(self.compact_width)

    # ---- 事件过滤：聚焦搜索框时拉伸；失焦/Esc 收起 ----
    def eventFilter(self, obj, event):
        if obj is self.search_input:
            t = event.type()
            if t == QEvent.Type.FocusIn:
                self.stretch()
            elif t == QEvent.Type.KeyPress:
                if isinstance(event, QKeyEvent) and event.key() == Qt.Key.Key_Escape:
                    self.search_input.clear()
                    self.search_input.clearFocus()
                    self.popover.hide()
                    self.collapse()
                    return True
        return super().eventFilter(obj, event)

    def on_search_text_changed(self, text):
        q = text.strip()
        if not q:
            self.popover.hide()
            return
        results = self.index.search(q)
        global_pos = self.mapToGlobal(self.search_input.pos())
        self.popover.show_search_results(q, global_pos, results)

    def open_folder_popover(self, folder_name):
        sender = self.sender()
        global_pos = self.mapToGlobal(sender.pos()) if sender else QCursor.pos()
        files = self.index.files_for_folder(folder_name)
        self.popover.show_folder_content(folder_name, global_pos, files)

    # ---- 窗口拖动（点击空白处）----
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            # 点在搜索框/按钮上时不拖动
            target = self.childAt(event.pos())
            if target is None or target is self.search_input:
                self._drag_offset = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
                if target is not self.search_input:
                    self.search_input.clearFocus()
                    self.popover.hide()
                    self.collapse()
            else:
                # 点击其它空白区域也收起
                self.search_input.clearFocus()
                self.popover.hide()
                self.collapse()
        elif event.button() == Qt.MouseButton.RightButton:
            self._show_context_menu(event.globalPosition().toPoint())

    def mouseMoveEvent(self, event):
        if self._drag_offset is not None and event.buttons() & Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self._drag_offset)

    def mouseReleaseEvent(self, event):
        self._drag_offset = None

    def _show_context_menu(self, global_pos):
        menu = QMenu(self)
        act_rescan = menu.addAction("🔄 重新扫描桌面")
        act_about = menu.addAction("ℹ️ 关于")
        menu.addSeparator()
        act_quit = menu.addAction("退出")
        chosen = menu.exec(global_pos)
        if chosen == act_rescan:
            self.rescan()
        elif chosen == act_about:
            QMessageBox.about(self, "关于 TidyUUUUp",
                              "TidyUUUUp v1.0.11\n灵动岛风格桌面整理 Dock\n\n"
                              f"桌面目录：{self.desktop_path}\n"
                              f"已索引文件：{len(self.index.files)} 个")
        elif chosen == act_quit:
            QApplication.quit()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), 24, 24)
        painter.fillPath(path, QColor(24, 24, 26, 215))
        pen = QPen(QColor(255, 255, 255, 35), 1)
        painter.setPen(pen)
        painter.drawPath(path)


# ==========================================
# 5. 系统托盘
# ==========================================
def install_tray(dock: TidyDynamicIslandDock) -> QSystemTrayIcon | None:
    try:
        tray = QSystemTrayIcon(dock)
        # 优先用主题图标，缺失时回退到自绘 pixmap
        icon = QIcon()
        for theme_icon in (QIcon.ThemeIcon.FolderOpen, QIcon.ThemeIcon.GoHome,
                           QIcon.ThemeIcon.Computer):
            cand = QIcon.fromTheme(theme_icon)
            if not cand.isNull():
                icon = cand
                break
        if icon.isNull():
            # 自绘一个简单的蓝色文件夹图标作为兜底
            from PyQt6.QtGui import QPixmap
            pix = QPixmap(64, 64)
            pix.fill(QColor(0, 0, 0, 0))
            p = QPainter(pix)
            p.setRenderHint(QPainter.RenderHint.Antialiasing)
            p.setBrush(QColor(0, 122, 255))
            p.setPen(Qt.PenStyle.NoPen)
            p.drawRoundedRect(8, 20, 48, 36, 6, 6)
            p.drawRoundedRect(8, 12, 20, 12, 4, 4)
            p.end()
            icon = QIcon(pix)
        tray.setIcon(icon)
        tray.setToolTip("TidyUUUUp Dock")
        menu = QMenu()
        a_show = menu.addAction("显示 Dock")
        a_rescan = menu.addAction("重新扫描桌面")
        a_about = menu.addAction("关于")
        menu.addSeparator()
        a_quit = menu.addAction("退出")
        a_show.triggered.connect(dock.show)
        a_rescan.triggered.connect(dock.rescan)
        a_about.triggered.connect(lambda: QMessageBox.about(
            None, "关于 TidyUUUUp",
            "TidyUUUUp v1.0.11\n灵动岛风格桌面整理 Dock"))
        a_quit.triggered.connect(QApplication.quit)
        tray.setContextMenu(menu)
        tray.show()
        return tray
    except Exception as e:
        print(f"[Tray] {e}")
        return None


# ==========================================
# 6. 主程序入口
# ==========================================
def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setApplicationName("TidyUUUUp")

    dock = TidyDynamicIslandDock()
    dock.show()

    tray = install_tray(dock)

    # 托盘缺失时通过 dock 右键菜单仍可退出
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
