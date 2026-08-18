"""
v1.0.12 截图生成脚本（offscreen 平台）
用法：QT_QPA_PLATFORM=offscreen python _take_screenshot.py
"""
import os
import sys
import tempfile

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
os.environ.setdefault("XDG_DATA_HOME", "/tmp/tidyuuuup_shot_data")
sys.argv = ["main.py"]

import importlib.util
spec = importlib.util.spec_from_file_location("m", os.path.join(os.path.dirname(__file__), "main.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer, QEvent, Qt, QRect
from PyQt6.QtGui import QFocusEvent

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
os.makedirs(OUT, exist_ok=True)


def shot(widget, name, region=None, scale=2):
    pix = widget.grab() if region is None else widget.grab(QRect(*region))
    if scale and scale != 1:
        pix = pix.scaled(pix.width() * scale, pix.height() * scale,
                         Qt.AspectRatioMode.KeepAspectRatio,
                         Qt.TransformationMode.SmoothTransformation)
    path = os.path.join(OUT, name)
    pix.save(path, "PNG")
    print(f"[截图] {path} ({pix.width()}x{pix.height()})")


def main():
    # 搭建演示桌面
    demo = tempfile.mkdtemp(prefix="tidy_demo_")
    for n in ["Q3_Financial_Forecast.xlsx", "Tax_Invoice_2026.pdf",
              "Budget_Allocation.docx", "AppIcon_Master_v2.png",
              "VisionOS_Design_Tokens.fig", "tidyuuuup_dock.py",
              "native_bridge.cpp", "manifest.json", "Holiday_Clip.mp4",
              "Podcast_Ep07.mp3", "Release_Archive.zip", "meeting_notes.txt"]:
        open(os.path.join(demo, n), "w").close()

    settings = m.UserSettings()
    settings.set("auto_check_updates", False)  # 截图时不触发更新检查
    dock = m.TidyDynamicIslandDock(desktop_path=demo, settings=settings)
    dock.show()
    app = QApplication.instance()
    app.processEvents()

    # 1) compact
    dock.collapse()
    for _ in range(40):
        app.processEvents()
    shot(dock, "01_dock_compact.png", scale=2)

    # 2) stretched (FocusIn)
    dock.stretch()
    for _ in range(40):
        app.processEvents()
    shot(dock, "02_dock_stretched.png", scale=2)

    # 3) search active
    dock.search_input.setText("report")
    QTimer.singleShot(400, app.quit)
    app.exec()
    app2 = QApplication.instance()
    shot(dock, "03_dock_search_active.png", scale=2)
    if dock.popover.isVisible():
        shot(dock.popover, "03b_search_popover.png")

    # 4) folder popover
    dock.search_input.clear()
    dock.open_folder_popover("Finance AI")
    app.processEvents()
    shot(dock.popover, "04_folder_popover.png", scale=1)

    # 5) full dock composite (compact)
    dock.collapse(); dock.popover.hide()
    for _ in range(40):
        app.processEvents()
    shot(dock, "05_dock_full_compact.png", scale=2)

    print("✅ 截图完成")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main()
    sys.exit(0)
