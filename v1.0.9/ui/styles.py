"""
TidyUUUUp Design System v2.0
参考 Apple HIG / macOS Sonoma 原生应用

设计原则：
  克制 · 留白 · 层次 · 安静

色彩系统：
  Background    #F5F5F7   接近白的浅灰
  Window        #FFFFFF    纯白窗口
  Primary Text  #1D1D1F   深灰（非纯黑）
  Secondary     #86868B    中灰
  Tertiary      #AEAEB2    浅灰
  Border        rgba(0,0,0,0.06)  极淡边框
  Accent        #007AFF   系统蓝
  Accent Light  rgba(0,122,255,0.08)

圆角层级：
  窗口    12px
  卡片    10px
  按钮     6px
  输入框   6px
  Badge    4px

字体：
  -apple-system, SF Pro Text, PingFang SC
  标题 17/600 · 正文 13/400 · 辅助 11/400
"""

TIDY_QSS = """
/* ========================================
   全局
   ======================================== */
* {
    font-family: -apple-system, "SF Pro Text", "SF Pro Display",
                 "PingFang SC", "Segoe UI", sans-serif;
    color: #1D1D1F;
}

QMainWindow, QWidget {
    background: transparent;
}

/* ========================================
   窗口背景
   ======================================== */
#WindowBackground {
    background: #F5F5F7;
}

#ContentBackground {
    background: #FFFFFF;
}

/* ========================================
   顶部栏
   ======================================== */
#TopBar {
    background: rgba(255, 255, 255, 0.80);
    border-bottom: 1px solid rgba(0, 0, 0, 0.06);
}

#LogoLabel {
    font-size: 15px;
    font-weight: 600;
    color: #1D1D1F;
    letter-spacing: 0.3px;
}

/* ========================================
   搜索框 (Spotlight 风格)
   ======================================== */
#SearchBox {
    background: rgba(0, 0, 0, 0.04);
    border: none;
    border-radius: 6px;
    padding: 7px 14px;
    color: #1D1D1F;
    font-size: 13px;
    selection-background-color: rgba(0, 122, 255, 0.15);
}

#SearchBox:focus {
    background: rgba(0, 0, 0, 0.06);
    border: none;
}

#SearchBox::placeholder {
    color: #86868B;
}

/* ========================================
   按钮
   ======================================== */

/* 主按钮 - 系统蓝 */
QPushButton {
    background: #007AFF;
    border: none;
    border-radius: 6px;
    padding: 8px 20px;
    color: #FFFFFF;
    font-size: 13px;
    font-weight: 500;
}

QPushButton:hover {
    background: #0066D6;
}

QPushButton:pressed {
    background: #0055B3;
}

QPushButton:disabled {
    background: #D1D1D6;
    color: #86868B;
}

/* 次要按钮 - 灰色 */
#SecondaryButton {
    background: rgba(0, 0, 0, 0.05);
    color: #1D1D1F;
    border: none;
}

#SecondaryButton:hover {
    background: rgba(0, 0, 0, 0.08);
}

#SecondaryButton:pressed {
    background: rgba(0, 0, 0, 0.12);
}

/* 文字按钮 - 无背景 */
#TextButton {
    background: transparent;
    color: #007AFF;
    border: none;
    padding: 6px 12px;
}

#TextButton:hover {
    background: rgba(0, 122, 255, 0.06);
}

#TextButton:pressed {
    background: rgba(0, 122, 255, 0.12);
}

/* ========================================
   侧边栏
   ======================================== */
#Sidebar {
    background: rgba(245, 245, 247, 0.60);
    border-right: 1px solid rgba(0, 0, 0, 0.04);
}

#SidebarHeader {
    color: #86868B;
    font-size: 11px;
    font-weight: 600;
    padding: 4px 12px;
    letter-spacing: 0.5px;
}

#SidebarItem {
    background: transparent;
    border: none;
    border-radius: 6px;
    padding: 6px 12px;
    color: #1D1D1F;
    text-align: left;
    font-size: 13px;
    font-weight: 400;
}

#SidebarItem:hover {
    background: rgba(0, 0, 0, 0.04);
}

#SidebarItem:checked {
    background: rgba(0, 0, 0, 0.07);
    color: #1D1D1F;
    font-weight: 500;
}

/* ========================================
   文件列表
   ======================================== */
#FileList {
    background: transparent;
    border: none;
    outline: none;
}

#FileList::item {
    background: transparent;
    border-bottom: 1px solid rgba(0, 0, 0, 0.03);
    padding: 4px 0;
}

#FileList::item:hover {
    background: rgba(0, 0, 0, 0.02);
}

#FileList::item:selected {
    background: rgba(0, 122, 255, 0.06);
}

/* ========================================
   Empty State
   ======================================== */
#EmptyStateIcon {
    color: #D1D1D6;
    font-size: 48px;
}

#EmptyStateTitle {
    color: #86868B;
    font-size: 17px;
    font-weight: 500;
}

#EmptyStateDesc {
    color: #AEAEB2;
    font-size: 13px;
}

/* ========================================
   标签
   ======================================== */
QLabel {
    color: #1D1D1F;
    font-size: 13px;
    background: transparent;
}

#TitleLabel {
    font-size: 17px;
    font-weight: 600;
    color: #1D1D1F;
}

#SubtitleLabel {
    font-size: 13px;
    color: #86868B;
}

#MetaLabel {
    color: #86868B;
    font-size: 11px;
}

/* ========================================
   Badge (极小)
   ======================================== */
#Badge {
    background: #007AFF;
    border-radius: 4px;
    padding: 1px 6px;
    color: #FFFFFF;
    font-size: 10px;
    font-weight: 600;
    min-width: 16px;
}

#BadgeGray {
    background: rgba(0, 0, 0, 0.08);
    border-radius: 4px;
    padding: 1px 6px;
    color: #86868B;
    font-size: 10px;
    font-weight: 500;
}

/* ========================================
   输入框
   ======================================== */
QLineEdit, QTextEdit {
    background: #FFFFFF;
    border: 1px solid rgba(0, 0, 0, 0.08);
    border-radius: 6px;
    padding: 7px 12px;
    color: #1D1D1F;
    font-size: 13px;
    selection-background-color: rgba(0, 122, 255, 0.15);
}

QLineEdit:focus, QTextEdit:focus {
    border: 1px solid rgba(0, 122, 255, 0.4);
}

/* ========================================
   下拉框
   ======================================== */
QComboBox {
    background: rgba(0, 0, 0, 0.04);
    border: 1px solid rgba(0, 0, 0, 0.06);
    border-radius: 6px;
    padding: 6px 12px;
    color: #1D1D1F;
    font-size: 13px;
}

QComboBox:hover {
    background: rgba(0, 0, 0, 0.06);
}

QComboBox::drop-down {
    border: none;
    width: 20px;
}

QComboBox QAbstractItemView {
    background: #FFFFFF;
    border: 1px solid rgba(0, 0, 0, 0.08);
    border-radius: 8px;
    color: #1D1D1F;
    selection-background-color: rgba(0, 122, 255, 0.08);
    selection-color: #007AFF;
    padding: 4px;
    outline: none;
}

/* ========================================
   复选框
   ======================================== */
QCheckBox {
    color: #1D1D1F;
    spacing: 8px;
    font-size: 13px;
    background: transparent;
}

QCheckBox::indicator {
    width: 16px;
    height: 16px;
    border-radius: 4px;
    border: 1.5px solid #D1D1D6;
    background: #FFFFFF;
}

QCheckBox::indicator:checked {
    background: #007AFF;
    border: 1.5px solid #007AFF;
}

QCheckBox::indicator:hover {
    border: 1.5px solid #86868B;
}

/* ========================================
   进度条
   ======================================== */
QProgressBar {
    background: rgba(0, 0, 0, 0.05);
    border: none;
    border-radius: 3px;
    height: 4px;
    text-align: center;
}

QProgressBar::chunk {
    background: #007AFF;
    border-radius: 3px;
}

/* ========================================
   滚动条 (极细)
   ======================================== */
QScrollBar:vertical {
    background: transparent;
    width: 6px;
    margin: 0;
}

QScrollBar::handle:vertical {
    background: rgba(0, 0, 0, 0.15);
    border-radius: 3px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover {
    background: rgba(0, 0, 0, 0.25);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: transparent;
}

QScrollBar:horizontal {
    background: transparent;
    height: 6px;
    margin: 0;
}

QScrollBar::handle:horizontal {
    background: rgba(0, 0, 0, 0.15);
    border-radius: 3px;
    min-width: 30px;
}

QScrollBar::handle:horizontal:hover {
    background: rgba(0, 0, 0, 0.25);
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0;
}

/* ========================================
   菜单
   ======================================== */
QMenu {
    background: rgba(255, 255, 255, 0.95);
    border: 1px solid rgba(0, 0, 0, 0.06);
    border-radius: 8px;
    padding: 4px;
    color: #1D1D1F;
}

QMenu::item {
    padding: 6px 16px;
    border-radius: 4px;
    font-size: 13px;
}

QMenu::item:hover {
    background: rgba(0, 122, 255, 0.08);
    color: #007AFF;
}

QMenu::separator {
    height: 1px;
    background: rgba(0, 0, 0, 0.06);
    margin: 4px 8px;
}

/* ========================================
   Dock
   ======================================== */
#DockContainer {
    background: rgba(255, 255, 255, 0.72);
    border: 1px solid rgba(0, 0, 0, 0.05);
    border-radius: 10px;
}

#DockButton {
    background: transparent;
    border: none;
    border-radius: 6px;
    padding: 4px;
    color: #1D1D1F;
    font-size: 11px;
}

#DockButton:hover {
    background: rgba(0, 0, 0, 0.06);
}

#DockButton:pressed {
    background: rgba(0, 0, 0, 0.10);
}

/* ========================================
   Tab
   ======================================== */
QTabWidget::pane {
    border: none;
    background: transparent;
}

QTabBar::tab {
    background: transparent;
    color: #86868B;
    padding: 8px 16px;
    border: none;
    font-size: 13px;
}

QTabBar::tab:hover {
    color: #1D1D1F;
}

QTabBar::tab:selected {
    color: #1D1D1F;
    font-weight: 500;
}

/* ========================================
   Toast
   ======================================== */
#Toast {
    background: rgba(30, 30, 30, 0.92);
    border-radius: 8px;
    padding: 10px 16px;
    color: #FFFFFF;
    font-size: 13px;
}
"""


def apply_tidy_style(app):
    """应用设计系统"""
    app.setStyleSheet(TIDY_QSS)
