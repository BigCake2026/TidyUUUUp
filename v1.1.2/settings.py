"""
TidyUUUUp - 用户设置与数据持久化

所有用户数据保存在用户专属目录（AppDataLocation），与程序代码目录完全分离。
Windows 安装程序仅替换应用目录，因此更新不会影响用户设置、桌面索引路径、
小岛位置或快捷方式记录。

存储位置（跨版本稳定）：
  Windows: %APPDATA%/TidyUUUUp/settings.json
  macOS:   ~/Library/Application Support/TidyUUUUp/settings.json
  Linux:   ~/.local/share/TidyUUUUp/settings.json
"""
import json
import os
import time

from PyQt6.QtCore import QStandardPaths


DEFAULTS = {
    # 更新检查不可关闭；仓库可由维护者在设置文件中迁移，但用户界面不暴露关闭项。
    "update_repo": "BigCake2026/TidyUUUUp",
    "last_check_timestamp": 0.0,
    # 界面相关
    "dock_position": None,
    # 索引相关
    "desktop_path": "",
    "shortcut_target": "",
}

# 早期版本可能保存这些键。加载时删除，避免旧偏好关闭新的强制检查逻辑。
LEGACY_UPDATE_KEYS = ("auto_check_updates", "check_interval_hours", "skip_version")


class UserSettings:
    """线程不安全；请在 GUI 线程使用。"""

    def __init__(self):
        base = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.GenericDataLocation)
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
                with open(self._path, "r", encoding="utf-8") as handle:
                    data = json.load(handle)
                if isinstance(data, dict):
                    self._data.update(data)
            changed = False
            for key in LEGACY_UPDATE_KEYS:
                if key in self._data:
                    self._data.pop(key, None)
                    changed = True
            if changed:
                self.save()
        except Exception as error:
            print(f"[Settings] load failed: {error}")

    def save(self) -> None:
        try:
            os.makedirs(self._dir, exist_ok=True)
            with open(self._path, "w", encoding="utf-8") as handle:
                json.dump(self._data, handle, ensure_ascii=False, indent=2)
        except Exception as error:
            print(f"[Settings] save failed: {error}")

    def get(self, key, default=None):
        return self._data.get(key, default if default is not None else DEFAULTS.get(key))

    def set(self, key, value) -> None:
        self._data[key] = value
        self.save()

    def should_auto_check(self) -> bool:
        """Update checking is mandatory and therefore runs at each application launch."""
        return True

    def mark_checked(self) -> None:
        self.set("last_check_timestamp", time.time())

    def is_skipped(self, version: str) -> bool:
        """Compatibility API: users can no longer suppress a release notification."""
        return False
