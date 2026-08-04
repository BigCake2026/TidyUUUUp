LIQUID_GLASS_QSS = """
* {
    font-family: "Segoe UI", "Microsoft YaHei", "PingFang SC", -apple-system, sans-serif;
}

QMainWindow, QWidget {
    background: transparent;
}

/* Liquid Glass 容器 - 磨砂玻璃效果 */
.LiquidGlass {
    background: rgba(30, 30, 40, 0.55);
    backdrop-filter: blur(40px) saturate(180%);
    -webkit-backdrop-filter: blur(40px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 20px;
}

.LiquidGlassPanel {
    background: rgba(40, 40, 55, 0.6);
    backdrop-filter: blur(30px) saturate(180%);
    -webkit-backdrop-filter: blur(30px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
}

.LiquidGlassCard {
    background: rgba(55, 55, 75, 0.5);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
}

.LiquidGlassCard:hover {
    background: rgba(70, 70, 95, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.15);
}

/* 底部 Dock 栏 */
#DockBar {
    background: rgba(25, 25, 35, 0.65);
    backdrop-filter: blur(50px) saturate(200%);
    -webkit-backdrop-filter: blur(50px) saturate(200%);
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    border-left: 1px solid rgba(255, 255, 255, 0.08);
    border-right: 1px solid rgba(255, 255, 255, 0.08);
    border-bottom: none;
    border-top-left-radius: 24px;
    border-top-right-radius: 24px;
}

#DockItem {
    background: transparent;
    border: none;
    border-radius: 14px;
    padding: 6px;
}

#DockItem:hover {
    background: rgba(255, 255, 255, 0.15);
}

#DockItem:pressed {
    background: rgba(255, 255, 255, 0.25);
}

/* 搜索框 */
#SearchBox {
    background: rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 8px 16px;
    color: white;
    font-size: 14px;
    selection-background-color: rgba(100, 150, 255, 0.4);
}

#SearchBox:focus {
    border: 1px solid rgba(100, 150, 255, 0.5);
    background: rgba(0, 0, 0, 0.4);
}

/* 按钮 */
QPushButton {
    background: rgba(100, 150, 255, 0.3);
    border: 1px solid rgba(100, 150, 255, 0.4);
    border-radius: 10px;
    padding: 8px 20px;
    color: white;
    font-size: 13px;
    font-weight: 500;
}

QPushButton:hover {
    background: rgba(120, 170, 255, 0.5);
    border: 1px solid rgba(120, 170, 255, 0.6);
}

QPushButton:pressed {
    background: rgba(80, 130, 235, 0.6);
}

QPushButton:disabled {
    background: rgba(100, 100, 120, 0.3);
    border: 1px solid rgba(100, 100, 120, 0.2);
    color: rgba(255, 255, 255, 0.4);
}

/* 次要按钮 */
#SecondaryButton {
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.15);
}

#SecondaryButton:hover {
    background: rgba(255, 255, 255, 0.2);
}

/* 危险按钮 */
#DangerButton {
    background: rgba(255, 80, 80, 0.3);
    border: 1px solid rgba(255, 80, 80, 0.4);
}

#DangerButton:hover {
    background: rgba(255, 100, 100, 0.5);
}

/* 成功按钮 */
#SuccessButton {
    background: rgba(80, 220, 120, 0.3);
    border: 1px solid rgba(80, 220, 120, 0.4);
}

#SuccessButton:hover {
    background: rgba(100, 240, 140, 0.5);
}

/* 标签 */
QLabel {
    color: white;
    font-size: 13px;
}

#TitleLabel {
    font-size: 24px;
    font-weight: 700;
    color: white;
}

#SubtitleLabel {
    font-size: 14px;
    color: rgba(255, 255, 255, 0.7);
}

#CategoryBadge {
    background: rgba(100, 150, 255, 0.3);
    border-radius: 6px;
    padding: 2px 8px;
    color: rgba(200, 220, 255, 0.95);
    font-size: 11px;
    font-weight: 500;
}

/* 列表 */
QListWidget {
    background: transparent;
    border: none;
    outline: none;
    color: white;
}

QListWidget::item {
    background: transparent;
    border-radius: 10px;
    padding: 8px;
    margin: 2px 0;
}

QListWidget::item:hover {
    background: rgba(255, 255, 255, 0.08);
}

QListWidget::item:selected {
    background: rgba(100, 150, 255, 0.35);
}

/* 滚动条 */
QScrollBar:vertical {
    background: transparent;
    width: 8px;
    margin: 0;
}

QScrollBar::handle:vertical {
    background: rgba(255, 255, 255, 0.2);
    border-radius: 4px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover {
    background: rgba(255, 255, 255, 0.35);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

QScrollBar:horizontal {
    background: transparent;
    height: 8px;
}

QScrollBar::handle:horizontal {
    background: rgba(255, 255, 255, 0.2);
    border-radius: 4px;
    min-width: 30px;
}

QScrollBar::handle:horizontal:hover {
    background: rgba(255, 255, 255, 0.35);
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0;
}

/* 进度条 */
QProgressBar {
    background: rgba(255, 255, 255, 0.1);
    border: none;
    border-radius: 6px;
    height: 8px;
    text-align: center;
}

QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 rgba(100, 200, 255, 0.9),
        stop:1 rgba(150, 100, 255, 0.9));
    border-radius: 6px;
}

/* 复选框 */
QCheckBox {
    color: white;
    spacing: 8px;
    font-size: 13px;
}

QCheckBox::indicator {
    width: 18px;
    height: 18px;
    border-radius: 5px;
    border: 1.5px solid rgba(255, 255, 255, 0.3);
    background: rgba(0, 0, 0, 0.2);
}

QCheckBox::indicator:checked {
    background: rgba(100, 150, 255, 0.9);
    border: 1.5px solid rgba(100, 150, 255, 1);
}

QCheckBox::indicator:hover {
    border: 1.5px solid rgba(255, 255, 255, 0.5);
}

/* 下拉框 */
QComboBox {
    background: rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 8px;
    padding: 6px 12px;
    color: white;
    font-size: 13px;
}

QComboBox:hover {
    border: 1px solid rgba(255, 255, 255, 0.25);
}

QComboBox::drop-down {
    border: none;
    width: 20px;
}

QComboBox QAbstractItemView {
    background: rgba(35, 35, 50, 0.95);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    color: white;
    selection-background-color: rgba(100, 150, 255, 0.4);
    padding: 4px;
    outline: none;
}

/* 分隔线 */
QFrame[frameShape="4"] {
    color: rgba(255, 255, 255, 0.1);
    max-height: 1px;
}

/* 动画提示 */
#Toast {
    background: rgba(30, 30, 45, 0.9);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    color: white;
    padding: 12px 20px;
    font-size: 13px;
}

/* 分类侧边栏 */
#CategorySidebar {
    background: rgba(30, 30, 45, 0.4);
    border-right: 1px solid rgba(255, 255, 255, 0.06);
}

#CategoryItem {
    background: transparent;
    border: none;
    border-radius: 10px;
    padding: 10px 14px;
    color: rgba(255, 255, 255, 0.75);
    text-align: left;
    font-size: 13px;
}

#CategoryItem:hover {
    background: rgba(255, 255, 255, 0.08);
    color: white;
}

#CategoryItem:checked {
    background: rgba(100, 150, 255, 0.35);
    color: white;
}

/* 状态栏 */
QStatusBar {
    background: transparent;
    color: rgba(255, 255, 255, 0.6);
    font-size: 12px;
}

/* Tab 组件 */
QTabWidget::pane {
    border: none;
    background: transparent;
}

QTabBar::tab {
    background: transparent;
    color: rgba(255, 255, 255, 0.6);
    padding: 10px 20px;
    border: none;
    border-bottom: 2px solid transparent;
    font-size: 13px;
    font-weight: 500;
}

QTabBar::tab:hover {
    color: rgba(255, 255, 255, 0.9);
}

QTabBar::tab:selected {
    color: white;
    border-bottom: 2px solid rgba(100, 150, 255, 0.9);
}
"""


def apply_liquid_glass(app):
    app.setStyleSheet(LIQUID_GLASS_QSS)
