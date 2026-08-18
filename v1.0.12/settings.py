"""
TidyUUUUp - 用户设置与数据持久化

所有用户数据保存在用户专属目录（AppDataLocation），与程序代码目录完全分离，
因此版本更新（替换代码目录）永远不会影响用户数据。

存储位置（跨平台，与应用名/脚本名无关，跨版本稳定）：
  Windows: %APPDATA%\\TidyUUUUp\\settings.json
  macOS:   ~/Library/Application Support/TidyUUUUp/settings.json
  Linux:   ~/.local/share/TidyUUUUp/settings.json
"""
import os
import json
import time
from PyQt6.QtCore import QStandardPaths


DEFAULTS = {
    # 更新相关
    "auto_check_updates": True,        # 启动时自动检查更新
    "check_interval_hours": 24,        # 自动检查的最小间隔（小时）
    "last_check_timestamp": 0.0,       # 上次检查的 unix 时间戳
    "skip_version": "",                # 用户选择跳过的版本号
    "update_repo": "BigCake2026/TidyUUUUp",  # GitHub 检测更新的仓库
    # 界面相关
    "dock_position": None,             # [x, y] 拖动后的位置（None=居中底部）
    # 索引相关
    "desktop_path": "",                # 自定义桌面路径（空=自动检测）
}


class UserSettings:
    """线程不安全；请在 GUI 线程使用。"""

    def __init__(self):
        # 使用 GenericDataLocation（不含应用名后缀）+ 固定子目录 "TidyUUUUp"，
        # 确保路径与运行时应用名/脚本名无关，跨版本稳定（用户数据保留的关键）。
        base = QStandardPaths.writableLocation(
            QStandardPaths.StandardLocation.GenericDataLocation)
        if not base:
            base = os.path.join(os.path.expanduser("~"), ".local", "share")
        self._dir = os.path.join(base, "TidyUUUUp")
        self._path = os.path.join(self._dir, "settings.json")
        self._data = dict(DEFAULTS)
        self.load()

    @property
    def dir(self) -> str:
        return self._dir

    @property
    def path(self) -> str:
        return self._path

    def load(self) -> None:
        try:
            os.makedirs(self._dir, exist_ok=True)
            if os.path.isfile(self._path):
                with open(self._path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if isinstance(data, dict):
                    self._data.update(data)
        except Exception as e:
            print(f"[Settings] load failed: {e}")

    def save(self) -> None:
        try:
            os.makedirs(self._dir, exist_ok=True)
            with open(self._path, "w", encoding="utf-8") as f:
                json.dump(self._data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[Settings] save failed: {e}")

    def get(self, key, default=None):
        return self._data.get(key, default if default is not None else DEFAULTS.get(key))

    def set(self, key, value) -> None:
        self._data[key] = value
        self.save()

    def should_auto_check(self) -> bool:
        """是否到了该自动检查更新的时候（满足开关 + 间隔）。"""
        if not self.get("auto_check_updates"):
            return False
        interval = float(self.get("check_interval_hours", 24)) * 3600
        last = float(self.get("last_check_timestamp", 0))
        return (time.time() - last) >= interval

    def mark_checked(self) -> None:
        self.set("last_check_timestamp", time.time())

    def is_skipped(self, version: str) -> bool:
        return self.get("skip_version") == version
