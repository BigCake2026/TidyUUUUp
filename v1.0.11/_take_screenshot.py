"""
v1.0.11 截图脚本（offscreen 平台）
不依赖 X11 实际显示，用 QWidget.grab() 渲染到 QPixmap
"""
import os
import sys
import time

os.environ['QT_QPA_PLATFORM'] = 'offscreen'

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt6.QtCore import Qt, QTimer, QPoint, QRect
from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtWidgets import QApplication

from main import TidyDynamicIslandDock, TopPopoverPanel


OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
os.makedirs(OUT_DIR, exist_ok=True)


def grab_widget(widget, name, scale=2):
    """截图单个 widget 并保存（可选 2x 高清）"""
    out = os.path.join(OUT_DIR, name)
    time.sleep(0.2)
    QApplication.processEvents()
    pix = widget.grab()
    if scale > 1:
        pix = pix.scaled(
            pix.width() * scale, pix.height() * scale,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
    pix.save(out)
    print(f"[截图] {out} ({pix.width()}x{pix.height()})")
    return out


def grab_full_desktop(dock, popover, name):
    """合成完整桌面截图：背景 + Dock + Popover"""
    out = os.path.join(OUT_DIR, name)
    W, H = 1440, 900
    time.sleep(0.2)
    QApplication.processEvents()

    canvas = QPixmap(W, H)
    canvas.fill(QColor(30, 30, 35))  # 深色桌面背景

    painter = QPainter(canvas)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)

    # 绘制桌面渐变
    from PyQt6.QtGui import QLinearGradient
    grad = QLinearGradient(0, 0, 0, H)
    grad.setColorAt(0.0, QColor(40, 40, 50))
    grad.setColorAt(1.0, QColor(20, 20, 25))
    painter.fillRect(0, 0, W, H, grad)

    # 绘制 Dock（居中底部）
    dock_pix = dock.grab()
    dx = (W - dock_pix.width()) // 2
    dy = H - dock_pix.height() - 24
    painter.drawPixmap(dx, dy, dock_pix)

    # 绘制 Popover（如果有）
    if popover and popover.isVisible():
        pop_pix = popover.grab()
        px = dx + 200  # 简单定位
        py = dy - pop_pix.height() - 12
        painter.drawPixmap(px, py, pop_pix)

    painter.end()
    canvas.save(out)
    print(f"[截图] {out} (全屏合成 {W}x{H})")
    return out


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    print("=== 创建 Dock ===")
    # 用一个临时"桌面"目录填充演示文件，让截图展示真实分类/搜索结果
    import tempfile
    demo_dir = os.path.join(tempfile.gettempdir(), "tidyuuuup_demo_desktop")
    os.makedirs(demo_dir, exist_ok=True)
    for name in [
        "Q3_Financial_Forecast.xlsx", "Tax_Invoice_2026.pdf", "Budget_Allocation.docx",
        "VisionOS_Design_Tokens.fig", "AppIcon_Master_v2.png", "UI_Guidelines.pdf",
        "tidyuuuup_dock.py", "native_bridge.cpp", "manifest.json",
        "Holiday_Clip.mp4", "Podcast_Ep07.mp3", "Release_Archive.zip",
        "meeting_notes.txt",
    ]:
        open(os.path.join(demo_dir, name), "w").close()

    dock = TidyDynamicIslandDock(desktop_path=demo_dir)
    dock.show()
    QApplication.processEvents()
    time.sleep(0.5)

    print("\n=== 截图 1: Dock 默认 compact 状态 ===")
    grab_widget(dock, "01_dock_compact.png", scale=2)

    print("\n=== 截图 2: 搜索框聚焦 → 弹簧拉伸 ===")
    dock.search_input.setFocus()
    dock.stretch()
    # 等待动画完成（直接设置最终宽度）
    dock.set_dock_width(dock.stretched_width)
    QApplication.processEvents()
    time.sleep(0.3)
    grab_widget(dock, "02_dock_stretched.png", scale=2)

    print("\n=== 截图 3: 搜索框输入文字 ===")
    dock.search_input.setText("financial")
    dock.on_search_text_changed("financial")
    QApplication.processEvents()
    time.sleep(0.3)
    grab_widget(dock, "03_dock_search_active.png", scale=2)

    print("\n=== 截图 4: 文件夹 Popover 弹出 ===")
    dock.search_input.clear()
    dock.search_input.clearFocus()
    dock.collapse()
    dock.set_dock_width(dock.compact_width)
    QApplication.processEvents()
    time.sleep(0.2)
    # 模拟点击文件夹
    global_pos = dock.mapToGlobal(dock.folders["Finance AI"].pos())
    dock.popover.show_folder_content(
        "Finance AI", global_pos,
        dock.index.files_for_folder("Finance AI"))
    QApplication.processEvents()
    time.sleep(0.3)
    grab_widget(dock.popover, "04_folder_popover.png", scale=2)

    print("\n=== 截图 5: 完整桌面合成 ===")
    grab_full_desktop(dock, dock.popover, "05_full_desktop.png")

    print("\n=== 截图 6: Dock + Popover 合成 ===")
    dock.popover.show_folder_content(
        "Code Engine", global_pos,
        dock.index.files_for_folder("Code Engine"))
    QApplication.processEvents()
    time.sleep(0.3)
    grab_full_desktop(dock, dock.popover, "06_dock_with_popover.png")

    print("\n✅ 所有截图完成！")
    print(f"保存目录: {OUT_DIR}")
    print("\n截图列表:")
    for f in sorted(os.listdir(OUT_DIR)):
        path = os.path.join(OUT_DIR, f)
        size = os.path.getsize(path) / 1024
        print(f"  {f} ({size:.1f} KB)")

    QTimer.singleShot(300, app.quit)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
