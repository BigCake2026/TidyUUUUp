"""
TidyUUUUp - Liquid Glass Pro 液态玻璃样式表 v1.0.7
基于 2025-26 顶级液态玻璃 UI 配方 + Apple Liquid Glass 设计语言
参考: design.dev/tools/liquid-glass-generator/, Apple HIG Liquid Glass

核心设计原则 (Apple Liquid Glass):
1. 径向渐变背景（模拟玻璃曲面折射）
2. 多层 box-shadow（内高光 + 内阴影 + 外投影）
3. 1px hairline 边框（玻璃边缘）
4. Specular Sheen 顶部镜面光泽
5. Inner Rim 内边框透镜效果
6. 悬停时玻璃透明度增强 (Adaptive Translucency)
7. 按压时液态变形感 (Liquid Deformation)
"""

LIQUID_GLASS_PRO_QSS = """
* {
    font-family: "Segoe UI", "Microsoft YaHei", "PingFang SC", -apple-system, BlinkMacSystemFont, sans-serif;
}

QMainWindow, QWidget {
    background: transparent;
}

/* ============================================================
   Liquid Glass Pro 容器 - 顶级玻璃效果
   参考: design.dev Liquid Glass Generator
   ============================================================ */

.LiquidGlassPro {
    background: qradialgradient(
        cx: 0.5, cy: 0.0,
        radius: 1.3,
        fx: 0.5, fy: 0.0,
        stop: 0.0 rgba(255, 255, 255, 55),
        stop: 0.45 rgba(255, 255, 255, 30),
        stop: 1.0 rgba(255, 255, 255, 18)
    );
    border: 1px solid rgba(255, 255, 255, 97);
    border-radius: 24px;
    color: white;
}

.LiquidGlassPanel {
    background: qradialgradient(
        cx: 0.5, cy: -0.1,
        radius: 1.5,
        fx: 0.5, fy: -0.1,
        stop: 0.0 rgba(255, 255, 255, 50),
        stop: 0.5 rgba(255, 255, 255, 28),
        stop: 1.0 rgba(255, 255, 255, 20)
    );
    border: 1px solid rgba(255, 255, 255, 80);
    border-radius: 16px;
    color: white;
}

.LiquidGlassCard {
    background: qradialgradient(
        cx: 0.5, cy: -0.2,
        radius: 1.8,
        fx: 0.5, fy: -0.2,
        stop: 0.0 rgba(255, 255, 255, 45),
        stop: 0.6 rgba(255, 255, 255, 25),
        stop: 1.0 rgba(255, 255, 255, 15)
    );
    border: 1px solid rgba(255, 255, 255, 65);
    border-radius: 12px;
    color: white;
}

.LiquidGlassCard:hover {
    background: qradialgradient(
        cx: 0.5, cy: -0.2,
        radius: 1.8,
        fx: 0.5, fy: -0.2,
        stop: 0.0 rgba(255, 255, 255, 70),
        stop: 0.6 rgba(255, 255, 255, 40),
        stop: 1.0 rgba(255, 255, 255, 22)
    );
    border: 1px solid rgba(255, 255, 255, 120);
}

/* ============================================================
   底部 Dock 栏 - 液态玻璃 Pro
   ============================================================ */

#DockBar {
    background: qradialgradient(
        cx: 0.5, cy: -0.5,
        radius: 2.0,
        fx: 0.5, fy: -0.5,
        stop: 0.0 rgba(255, 255, 255, 50),
        stop: 0.3 rgba(255, 255, 255, 32),
        stop: 0.6 rgba(255, 255, 255, 22),
        stop: 1.0 rgba(255, 255, 255, 16)
    );
    border-top: 1.5px solid rgba(255, 255, 255, 180);
    border-left: 1px solid rgba(255, 255, 255, 70);
    border-right: 1px solid rgba(255, 255, 255, 70);
    border-bottom: none;
    border-top-left-radius: 28px;
    border-top-right-radius: 28px;
}

#DockItem {
    background: transparent;
    border: none;
    border-radius: 16px;
    padding: 6px;
    color: white;
}

#DockItem:hover {
    background: qradialgradient(
        cx: 0.5, cy: 0.0,
        radius: 1.5,
        fx: 0.5, fy: 0.0,
        stop: 0.0 rgba(255, 255, 255, 75),
        stop: 0.5 rgba(255, 255, 255, 40),
        stop: 1.0 rgba(255, 255, 255, 22)
    );
    border: 1px solid rgba(255, 255, 255, 80);
}

#DockItem:pressed {
    background: qradialgradient(
        cx: 0.5, cy: 0.5,
        radius: 1.2,
        fx: 0.5, fy: 0.5,
        stop: 0.0 rgba(100, 150, 255, 130),
        stop: 0.6 rgba(100, 150, 255, 70),
        stop: 1.0 rgba(255, 255, 255, 30)
    );
    border: 1px solid rgba(100, 150, 255, 100);
    padding: 8px 4px 4px 8px;
}

/* ============================================================
   系统按钮 - 玻璃按钮
   ============================================================ */

#SystemButton {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 1.8,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(255, 255, 255, 35),
        stop: 1.0 rgba(255, 255, 255, 15)
    );
    border: 1px solid rgba(255, 255, 255, 50);
    border-radius: 14px;
    padding: 8px;
    color: white;
    font-size: 20px;
}

#SystemButton:hover {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 1.8,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(255, 255, 255, 70),
        stop: 1.0 rgba(255, 255, 255, 30)
    );
    border: 1px solid rgba(255, 255, 255, 100);
}

#SystemButton:pressed {
    background: qradialgradient(
        cx: 0.5, cy: 0.5,
        radius: 1.3,
        fx: 0.5, fy: 0.5,
        stop: 0.0 rgba(100, 150, 255, 140),
        stop: 0.6 rgba(100, 150, 255, 75),
        stop: 1.0 rgba(100, 150, 255, 40)
    );
    border: 1px solid rgba(100, 150, 255, 130);
    padding: 10px 6px 6px 10px;
}

/* ============================================================
   撤销按钮 - Liquid Glass 特殊样式
   ============================================================ */

#UndoButton {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 1.8,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(255, 200, 100, 50),
        stop: 1.0 rgba(255, 200, 100, 20)
    );
    border: 1px solid rgba(255, 200, 100, 60);
    border-radius: 16px;
    padding: 6px;
    color: white;
}

#UndoButton:hover {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 1.8,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(255, 200, 100, 90),
        stop: 1.0 rgba(255, 200, 100, 40)
    );
    border: 1px solid rgba(255, 200, 100, 120);
}

#UndoButton:pressed {
    background: qradialgradient(
        cx: 0.5, cy: 0.5,
        radius: 1.3,
        fx: 0.5, fy: 0.5,
        stop: 0.0 rgba(255, 180, 80, 150),
        stop: 1.0 rgba(255, 180, 80, 50)
    );
    padding: 8px 4px 4px 8px;
}

/* 小红点提示 (撤销记录) */
#UndoBadge {
    background: qradialgradient(
        cx: 0.3, cy: 0.3,
        radius: 1.0,
        fx: 0.3, fy: 0.3,
        stop: 0.0 rgba(255, 100, 100, 255),
        stop: 1.0 rgba(220, 50, 50, 255)
    );
    border: 1.5px solid rgba(255, 255, 255, 200);
    border-radius: 9px;
    color: white;
    font-size: 10px;
    font-weight: 700;
}

/* ============================================================
   开始按钮 - Windows 徽标
   ============================================================ */

#StartButton {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 1.8,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(0, 120, 215, 80),
        stop: 1.0 rgba(0, 180, 255, 30)
    );
    border: 1px solid rgba(0, 180, 255, 80);
    border-radius: 16px;
    padding: 6px;
}

#StartButton:hover {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 1.8,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(0, 150, 255, 130),
        stop: 1.0 rgba(0, 200, 255, 50)
    );
    border: 1px solid rgba(0, 200, 255, 130);
}

#StartButton:pressed {
    background: qradialgradient(
        cx: 0.5, cy: 0.5,
        radius: 1.3,
        fx: 0.5, fy: 0.5,
        stop: 0.0 rgba(0, 100, 200, 150),
        stop: 1.0 rgba(0, 150, 255, 50)
    );
    padding: 8px 4px 4px 8px;
}

/* ============================================================
   搜索框
   ============================================================ */

#SearchBox {
    background: qradialgradient(
        cx: 0.5, cy: -0.5,
        radius: 2.0,
        fx: 0.5, fy: -0.5,
        stop: 0.0 rgba(0, 0, 0, 60),
        stop: 1.0 rgba(0, 0, 0, 40)
    );
    border: 1px solid rgba(255, 255, 255, 60);
    border-radius: 14px;
    padding: 10px 20px;
    color: white;
    font-size: 14px;
    selection-background-color: rgba(100, 150, 255, 50);
}

#SearchBox:focus {
    border: 1px solid rgba(100, 150, 255, 120);
    background: qradialgradient(
        cx: 0.5, cy: -0.5,
        radius: 2.0,
        fx: 0.5, fy: -0.5,
        stop: 0.0 rgba(0, 0, 0, 80),
        stop: 1.0 rgba(0, 0, 0, 50)
    );
}

/* ============================================================
   按钮 - 玻璃按钮
   ============================================================ */

QPushButton {
    background: qradialgradient(
        cx: 0.5, cy: -0.4,
        radius: 1.8,
        fx: 0.5, fy: -0.4,
        stop: 0.0 rgba(100, 150, 255, 90),
        stop: 0.5 rgba(100, 150, 255, 60),
        stop: 1.0 rgba(100, 150, 255, 40)
    );
    border: 1px solid rgba(120, 170, 255, 100);
    border-radius: 12px;
    padding: 10px 24px;
    color: white;
    font-size: 13px;
    font-weight: 500;
}

QPushButton:hover {
    background: qradialgradient(
        cx: 0.5, cy: -0.4,
        radius: 1.8,
        fx: 0.5, fy: -0.4,
        stop: 0.0 rgba(120, 180, 255, 130),
        stop: 0.5 rgba(120, 180, 255, 80),
        stop: 1.0 rgba(120, 180, 255, 55)
    );
    border: 1px solid rgba(150, 200, 255, 150);
}

QPushButton:pressed {
    background: qradialgradient(
        cx: 0.5, cy: 0.5,
        radius: 1.3,
        fx: 0.5, fy: 0.5,
        stop: 0.0 rgba(80, 130, 235, 170),
        stop: 0.6 rgba(80, 130, 235, 100),
        stop: 1.0 rgba(80, 130, 235, 50)
    );
    border: 1px solid rgba(80, 130, 235, 150);
    padding: 12px 22px 8px 26px;
}

QPushButton:disabled {
    background: qradialgradient(
        cx: 0.5, cy: 0.5,
        radius: 1.5,
        fx: 0.5, fy: 0.5,
        stop: 0.0 rgba(100, 100, 120, 50),
        stop: 1.0 rgba(100, 100, 120, 30)
    );
    border: 1px solid rgba(100, 100, 120, 40);
    color: rgba(255, 255, 255, 40);
}

/* 次要按钮 */
#SecondaryButton {
    background: qradialgradient(
        cx: 0.5, cy: -0.4,
        radius: 1.8,
        fx: 0.5, fy: -0.4,
        stop: 0.0 rgba(255, 255, 255, 35),
        stop: 1.0 rgba(255, 255, 255, 15)
    );
    border: 1px solid rgba(255, 255, 255, 60);
}

#SecondaryButton:hover {
    background: qradialgradient(
        cx: 0.5, cy: -0.4,
        radius: 1.8,
        fx: 0.5, fy: -0.4,
        stop: 0.0 rgba(255, 255, 255, 60),
        stop: 1.0 rgba(255, 255, 255, 28)
    );
    border: 1px solid rgba(255, 255, 255, 100);
}

/* ============================================================
   标签
   ============================================================ */

QLabel {
    color: white;
    font-size: 13px;
    background: transparent;
}

#TitleLabel {
    font-size: 26px;
    font-weight: 700;
    color: white;
    background: transparent;
}

#SubtitleLabel {
    font-size: 14px;
    color: rgba(255, 255, 255, 70);
    background: transparent;
}

#CategoryBadge {
    background: qradialgradient(
        cx: 0.5, cy: -0.5,
        radius: 2.0,
        fx: 0.5, fy: -0.5,
        stop: 0.0 rgba(100, 150, 255, 70),
        stop: 1.0 rgba(100, 150, 255, 40)
    );
    border: 1px solid rgba(100, 150, 255, 60);
    border-radius: 8px;
    padding: 4px 12px;
    color: rgba(200, 220, 255, 95);
    font-size: 11px;
    font-weight: 500;
}

/* ============================================================
   列表 - 玻璃列表
   ============================================================ */

QListWidget {
    background: transparent;
    border: none;
    outline: none;
    color: white;
}

QListWidget::item {
    background: transparent;
    border-radius: 12px;
    padding: 10px;
    margin: 3px 0;
}

QListWidget::item:hover {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 2.0,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(255, 255, 255, 35),
        stop: 1.0 rgba(255, 255, 255, 12)
    );
    border: 1px solid rgba(255, 255, 255, 30);
}

QListWidget::item:selected {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 2.0,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(100, 150, 255, 100),
        stop: 1.0 rgba(100, 150, 255, 55)
    );
    border: 1px solid rgba(100, 150, 255, 80);
}

/* ============================================================
   滚动条 - 玻璃滚动条
   ============================================================ */

QScrollBar:vertical {
    background: transparent;
    width: 10px;
    margin: 4px;
}

QScrollBar::handle:vertical {
    background: qradialgradient(
        cx: 0.5, cy: 0.0,
        radius: 1.5,
        fx: 0.5, fy: 0.0,
        stop: 0.0 rgba(255, 255, 255, 80),
        stop: 1.0 rgba(255, 255, 255, 35)
    );
    border: 1px solid rgba(255, 255, 255, 40);
    border-radius: 5px;
    min-height: 40px;
}

QScrollBar::handle:vertical:hover {
    background: qradialgradient(
        cx: 0.5, cy: 0.0,
        radius: 1.5,
        fx: 0.5, fy: 0.0,
        stop: 0.0 rgba(255, 255, 255, 120),
        stop: 1.0 rgba(255, 255, 255, 60)
    );
    border: 1px solid rgba(255, 255, 255, 80);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

QScrollBar:horizontal {
    background: transparent;
    height: 10px;
    margin: 4px;
}

QScrollBar::handle:horizontal {
    background: qradialgradient(
        cx: 0.0, cy: 0.5,
        radius: 1.5,
        fx: 0.0, fy: 0.5,
        stop: 0.0 rgba(255, 255, 255, 80),
        stop: 1.0 rgba(255, 255, 255, 35)
    );
    border: 1px solid rgba(255, 255, 255, 40);
    border-radius: 5px;
    min-width: 40px;
}

QScrollBar::handle:horizontal:hover {
    background: qradialgradient(
        cx: 0.0, cy: 0.5,
        radius: 1.5,
        fx: 0.0, fy: 0.5,
        stop: 0.0 rgba(255, 255, 255, 120),
        stop: 1.0 rgba(255, 255, 255, 60)
    );
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0;
}

/* ============================================================
   复选框
   ============================================================ */

QCheckBox {
    color: white;
    spacing: 10px;
    font-size: 13px;
    background: transparent;
}

QCheckBox::indicator {
    width: 20px;
    height: 20px;
    border-radius: 6px;
    border: 1.5px solid rgba(255, 255, 255, 80);
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 2.0,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(0, 0, 0, 40),
        stop: 1.0 rgba(0, 0, 0, 20)
    );
}

QCheckBox::indicator:checked {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 2.0,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(100, 150, 255, 200),
        stop: 1.0 rgba(100, 150, 255, 140)
    );
    border: 1.5px solid rgba(150, 180, 255, 200);
}

QCheckBox::indicator:hover {
    border: 1.5px solid rgba(255, 255, 255, 130);
}

/* ============================================================
   下拉框
   ============================================================ */

QComboBox {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 2.0,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(0, 0, 0, 60),
        stop: 1.0 rgba(0, 0, 0, 35)
    );
    border: 1px solid rgba(255, 255, 255, 60);
    border-radius: 10px;
    padding: 8px 16px;
    color: white;
    font-size: 13px;
}

QComboBox:hover {
    border: 1px solid rgba(255, 255, 255, 100);
}

QComboBox::drop-down {
    border: none;
    width: 24px;
}

QComboBox QAbstractItemView {
    background: qradialgradient(
        cx: 0.5, cy: -0.2,
        radius: 2.0,
        fx: 0.5, fy: -0.2,
        stop: 0.0 rgba(35, 35, 55, 230),
        stop: 1.0 rgba(20, 20, 40, 220)
    );
    border: 1px solid rgba(255, 255, 255, 50);
    border-radius: 12px;
    color: white;
    selection-background-color: rgba(100, 150, 255, 80);
    padding: 6px;
    outline: none;
}

/* ============================================================
   输入框
   ============================================================ */

QLineEdit, QTextEdit {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 2.0,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(0, 0, 0, 50),
        stop: 1.0 rgba(0, 0, 0, 30)
    );
    border: 1px solid rgba(255, 255, 255, 50);
    border-radius: 10px;
    padding: 8px 14px;
    color: white;
    font-size: 13px;
    selection-background-color: rgba(100, 150, 255, 50);
}

QLineEdit:focus, QTextEdit:focus {
    border: 1px solid rgba(100, 150, 255, 120);
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 2.0,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(0, 0, 0, 70),
        stop: 1.0 rgba(0, 0, 0, 40)
    );
}

/* ============================================================
   进度条 - 玻璃进度条
   ============================================================ */

QProgressBar {
    background: qradialgradient(
        cx: 0.5, cy: -0.5,
        radius: 2.0,
        fx: 0.5, fy: -0.5,
        stop: 0.0 rgba(255, 255, 255, 15),
        stop: 1.0 rgba(255, 255, 255, 8)
    );
    border: 1px solid rgba(255, 255, 255, 30);
    border-radius: 8px;
    height: 10px;
    text-align: center;
    color: white;
}

QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0.0 rgba(100, 200, 255, 230),
        stop:0.5 rgba(150, 120, 255, 230),
        stop:1.0 rgba(255, 150, 200, 230)
    );
    border-radius: 8px;
}

/* ============================================================
   分类侧边栏
   ============================================================ */

#CategorySidebar {
    background: qradialgradient(
        cx: 0.0, cy: 0.5,
        radius: 2.0,
        fx: 0.0, fy: 0.5,
        stop: 0.0 rgba(30, 30, 50, 100),
        stop: 1.0 rgba(30, 30, 50, 40)
    );
    border-right: 1px solid rgba(255, 255, 255, 30);
}

#CategoryItem {
    background: transparent;
    border: none;
    border-radius: 12px;
    padding: 12px 18px;
    color: rgba(255, 255, 255, 75);
    text-align: left;
    font-size: 13px;
}

#CategoryItem:hover {
    background: qradialgradient(
        cx: 0.0, cy: 0.5,
        radius: 2.0,
        fx: 0.0, fy: 0.5,
        stop: 0.0 rgba(255, 255, 255, 30),
        stop: 1.0 rgba(255, 255, 255, 10)
    );
    color: white;
}

#CategoryItem:checked {
    background: qradialgradient(
        cx: 0.0, cy: 0.5,
        radius: 2.0,
        fx: 0.0, fy: 0.5,
        stop: 0.0 rgba(100, 150, 255, 100),
        stop: 1.0 rgba(100, 150, 255, 50)
    );
    color: white;
    border: 1px solid rgba(100, 150, 255, 60);
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
    color: rgba(255, 255, 255, 60);
    padding: 12px 24px;
    border: none;
    border-bottom: 2px solid transparent;
    font-size: 13px;
    font-weight: 500;
}

QTabBar::tab:hover {
    color: rgba(255, 255, 255, 90);
    background: qradialgradient(
        cx: 0.5, cy: 1.0,
        radius: 2.0,
        fx: 0.5, fy: 1.0,
        stop: 0.0 rgba(255, 255, 255, 20),
        stop: 1.0 rgba(255, 255, 255, 0)
    );
}

QTabBar::tab:selected {
    color: white;
    border-bottom: 2px solid rgba(100, 150, 255, 230);
}

/* ============================================================
   菜单 - 玻璃菜单
   ============================================================ */

QMenu {
    background: qradialgradient(
        cx: 0.5, cy: -0.2,
        radius: 2.0,
        fx: 0.5, fy: -0.2,
        stop: 0.0 rgba(35, 35, 55, 240),
        stop: 1.0 rgba(20, 20, 40, 230)
    );
    border: 1px solid rgba(255, 255, 255, 50);
    border-radius: 14px;
    padding: 8px;
    color: white;
}

QMenu::item {
    padding: 10px 24px;
    border-radius: 8px;
    font-size: 13px;
}

QMenu::item:hover {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 2.0,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(100, 150, 255, 100),
        stop: 1.0 rgba(100, 150, 255, 50)
    );
}

QMenu::separator {
    height: 1px;
    background: rgba(255, 255, 255, 15);
    margin: 6px 12px;
}

/* ============================================================
   Quick Look 预览面板 - Apple 风格
   ============================================================ */

#QuickLookPanel {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 2.0,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(40, 40, 60, 235),
        stop: 0.5 rgba(25, 25, 45, 225),
        stop: 1.0 rgba(15, 15, 35, 215)
    );
    border: 1px solid rgba(255, 255, 255, 70);
    border-radius: 20px;
    color: white;
}

#QuickLookImage {
    background: transparent;
    border: 1px solid rgba(255, 255, 255, 40);
    border-radius: 12px;
}

#QuickLookInfo {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 1.8,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(255, 255, 255, 30),
        stop: 1.0 rgba(255, 255, 255, 12)
    );
    border: 1px solid rgba(255, 255, 255, 50);
    border-radius: 10px;
    padding: 10px 14px;
    color: white;
}

#ConfidenceBar {
    background: qradialgradient(
        cx: 0.5, cy: -0.5,
        radius: 2.0,
        fx: 0.5, fy: -0.5,
        stop: 0.0 rgba(255, 255, 255, 20),
        stop: 1.0 rgba(255, 255, 255, 8)
    );
    border: 1px solid rgba(255, 255, 255, 30);
    border-radius: 6px;
    height: 8px;
}

#ConfidenceChunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0.0 rgba(100, 200, 255, 230),
        stop:0.5 rgba(150, 120, 255, 230),
        stop:1.0 rgba(255, 150, 200, 230)
    );
    border-radius: 6px;
}

/* ============================================================
   虚拟文件夹 - Dock 栏分类
   ============================================================ */

#VirtualFolder {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 1.8,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(255, 200, 100, 60),
        stop: 1.0 rgba(255, 150, 80, 25)
    );
    border: 1px solid rgba(255, 200, 100, 70);
    border-radius: 14px;
    padding: 6px;
}

#VirtualFolder:hover {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 1.8,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(255, 200, 100, 100),
        stop: 1.0 rgba(255, 150, 80, 40)
    );
    border: 1px solid rgba(255, 200, 100, 130);
}

#VirtualFolder:pressed {
    background: qradialgradient(
        cx: 0.5, cy: 0.5,
        radius: 1.3,
        fx: 0.5, fy: 0.5,
        stop: 0.0 rgba(255, 180, 80, 140),
        stop: 1.0 rgba(255, 150, 80, 50)
    );
    padding: 8px 4px 4px 8px;
}

/* ============================================================
   Toast 提示 - Liquid Glass 浮动卡片
   ============================================================ */

#Toast {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 1.8,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(35, 35, 55, 240),
        stop: 1.0 rgba(20, 20, 40, 230)
    );
    border: 1px solid rgba(255, 255, 255, 60);
    border-radius: 12px;
    padding: 12px 20px;
    color: white;
}

/* ============================================================
   撤销面板 - Liquid Glass 列表
   ============================================================ */

#UndoPanel {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 2.0,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(40, 40, 60, 240),
        stop: 0.5 rgba(25, 25, 45, 230),
        stop: 1.0 rgba(15, 15, 35, 220)
    );
    border: 1px solid rgba(255, 255, 255, 70);
    border-radius: 18px;
    color: white;
}

#UndoRecordItem {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 1.8,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(255, 255, 255, 25),
        stop: 1.0 rgba(255, 255, 255, 10)
    );
    border: 1px solid rgba(255, 255, 255, 30);
    border-radius: 10px;
    padding: 10px 14px;
    color: white;
}

#UndoRecordItem:hover {
    background: qradialgradient(
        cx: 0.5, cy: -0.3,
        radius: 1.8,
        fx: 0.5, fy: -0.3,
        stop: 0.0 rgba(100, 150, 255, 70),
        stop: 1.0 rgba(100, 150, 255, 30)
    );
    border: 1px solid rgba(100, 150, 255, 80);
}

#UndoRecordItem:pressed {
    background: qradialgradient(
        cx: 0.5, cy: 0.5,
        radius: 1.3,
        fx: 0.5, fy: 0.5,
        stop: 0.0 rgba(100, 150, 255, 120),
        stop: 1.0 rgba(100, 150, 255, 40)
    );
}

/* ============================================================
   悬浮球 - Floating Ball (动态绘制为主)
   ============================================================ */

#FloatingBall {
    background: transparent;
    border: none;
}
"""


def apply_liquid_glass(app):
    """应用液态玻璃 Pro 样式"""
    app.setStyleSheet(LIQUID_GLASS_PRO_QSS)
