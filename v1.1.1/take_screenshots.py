"""Render the v1.1.1 Dock in four representative states without a live desktop."""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QColor, QPainter, QPixmap
from PyQt6.QtWidgets import QApplication

from main import TidyDynamicIslandDock
from settings import UserSettings

APP_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = APP_DIR / "screenshots"
CANVAS_SIZE = (1000, 500)


def save_state(dock: TidyDynamicIslandDock, filename: str, with_popover: bool = False) -> None:
    """Compose real widget captures onto a neutral desktop-style background."""
    canvas = QPixmap(*CANVAS_SIZE)
    canvas.fill(QColor("#171821"))
    painter = QPainter(canvas)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)

    dock_image = dock.grab()
    dock_x = (canvas.width() - dock_image.width()) // 2
    dock_y = canvas.height() - dock_image.height() - 48
    painter.drawPixmap(dock_x, dock_y, dock_image)

    if with_popover and dock.popover.isVisible():
        popover_image = dock.popover.grab()
        popover_x = (canvas.width() - popover_image.width()) // 2
        popover_y = dock_y - popover_image.height() - 20
        painter.drawPixmap(popover_x, popover_y, popover_image)

    painter.end()
    canvas.save(str(OUTPUT_DIR / filename))


def main() -> None:
    app = QApplication(sys.argv)
    app.setApplicationName("TidyUUUUp")
    OUTPUT_DIR.mkdir(exist_ok=True)

    with tempfile.TemporaryDirectory() as temp_directory:
        desktop = Path(temp_directory)
        fixtures = {
            "项目报告.docx": "work",
            "预算.xlsx": "work",
            "设计稿.png": "image",
            "发布演示.mp4": "media",
            "main.py": "code",
            "tidy_config.json": "code",
        }
        for name, content in fixtures.items():
            (desktop / name).write_text(content, encoding="utf-8")

        settings = UserSettings()
        settings.set("desktop_path", str(desktop))
        settings.set("dock_position", None)
        dock = TidyDynamicIslandDock(settings)
        dock.show()
        app.processEvents()

        # 01: clean, centred default state.
        save_state(dock, "01_centered_compact.png")

        # 02: focused search state with the real animated target dimensions applied.
        dock.set_dock_width(dock.stretched_width)
        dock.search_input.setMaximumWidth(270)
        dock.search_input.setFocus()
        app.processEvents()
        save_state(dock, "02_search_focused.png")

        # 03: category popup with real local desktop index data.
        dock.open_group("工作")
        app.processEvents()
        save_state(dock, "03_work_files_popover.png", with_popover=True)

        # 04: search results popup with real indexed file matches.
        dock.search_input.setText("main")
        dock.run_search()
        app.processEvents()
        save_state(dock, "04_search_results.png", with_popover=True)

        dock.close()
        settings.set("desktop_path", "")
        settings.set("dock_position", None)

    print("Created v1.1.1 screenshot set")


if __name__ == "__main__":
    main()
