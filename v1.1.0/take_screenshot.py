"""Render a headless preview of the centered v1.1.0 Dock."""
from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QColor, QPainter, QPixmap
from PyQt6.QtWidgets import QApplication

from main import TidyDynamicIslandDock
from settings import UserSettings


def main() -> None:
    app = QApplication(sys.argv)
    app.setApplicationName("TidyUUUUp")
    settings = UserSettings()
    settings.set("dock_position", None)
    dock = TidyDynamicIslandDock(settings)
    dock.show()

    def capture() -> None:
        canvas = QPixmap(900, 240)
        canvas.fill(QColor("#15161C"))
        painter = QPainter(canvas)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        image = dock.grab()
        x = (canvas.width() - image.width()) // 2
        y = (canvas.height() - image.height()) // 2
        painter.drawPixmap(x, y, image)
        painter.end()
        destination = Path(__file__).resolve().parent / "screenshots" / "v1.1.0_centered_island.png"
        destination.parent.mkdir(exist_ok=True)
        canvas.save(str(destination))
        dock.close()
        app.quit()

    QTimer.singleShot(80, capture)
    app.exec()


if __name__ == "__main__":
    main()
