"""
TidyUUUUp - Apple 风格样式表 v1.0.8
参考：Apple HIG, macOS Sonoma 控制中心 / Finder / Dock

核心设计原则 (Apple Light):
1. 浅色 / 极淡的冷色调磨砂玻璃背景
2. 灰阶分层（80/70/50% Alpha 白作三层深度）
3. 细 0.6px Hairline 边框（极淡的灰蓝）
4. 深灰文字（#1D1D1F ~ #3C3C43），Apple 官方前景色
5. 悬停时稍亮（不发光，只加强对比度）
6. 统一控件高度与圆角（12/14/16 三档）
7. 颜色克制：仅 Accent 用 Apple 蓝，其他用灰阶分层
"""

LIQUID_GLASS_PRO_QSS = """
* {
    font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Segoe UI", "Microsoft YaHei", sans-serif;
    color: #1D1D1F;
}

QMainWindow, QWidget {
    background: transparent;
}

/* ============================================================
   玻璃容器 - 三层深度（仿控制中心卡片）
   ============================================================ */

.LiquidGlassPro {
    background: rgba(250, 251, 255, 0.78);
    border: 1px solid rgba(120, 130, 160, 0.18);
    border-radius: 22px;
    color: #1D1D1F;
}

.LiquidGlassPanel {
    background: rgba(248, 250, 255, 0.82);
    border: 1px solid rgba(120, 130, 160, 0.15);
    border-radius: 16px;
    color: #1D1D1F;
}

.LiquidGlassCard {
    background: rgba(252, 253, 255, 0.88);
    border: 1px solid rgba(120, 130, 160, 0.12);
    border-radius: 12px;
    color: #1D1D1F;
}

.LiquidGlassCard:hover {
    background: rgba(255, 255, 255, 0.95);
    border: 1px solid rgba(120, 130, 160, 0.25);
}

/* ============================================================
   Dock 栏（动态绘制为主，这里只补充兜底）
   ============================================================ */

#DockItem {
    background: transparent;
    border: none;
    border-radius: 14px;
    padding: 4px;
}

#DockItem:hover {
    background: rgba(255, 255, 255, 0.45);
    border: 1px solid rgba(255, 255, 255, 0.65);
}

#DockItem:pressed {
    background: rgba(10, 132, 255, 0.18);
    border: 1px solid rgba(10, 132, 255, 0.35);
    padding: 6px 2px 2px 6px;
}

/* ============================================================
   系统按钮
   ============================================================ */

#SystemButton {
    background: rgba(250, 251, 255, 0.75);
    border: 1px solid rgba(120, 130, 160, 0.18);
    border-radius: 12px;
    padding: 6px;
    font-size: 20px;
}

#SystemButton:hover {
    background: rgba(255, 255, 255, 0.92);
    border: 1px solid rgba(120, 130, 160, 0.30);
}

#SystemButton:pressed {
    background: rgba(10, 132, 255, 0.20);
    border: 1px solid rgba(10, 132, 255, 0.40);
    padding: 8px 4px 4px 8px;
}

/* ============================================================
   撤销按钮
   ============================================================ */

#UndoButton {
    background: rgba(255, 204, 0, 0.18);
    border: 1px solid rgba(255, 159, 10, 0.25);
    border-radius: 14px;
    padding: 6px;
}

#UndoButton:hover {
    background: rgba(255, 204, 0, 0.30);
    border: 1px solid rgba(255, 159, 10, 0.40);
}

#UndoButton:pressed {
    background: rgba(255, 159, 10, 0.40);
    padding: 8px 4px 4px 8px;
}

#UndoBadge {
    background: rgba(255, 59, 48, 235);
    border: 1px solid rgba(255, 255, 255, 0.85);
    border-radius: 9px;
    color: white;
    font-size: 10px;
    font-weight: 700;
}

/* ============================================================
   开始按钮
   ============================================================ */

#StartButton {
    background: rgba(10, 132, 255, 0.12);
    border: 1px solid rgba(10, 132, 255, 0.22);
    border-radius: 14px;
    padding: 6px;
}

#StartButton:hover {
    background: rgba(10, 132, 255, 0.22);
    border: 1px solid rgba(10, 132, 255, 0.40);
}

#StartButton:pressed {
    background: rgba(10, 132, 255, 0.35);
    padding: 8px 4px 4px 8px;
}

/* ============================================================
   搜索框
   ============================================================ */

#SearchBox {
    background: rgba(255, 255, 255, 0.90);
    border: 1px solid rgba(120, 130, 160, 0.20);
    border-radius: 12px;
    padding: 9px 18px;
    color: #1D1D1F;
    font-size: 13px;
    selection-background-color: rgba(10, 132, 255, 0.25);
    selection-color: #1D1D1F;
}

#SearchBox:focus {
    border: 1px solid rgba(10, 132, 255, 0.50);
    background: rgba(255, 255, 255, 1.0);
}

/* ============================================================
   通用按钮
   ============================================================ */

QPushButton {
    background: rgba(10, 132, 255, 0.14);
    border: 1px solid rgba(10, 132, 255, 0.25);
    border-radius: 10px;
    padding: 9px 22px;
    color: #0A84FF;
    font-size: 13px;
    font-weight: 600;
}

QPushButton:hover {
    background: rgba(10, 132, 255, 0.24);
    border: 1px solid rgba(10, 132, 255, 0.40);
    color: #0066CC;
}

QPushButton:pressed {
    background: rgba(10, 132, 255, 0.35);
    padding: 11px 20px 7px 24px;
}

QPushButton:disabled {
    background: rgba(120, 130, 160, 0.10);
    border: 1px solid rgba(120, 130, 160, 0.12);
    color: rgba(120, 130, 160, 0.50);
}

#SecondaryButton {
    background: rgba(250, 251, 255, 0.70);
    border: 1px solid rgba(120, 130, 160, 0.20);
    color: #1D1D1F;
}

#SecondaryButton:hover {
    background: rgba(255, 255, 255, 0.92);
    border: 1px solid rgba(120, 130, 160, 0.30);
    color: #1D1D1F;
}

/* ============================================================
   标签
   ============================================================ */

QLabel {
    color: #1D1D1F;
    font-size: 13px;
    background: transparent;
}

#TitleLabel {
    font-size: 24px;
    font-weight: 700;
    color: #1D1D1F;
}

#SubtitleLabel {
    font-size: 13px;
    color: #6E6E73;
}

#CategoryBadge {
    background: rgba(10, 132, 255, 0.12);
    border: 1px solid rgba(10, 132, 255, 0.20);
    border-radius: 8px;
    padding: 4px 12px;
    color: #0A84FF;
    font-size: 11px;
    font-weight: 600;
}

/* ============================================================
   列表
   ============================================================ */

QListWidget {
    background: transparent;
    border: none;
    outline: none;
    color: #1D1D1F;
}

QListWidget::item {
    background: transparent;
    border-radius: 10px;
    padding: 9px;
    margin: 2px 0;
}

QListWidget::item:hover {
    background: rgba(120, 130, 160, 0.10);
    border: 1px solid rgba(120, 130, 160, 0.12);
}

QListWidget::item:selected {
    background: rgba(10, 132, 255, 0.16);
    border: 1px solid rgba(10, 132, 255, 0.30);
    color: #0A84FF;
}

/* ============================================================
   滚动条
   ============================================================ */

QScrollBar:vertical {
    background: transparent;
    width: 8px;
    margin: 4px 3px;
}

QScrollBar::handle:vertical {
    background: rgba(120, 130, 160, 0.28);
    border-radius: 4px;
    min-height: 36px;
}

QScrollBar::handle:vertical:hover {
    background: rgba(120, 130, 160, 0.48);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

QScrollBar:horizontal {
    background: transparent;
    height: 8px;
    margin: 3px 4px;
}

QScrollBar::handle:horizontal {
    background: rgba(120, 130, 160, 0.28);
    border-radius: 4px;
    min-width: 36px;
}

QScrollBar::handle:horizontal:hover {
    background: rgba(120, 130, 160, 0.48);
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0;
}

/* ============================================================
   复选框
   ============================================================ */

QCheckBox {
    color: #1D1D1F;
    spacing: 10px;
    font-size: 13px;
    background: transparent;
}

QCheckBox::indicator {
    width: 19px;
    height: 19px;
    border-radius: 6px;
    border: 1.2px solid rgba(120, 130, 160, 0.35);
    background: rgba(255, 255, 255, 0.90);
}

QCheckBox::indicator:checked {
    background: rgba(10, 132, 255, 230);
    border: 1.2px solid rgba(10, 132, 255, 0.70);
}

QCheckBox::indicator:hover {
    border: 1.2px solid rgba(10, 132, 255, 0.45);
}

/* ============================================================
   下拉框
   ============================================================ */

QComboBox {
    background: rgba(255, 255, 255, 0.90);
    border: 1px solid rgba(120, 130, 160, 0.20);
    border-radius: 10px;
    padding: 7px 14px;
    color: #1D1D1F;
    font-size: 13px;
}

QComboBox:hover {
    border: 1px solid rgba(120, 130, 160, 0.35);
}

QComboBox::drop-down {
    border: none;
    width: 22px;
}

QComboBox QAbstractItemView {
    background: rgba(250, 251, 255, 0.98);
    border: 1px solid rgba(120, 130, 160, 0.18);
    border-radius: 12px;
    color: #1D1D1F;
    selection-background-color: rgba(10, 132, 255, 0.16);
    selection-color: #0A84FF;
    padding: 5px;
    outline: none;
}

/* ============================================================
   输入框
   ============================================================ */

QLineEdit, QTextEdit {
    background: rgba(255, 255, 255, 0.92);
    border: 1px solid rgba(120, 130, 160, 0.22);
    border-radius: 9px;
    padding: 7px 13px;
    color: #1D1D1F;
    font-size: 13px;
    selection-background-color: rgba(10, 132, 255, 0.25);
    selection-color: #1D1D1F;
}

QLineEdit:focus, QTextEdit:focus {
    border: 1px solid rgba(10, 132, 255, 0.50);
    background: rgba(255, 255, 255, 1.0);
}

/* ============================================================
   进度条
   ============================================================ */

QProgressBar {
    background: rgba(120, 130, 160, 0.12);
    border: 1px solid rgba(120, 130, 160, 0.15);
    border-radius: 7px;
    height: 9px;
    text-align: center;
    color: #3C3C43;
}

QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0.0 #64D2FF,
        stop:0.5 #0A84FF,
        stop:1.0 #5E5CE6
    );
    border-radius: 7px;
}

/* ============================================================
   分类侧边栏
   ============================================================ */

#CategorySidebar {
    background: rgba(250, 251, 255, 0.60);
    border-right: 1px solid rgba(120, 130, 160, 0.12);
}

#CategoryItem {
    background: transparent;
    border: none;
    border-radius: 10px;
    padding: 11px 16px;
    color: #6E6E73;
    text-align: left;
    font-size: 13px;
}

#CategoryItem:hover {
    background: rgba(120, 130, 160, 0.10);
    color: #1D1D1F;
}

#CategoryItem:checked {
    background: rgba(10, 132, 255, 0.14);
    color: #0A84FF;
    border: 1px solid rgba(10, 132, 255, 0.22);
}

/* ============================================================
   Tab 组件
   ============================================================ */

QTabWidget::pane {
    border: none;
    background: transparent;
}

QTabBar::tab {
    background: transparent;
    color: #6E6E73;
    padding: 11px 22px;
    border: none;
    border-bottom: 2px solid transparent;
    font-size: 13px;
    font-weight: 500;
}

QTabBar::tab:hover {
    color: #1D1D1F;
}

QTabBar::tab:selected {
    color: #0A84FF;
    border-bottom: 2px solid rgba(10, 132, 255, 230);
}

/* ============================================================
   菜单
   ============================================================ */

QMenu {
    background: rgba(250, 251, 255, 0.98);
    border: 1px solid rgba(120, 130, 160, 0.16);
    border-radius: 13px;
    padding: 6px;
    color: #1D1D1F;
}

QMenu::item {
    padding: 9px 20px;
    border-radius: 7px;
    font-size: 13px;
    color: #1D1D1F;
}

QMenu::item:hover {
    background: rgba(10, 132, 255, 0.14);
    color: #0A84FF;
}

QMenu::separator {
    height: 1px;
    background: rgba(120, 130, 160, 0.12);
    margin: 5px 10px;
}

/* ============================================================
   Quick Look 预览面板
   ============================================================ */

#QuickLookPanel {
    background: rgba(250, 251, 255, 0.96);
    border: 1px solid rgba(120, 130, 160, 0.18);
    border-radius: 18px;
    color: #1D1D1F;
}

#QuickLookImage {
    background: rgba(255, 255, 255, 0.90);
    border: 1px solid rgba(120, 130, 160, 0.14);
    border-radius: 11px;
}

#QuickLookInfo {
    background: rgba(250, 251, 255, 0.82);
    border: 1px solid rgba(120, 130, 160, 0.14);
    border-radius: 9px;
    padding: 9px 13px;
    color: #1D1D1F;
}

#ConfidenceBar {
    background: rgba(120, 130, 160, 0.10);
    border: 1px solid rgba(120, 130, 160, 0.12);
    border-radius: 5px;
    height: 7px;
}

#ConfidenceChunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0.0 #64D2FF,
        stop:0.5 #0A84FF,
        stop:1.0 #BF5AF2
    );
    border-radius: 5px;
}

/* ============================================================
   虚拟文件夹
   ============================================================ */

#VirtualFolder {
    background: rgba(255, 159, 10, 0.14);
    border: 1px solid rgba(255, 159, 10, 0.22);
    border-radius: 12px;
    padding: 6px;
}

#VirtualFolder:hover {
    background: rgba(255, 159, 10, 0.24);
    border: 1px solid rgba(255, 159, 10, 0.40);
}

#VirtualFolder:pressed {
    background: rgba(255, 159, 10, 0.35);
    padding: 8px 4px 4px 8px;
}

/* ============================================================
   Toast
   ============================================================ */

#Toast {
    background: rgba(250, 251, 255, 0.96);
    border: 1px solid rgba(120, 130, 160, 0.18);
    border-radius: 11px;
    padding: 11px 18px;
    color: #1D1D1F;
}

/* ============================================================
   撤销面板
   ============================================================ */

#UndoPanel {
    background: rgba(250, 251, 255, 0.96);
    border: 1px solid rgba(120, 130, 160, 0.18);
    border-radius: 16px;
    color: #1D1D1F;
}

#UndoRecordItem {
    background: rgba(250, 251, 255, 0.72);
    border: 1px solid rgba(120, 130, 160, 0.12);
    border-radius: 9px;
    padding: 9px 13px;
    color: #1D1D1F;
}

#UndoRecordItem:hover {
    background: rgba(10, 132, 255, 0.12);
    border: 1px solid rgba(10, 132, 255, 0.22);
    color: #0A84FF;
}

#UndoRecordItem:pressed {
    background: rgba(10, 132, 255, 0.22);
    color: #0066CC;
}

/* ============================================================
   悬浮球
   ============================================================ */

#FloatingBall {
    background: transparent;
    border: none;
}
"""


def apply_liquid_glass(app):
    """应用 Apple 风格样式"""
    app.setStyleSheet(LIQUID_GLASS_PRO_QSS)
