"""
撤销管理器 - Undo Manager
记录每次文件整理/移动操作，支持一键撤销
"""
import os
import json
import time
import shutil
from datetime import datetime
from PyQt5.QtCore import QObject, pyqtSignal


MAX_UNDO_RECORDS = 10


class UndoManager(QObject):
    """撤销管理器"""

    undo_record_added = pyqtSignal(int)   # 新增记录时发出（当前记录数）
    undo_performed = pyqtSignal(int, int)  # 撤销完成（恢复文件数，跳过数）

    def __init__(self):
        super().__init__()
        self.undo_dir = os.path.join(
            os.path.expanduser('~'), '.nexus_dock', 'undo_log'
        )
        os.makedirs(self.undo_dir, exist_ok=True)
        self.records = []
        self._load_records()

    def _get_record_file(self):
        return os.path.join(self.undo_dir, 'undo_records.json')

    def _load_records(self):
        try:
            record_file = self._get_record_file()
            if os.path.exists(record_file):
                with open(record_file, 'r', encoding='utf-8') as f:
                    self.records = json.load(f)
        except Exception:
            self.records = []

    def _save_records(self):
        try:
            record_file = self._get_record_file()
            with open(record_file, 'w', encoding='utf-8') as f:
                json.dump(self.records, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def add_record(self, source, target, action_type='move'):
        """
        记录一次文件移动操作
        source: 原路径
        target: 新路径
        action_type: 操作类型
        """
        if not os.path.exists(target):
            return

        record = {
            'id': int(time.time() * 1000),
            'timestamp': time.time(),
            'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'source': source,
            'target': target,
            'filename': os.path.basename(target),
            'action_type': action_type,
        }

        self.records.insert(0, record)

        # 只保留最近 MAX_UNDO_RECORDS 条
        if len(self.records) > MAX_UNDO_RECORDS:
            self.records = self.records[:MAX_UNDO_RECORDS]

        self._save_records()
        self.undo_record_added.emit(len(self.records))

    def add_batch_record(self, move_map, action_type='organize'):
        """
        批量记录（如一键整理桌面）
        move_map: dict {source: target}
        """
        if not move_map:
            return

        batch_id = int(time.time() * 1000)
        items = []
        for source, target in move_map.items():
            if os.path.exists(target):
                items.append({
                    'source': source,
                    'target': target,
                    'filename': os.path.basename(target),
                })

        if not items:
            return

        record = {
            'id': batch_id,
            'timestamp': time.time(),
            'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'action_type': action_type,
            'is_batch': True,
            'batch_count': len(items),
            'items': items,
        }

        self.records.insert(0, record)

        if len(self.records) > MAX_UNDO_RECORDS:
            self.records = self.records[:MAX_UNDO_RECORDS]

        self._save_records()
        self.undo_record_added.emit(len(self.records))

    def get_records(self):
        """获取所有撤销记录"""
        return list(self.records)

    def get_record_count(self):
        return len(self.records)

    def undo_record(self, record_id):
        """
        撤销指定记录
        返回 (成功恢复数, 跳过数)
        """
        record = None
        record_idx = -1
        for i, r in enumerate(self.records):
            if r['id'] == record_id:
                record = r
                record_idx = i
                break

        if not record:
            return 0, 0

        restored = 0
        skipped = 0

        if record.get('is_batch'):
            # 批量撤销
            for item in record.get('items', []):
                target = item.get('source')  # 原路径（撤销的目标）
                source = item.get('target')  # 当前路径（要移动回来）
                if self._restore_file(source, target):
                    restored += 1
                else:
                    skipped += 1
        else:
            # 单条撤销
            target = record.get('source')
            source = record.get('target')
            if self._restore_file(source, target):
                restored += 1
            else:
                skipped += 1

        # 移除已撤销的记录
        if record_idx >= 0:
            self.records.pop(record_idx)
            self._save_records()

        self.undo_performed.emit(restored, skipped)
        return restored, skipped

    def _restore_file(self, source, target):
        """
        将文件从 source 恢复到 target
        """
        try:
            if not os.path.exists(source):
                return False

            # 确保目标目录存在
            target_dir = os.path.dirname(target)
            os.makedirs(target_dir, exist_ok=True)

            # 处理重名
            final_target = target
            if os.path.exists(target) and os.path.abspath(source) != os.path.abspath(target):
                base, ext = os.path.splitext(target)
                counter = 1
                while os.path.exists(f"{base}_恢复{counter}{ext}"):
                    counter += 1
                final_target = f"{base}_恢复{counter}{ext}"

            # 移动回去
            shutil.move(source, final_target)
            return True
        except Exception:
            return False

    def clear_records(self):
        """清空所有撤销记录"""
        self.records = []
        self._save_records()
