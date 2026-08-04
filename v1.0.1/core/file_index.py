import os
import json
import time
import threading
from pathlib import Path
from datetime import datetime
from PyQt5.QtCore import QObject, pyqtSignal
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileIndex(QObject):
    index_updated = pyqtSignal()
    search_completed = pyqtSignal(list)

    FILE_CATEGORIES = {
        '图片': {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg', '.ico', '.tiff', '.raw', '.heic'},
        '视频': {'.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.mpg', '.mpeg'},
        '音频': {'.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.aiff', '.opus'},
        '文档': {'.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.docm', '.dotx'},
        '表格': {'.xls', '.xlsx', '.csv', '.ods', '.xlsm', '.xlsb'},
        '演示': {'.ppt', '.pptx', '.odp', '.pptm'},
        '压缩包': {'.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.iso'},
        '代码': {'.py', '.js', '.ts', '.html', '.css', '.java', '.cpp', '.c', '.h', '.go', '.rs', '.swift', '.kt', '.rb', '.php', '.vue', '.jsx', '.tsx'},
        '可执行': {'.exe', '.msi', '.bat', '.cmd', '.ps1', '.sh', '.apk', '.appimage'},
        '电子书': {'.epub', '.mobi', '.azw', '.azw3'},
        '字体': {'.ttf', '.otf', '.woff', '.woff2', '.eot'},
        '设计': {'.psd', '.ai', '.fig', '.sketch', '.xd', '.cdr'},
        '3D模型': {'.obj', '.fbx', '.blend', '.stl', '.3ds', '.max'},
        '数据': {'.json', '.xml', '.yaml', '.yml', '.sql', '.db', '.sqlite'},
        '垃圾缓存': {'.tmp', '.temp', '.log', '.crdownload', '.part', '.cache', '.bak', '.old'},
    }

    def __init__(self, db_path=None):
        super().__init__()
        if db_path is None:
            db_path = os.path.join(os.path.expanduser('~'), '.nexus_dock', 'file_index.json')
        self.db_path = db_path
        self.index = {}
        self.watchers = []
        self._lock = threading.Lock()
        self._load_index()

    def _load_index(self):
        try:
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            if os.path.exists(self.db_path):
                with open(self.db_path, 'r', encoding='utf-8') as f:
                    self.index = json.load(f)
        except Exception:
            self.index = {}

    def _save_index(self):
        try:
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            with open(self.db_path, 'w', encoding='utf-8') as f:
                json.dump(self.index, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def categorize_file(self, filepath):
        ext = os.path.splitext(filepath)[1].lower()
        for category, extensions in self.FILE_CATEGORIES.items():
            if ext in extensions:
                return category
        return '其他'

    def scan_directory(self, directory, recursive=True):
        directory = os.path.abspath(directory)
        if not os.path.exists(directory):
            return

        files_found = []
        try:
            if recursive:
                for root, dirs, files in os.walk(directory):
                    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in {'node_modules', '__pycache__', 'AppData'}]
                    for filename in files:
                        if filename.startswith('.'):
                            continue
                        filepath = os.path.join(root, filename)
                        files_found.append(filepath)
            else:
                for item in os.listdir(directory):
                    if item.startswith('.'):
                        continue
                    filepath = os.path.join(directory, item)
                    if os.path.isfile(filepath):
                        files_found.append(filepath)
        except PermissionError:
            pass

        with self._lock:
            for filepath in files_found:
                try:
                    stat = os.stat(filepath)
                    self.index[filepath] = {
                        'name': os.path.basename(filepath),
                        'path': filepath,
                        'size': stat.st_size,
                        'modified': stat.st_mtime,
                        'created': getattr(stat, 'st_ctime', stat.st_mtime),
                        'category': self.categorize_file(filepath),
                        'extension': os.path.splitext(filepath)[1].lower(),
                    }
                except (OSError, PermissionError):
                    continue

        self._save_index()
        self.index_updated.emit()

    def scan_default_locations(self):
        home = os.path.expanduser('~')
        locations = [
            os.path.join(home, 'Desktop'),
            os.path.join(home, 'Downloads'),
            os.path.join(home, 'Documents'),
            os.path.join(home, 'Pictures'),
            os.path.join(home, 'Videos'),
            os.path.join(home, 'Music'),
        ]
        for loc in locations:
            if os.path.exists(loc):
                self.scan_directory(loc, recursive=True)

    def search(self, query, category=None, limit=100):
        query = query.lower().strip()
        results = []

        with self._lock:
            for filepath, info in self.index.items():
                if category and info.get('category') != category:
                    continue
                if not query or query in info['name'].lower() or query in filepath.lower():
                    results.append(info)
                    if len(results) >= limit:
                        break

        results.sort(key=lambda x: x.get('modified', 0), reverse=True)
        self.search_completed.emit(results)
        return results

    def get_by_category(self, category):
        results = []
        with self._lock:
            for filepath, info in self.index.items():
                if info.get('category') == category:
                    results.append(info)
        results.sort(key=lambda x: x.get('modified', 0), reverse=True)
        return results

    def get_recent(self, limit=50):
        with self._lock:
            items = list(self.index.values())
        items.sort(key=lambda x: x.get('modified', 0), reverse=True)
        return items[:limit]

    def start_watching(self, directories):
        class Handler(FileSystemEventHandler):
            def __init__(self, indexer):
                self.indexer = indexer

            def on_created(self, event):
                if not event.is_directory:
                    self.indexer._add_to_index(event.src_path)

            def on_deleted(self, event):
                if not event.is_directory:
                    self.indexer._remove_from_index(event.src_path)

            def on_moved(self, event):
                if not event.is_directory:
                    self.indexer._remove_from_index(event.src_path)
                    self.indexer._add_to_index(event.dest_path)

        for directory in directories:
            if os.path.exists(directory):
                observer = Observer()
                observer.schedule(Handler(self), directory, recursive=True)
                observer.start()
                self.watchers.append(observer)

    def stop_watching(self):
        for observer in self.watchers:
            observer.stop()
            observer.join()
        self.watchers = []

    def _add_to_index(self, filepath):
        try:
            if not os.path.isfile(filepath):
                return
            stat = os.stat(filepath)
            with self._lock:
                self.index[filepath] = {
                    'name': os.path.basename(filepath),
                    'path': filepath,
                    'size': stat.st_size,
                    'modified': stat.st_mtime,
                    'created': getattr(stat, 'st_ctime', stat.st_mtime),
                    'category': self.categorize_file(filepath),
                    'extension': os.path.splitext(filepath)[1].lower(),
                }
            self._save_index()
            self.index_updated.emit()
        except (OSError, PermissionError):
            pass

    def _remove_from_index(self, filepath):
        with self._lock:
            if filepath in self.index:
                del self.index[filepath]
        self._save_index()
        self.index_updated.emit()

    def get_categories(self):
        return list(self.FILE_CATEGORIES.keys()) + ['其他']

    def get_stats(self):
        stats = {}
        with self._lock:
            for info in self.index.values():
                cat = info.get('category', '其他')
                if cat not in stats:
                    stats[cat] = {'count': 0, 'size': 0}
                stats[cat]['count'] += 1
                stats[cat]['size'] += info.get('size', 0)
        return stats

    def cleanup_missing(self):
        missing = []
        with self._lock:
            for filepath in list(self.index.keys()):
                if not os.path.exists(filepath):
                    missing.append(filepath)
                    del self.index[filepath]
        if missing:
            self._save_index()
            self.index_updated.emit()
        return len(missing)
