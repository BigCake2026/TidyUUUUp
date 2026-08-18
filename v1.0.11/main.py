"""
TidyUUUUp v1.0.11 - Dynamic Island Dock
灵动岛风格 Dock，基于 PyQt6

修正记录：
  - 修正 pyqtProperty 未导入的 bug（原代码使用但未从 PyQt6.QtCore 导入）
"""
import sys
import os
import ctypes
from ctypes import wintypes
from PyQt6.QtCore import (Qt, QTimer, QTime, QDate, QPropertyAnimation,
                           QEasingCurve, QRect, QSize, pyqtSignal, pyqtProperty)
from PyQt6.QtGui import (QPainter, QColor, QFont, QPen, QBrush,
                         QPainterPath, QLinearGradient, QAction, QIcon)
from PyQt6.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
                             QLabel, QLineEdit, QPushButton, QFrame,
                             QGraphicsDropShadowEffect, QListWidget, QListWidgetItem, QMenu)

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
    """开启 Windows 10/11 原生 API 的 Acrylic 深度毛玻璃效果"""
    try:
        user32 = ctypes.windll.user32
        ACCENT_ENABLE_ACRYLICBLURBEHIND = 4

        # 0xCC000000 为深色半透明，0xCCFFFFFF 为浅色半透明
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

        # Tidy (Top)
        painter.setFont(QFont("Segoe UI", 9, QFont.Weight.DemiBold))
        painter.setPen(QColor(255, 255, 255, 210))
        painter.drawText(QRect(0, 8, 64, 16), Qt.AlignmentFlag.AlignLeft, "Tidy")

        # UUUUp (Bottom)
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
        painter.setPen(QPen(QColor(255, 255, 255, 70), 1))
        painter.drawPath(body_path)


