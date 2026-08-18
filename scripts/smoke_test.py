"""Headless smoke tests for TidyUUUUp v1.1.2.

Run from the repository root:
    QT_QPA_PLATFORM=offscreen python scripts/smoke_test.py
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "v1.1.2"))

from PyQt6.QtWidgets import QApplication
from main import DesktopIndex, TidyDynamicIslandDock
from settings import UserSettings
from updater import CURRENT_VERSION, is_newer


def main() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        for name in ("brief.docx", "chart.png", "recording.mp4", "main.py", "bundle.zip", "notes.txt"):
            (root / name).write_text("test", encoding="utf-8")
        index = DesktopIndex(str(root))
        assert len(index.files) == 6, index.files
        assert {item["name"] for item in index.group_files("工作")} == {"brief.docx", "notes.txt"}
        assert {item["name"] for item in index.group_files("图片")} == {"chart.png"}
        assert {item["name"] for item in index.group_files("媒体")} == {"recording.mp4"}
        assert {item["name"] for item in index.group_files("代码")} == {"main.py"}
        assert index.search("brief")[0][1]["name"] == "brief.docx"

        app = QApplication.instance() or QApplication([])
        settings = UserSettings()
        settings.set("desktop_path", str(root))
        settings.set("dock_position", None)
        dock = TidyDynamicIslandDock(settings)
        assert dock.width() == dock.compact_width == 620
        assert hasattr(dock, "clock_widget") and hasattr(dock, "time_label")
        assert dock.layout().count() >= 7, "Classic layout must include logo, controls, folders, search and clock."
        dock.expand_search()
        assert dock.search_width_animation.endValue() == 360
        assert dock.width_animation.endValue() == dock.stretched_width
        dock.search_input.setText("main")
        dock.run_search()
        assert dock.popover.title.text() == "Search · main"
        assert dock.popover.items.count() == 1
        dock.close()
        settings.set("desktop_path", "")

    assert CURRENT_VERSION == "1.1.2"
    assert is_newer("1.1.3", "1.1.2")
    assert not is_newer("1.1.1", "1.1.2")
    print("TidyUUUUp v1.1.2 smoke tests passed")


if __name__ == "__main__":
    main()