# ==========================================
# 3. 顶部 Popover 悬浮毛玻璃面板
# ==========================================
class TopPopoverPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.WindowType.ToolTip | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(360, 220)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)

        self.title_label = QLabel("AI Virtual Directory", self)
        self.title_label.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        self.title_label.setStyleSheet("color: #FFFFFF;")
        layout.addWidget(self.title_label)

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
        """)
        layout.addWidget(self.list_widget)

        # 模拟内部文件可点击交互
        self.list_widget.itemClicked.connect(self.on_file_clicked)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # 毛玻璃背景底板
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), 18, 18)

        painter.fillPath(path, QColor(30, 30, 32, 215))
        painter.setPen(QPen(QColor(255, 255, 255, 30), 1.2))
        painter.drawPath(path)

    def show_folder_content(self, folder_name, global_pos):
        self.title_label.setText(f"📁 {folder_name} (Desktop Virtual Mapping)")
        self.list_widget.clear()

        # 物理桌面文件不移动，仅做 AI 内容语义分类映射
        mock_files = {
            "Finance AI": ["Q3_Financial_Forecast.xlsx (98%)", "Tax_Invoice_2026.pdf", "Budget_Allocation.docx"],
            "Design Spec": ["VisionOS_Design_Tokens.fig", "AppIcon_Master_v2.png", "UI_Guidelines.pdf"],
            "Code Engine": ["tidyuuuup_dock.py", "native_bridge.cpp", "manifest.json"]
        }

        files = mock_files.get(folder_name, ["Indexed_Document_01.pdf", "Project_Notes.txt"])
        for f in files:
            self.list_widget.addItem(QListWidgetItem(f))

        self.move(global_pos.x() - 140, global_pos.y() - self.height() - 12)
        self.show()

    def show_search_results(self, query, global_pos):
        self.title_label.setText(f"🔍 Semantic Search Matches")
        self.list_widget.clear()
        if not query:
            self.hide()
            return

        self.list_widget.addItem(QListWidgetItem(f"Match 98% • {query}_Analysis_Report.pdf"))
        self.list_widget.addItem(QListWidgetItem(f"Match 87% • Desktop/Drafts/{query}_v1.docx"))
        self.list_widget.addItem(QListWidgetItem(f"Match 75% • Archive/2026_{query}.notes"))

        self.move(global_pos.x() - 100, global_pos.y() - self.height() - 12)
        self.show()

    def on_file_clicked(self, item):
        print(f"[TidyUUUUp Action] Opening virtual file: {item.text()}")
        self.hide()


# ==========================================
# 4. 主灵动岛 Window (Dynamic Island Dock)
# ==========================================
class TidyDynamicIslandDock(QWidget):
    def __init__(self):
        super().__init__()

        # 基础尺寸配置
        self.compact_width = 560
        self.stretched_width = 780
        self.current_width = self.compact_width
        self.height_size = 58

        # 窗口无边框、置顶、任务栏隐藏
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint |
                            Qt.WindowType.WindowStaysOnTopHint |
                            Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setup_ui()
        self.center_bottom_position()

        # 开启原生 Acrylic 毛玻璃
        enable_windows_acrylic(int(self.winId()), dark=True)

        # 弹簧伸缩动画 (Apple Spring Physics Simulation)
        self.spring_anim = QPropertyAnimation(self, b"dockWidth")
        self.spring_anim.setDuration(450)
        self.spring_anim.setEasingCurve(QEasingCurve.Type.OutBack)  # 带过冲与回弹感

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

        # 全局布局 (零无用空白)
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(16, 0, 16, 0)
        self.main_layout.setSpacing(12)

        # 1. 品牌 Logo (Stacked)
        self.logo = StackedLogoWidget(self)
        self.main_layout.addWidget(self.logo)

        # 2. Pinned Apps/Files (固定应用区)
        self.pinned_container = QWidget(self)
        pinned_layout = QHBoxLayout(self.pinned_container)
        pinned_layout.setContentsMargins(0, 0, 0, 0)
        pinned_layout.setSpacing(8)

        btn_safari = self.create_pinned_button("🌐", "Browser")
        btn_terminal = self.create_pinned_button("💻", "Terminal")
        pinned_layout.addWidget(btn_safari)
        pinned_layout.addWidget(btn_terminal)
        self.main_layout.addWidget(self.pinned_container)

        # 分割线
        self.main_layout.addWidget(self.create_divider())

        # 3. AI 虚拟目录 (Apple Vector Folders)
        self.folders_container = QWidget(self)
        folders_layout = QHBoxLayout(self.folders_container)
        folders_layout.setContentsMargins(0, 0, 0, 0)
        folders_layout.setSpacing(8)

        self.folder_fin = AppleVectorFolderIcon("Finance AI", self)
        self.folder_des = AppleVectorFolderIcon("Design Spec", self)
        self.folder_code = AppleVectorFolderIcon("Code Engine", self)

        folders_layout.addWidget(self.folder_fin)
        folders_layout.addWidget(self.folder_des)
        folders_layout.addWidget(self.folder_code)

        self.main_layout.addWidget(self.folders_container)

        # Popover 弹窗实例化
        self.popover = TopPopoverPanel(self)
        self.folder_fin.clicked.connect(self.open_folder_popover)
        self.folder_des.clicked.connect(self.open_folder_popover)
        self.folder_code.clicked.connect(self.open_folder_popover)

        # 4. 药丸型嵌入式搜索框 (Embedded Search Pill)
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Search content / similarity...")
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
        self.search_input.focused = False
        self.search_input.selectionChanged.connect(self.on_search_focused)
        self.search_input.textChanged.connect(self.on_search_text_changed)
        self.main_layout.addWidget(self.search_input)

        # 分割线
        self.main_layout.addWidget(self.create_divider())

        # 5. 常驻内置时间/日期 (Embedded Integrated Clock on Far Right)
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

        # 时钟定时器
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
        btn.setStyleSheet("""
            QPushButton {
                background: rgba(255, 255, 255, 0.06);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 8px;
                color: #FFFFFF;
                font-size: 14px;
            }
            QPushButton:hover {
                background: rgba(255, 255, 255, 0.18);
            }
        """)
        return btn

    def update_clock(self):
        self.time_label.setText(QTime.currentTime().toString("hh:mm A"))
        self.date_label.setText(QDate.currentDate().toString("MM/dd ddd"))

    def center_bottom_position(self):
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.current_width) // 2
        y = screen.height() - self.height_size - 24  # 距离底栏 24px
        self.move(x, y)

    def trigger_spring_animation(self, target_width):
        if self.current_width == target_width:
            return
        self.spring_anim.stop()
        self.spring_anim.setStartValue(self.current_width)
        self.spring_anim.setEndValue(target_width)
        self.spring_anim.start()

    def on_search_focused(self):
        # 点击/聚焦搜索框时触发 Apple Spring 伸缩变长
        self.trigger_spring_animation(self.stretched_width)

    def on_search_text_changed(self, text):
        if text.strip():
            global_pos = self.mapToGlobal(self.search_input.pos())
            self.popover.show_search_results(text.strip(), global_pos)
        else:
            self.popover.hide()

    def open_folder_popover(self, folder_name):
        # 伸缩还原或展示 Popover
        sender = self.sender()
        global_pos = self.mapToGlobal(sender.pos())
        self.popover.show_folder_content(folder_name, global_pos)

    def mousePressEvent(self, event):
        # 点击小岛空白处收起搜索框
        if not self.search_input.geometry().contains(event.pos()):
            self.search_input.clearFocus()
            self.popover.hide()
            self.trigger_spring_animation(self.compact_width)

    def paintEvent(self, event):
        # 绘制灵动岛半透明圆角底板与高光边框
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), 24, 24)

        # 极简深色半透明玻璃底色
        painter.fillPath(path, QColor(24, 24, 26, 200))

        # 1px 顶部微光描边
        pen = QPen(QColor(255, 255, 255, 35), 1)
        painter.setPen(pen)
        painter.drawPath(path)


# ==========================================
# 5. 主程序入口
# ==========================================
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 启用高 DPI 缩放
    app.setStyle("Fusion")

    dock = TidyDynamicIslandDock()
    dock.show()

    sys.exit(app.exec())
