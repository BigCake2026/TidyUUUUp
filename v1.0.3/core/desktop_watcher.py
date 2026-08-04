"""
桌面实时文件监控 - Desktop Watcher
监控桌面文件变化，1秒内自动分类归档
"""
import os
import time
import threading
from pathlib import Path
from PyQt5.QtCore import QObject, pyqtSignal
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from .smart_engine import SmartRuleEngine


class DesktopWatcher(QObject):
    """桌面文件监控器"""

    file_detected = pyqtSignal(str, str)  # filepath, zone
    file_moved = pyqtSignal(str, str)      # old_path, new_path
    organize_completed = pyqtSignal(dict)

    def __init__(self, smart_engine=None):
        super().__init__()
        self.engine = smart_engine or SmartRuleEngine()
        self.observer = None
        self._running = False
        self._pending_files = {}
        self._lock = threading.Lock()
        self._settle_time = 1.0  # 等待文件写入稳定的时间（秒）

        # 桌面路径
        self.desktop_path = self._get_desktop_path()

        # 归档根目录
        self.organize_root = os.path.join(self.desktop_path, "智能分类")

    def _get_desktop_path(self):
        """获取桌面路径"""
        home = os.path.expanduser('~')
        possible_paths = [
            os.path.join(home, 'Desktop'),
            os.path.join(home, '桌面'),
        ]
        # 检查 OneDrive 桌面
        onedrive = os.environ.get('OneDrive')
        if onedrive:
            possible_paths.insert(0, os.path.join(onedrive, 'Desktop'))

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return possible_paths[0]

    def start(self):
        """开始监控"""
        if self._running:
            return

        if not os.path.exists(self.desktop_path):
            return

        self._running = True

        # 创建事件处理器
        class Handler(FileSystemEventHandler):
            def __init__(self, watcher):
                self.watcher = watcher

            def on_created(self, event):
                if not event.is_directory:
                    self.watcher._on_file_created(event.src_path)

            def on_moved(self, event):
                if not event.is_directory:
                    # 如果是新文件移动到桌面
                    if self.watcher.desktop_path in event.dest_path:
                        self.watcher._on_file_created(event.dest_path)

        # 启动观察者
        self.observer = Observer()
        self.observer.schedule(Handler(self), self.desktop_path, recursive=False)
        self.observer.start()

        # 启动文件稳定检查线程
        self._checker_thread = threading.Thread(target=self._check_pending_files, daemon=True)
        self._checker_thread.start()

    def stop(self):
        """停止监控"""
        self._running = False
        if self.observer:
            self.observer.stop()
            self.observer.join()
            self.observer = None

    def _on_file_created(self, filepath):
        """文件创建事件"""
        # 忽略临时文件和我们自己创建的分类文件夹
        filename = os.path.basename(filepath)
        if filename.startswith('.') or filename.startswith('~$'):
            return
        if self.organize_root in filepath:
            return

        # 添加到待处理队列
        with self._lock:
            self._pending_files[filepath] = time.time()

    def _check_pending_files(self):
        """检查待处理文件，等待文件稳定后再分类"""
        while self._running:
            try:
                now = time.time()
                to_process = []

                with self._lock:
                    for filepath, create_time in list(self._pending_files.items()):
                        # 等待文件写入稳定
                        if now - create_time >= self._settle_time:
                            # 检查文件是否还在增长
                            try:
                                current_size = os.path.getsize(filepath)
                                time.sleep(0.2)
                                new_size = os.path.getsize(filepath)
                                if current_size == new_size:  # 文件大小稳定了
                                    to_process.append(filepath)
                                    del self._pending_files[filepath]
                            except (OSError, FileNotFoundError):
                                del self._pending_files[filepath]

                # 处理稳定的文件
                for filepath in to_process:
                    try:
                        self._process_file(filepath)
                    except Exception as e:
                        print(f"处理文件出错 {filepath}: {e}")

            except Exception as e:
                print(f"检查线程出错: {e}")

            time.sleep(0.3)

    def _process_file(self, filepath):
        """处理单个文件 - 分类并归档"""
        if not os.path.exists(filepath):
            return

        # 智能分类
        zone, confidence = self.engine.classify(filepath)

        if zone is None:
            # 无法分类的放到"其他"
            zone = "其他"

        # 通知
        self.file_detected.emit(filepath, zone)

        # 自动归档
        self._auto_organize(filepath, zone)

    def _auto_organize(self, filepath, zone):
        """自动将文件移动到对应分类文件夹"""
        try:
            filename = os.path.basename(filepath)

            # 目标文件夹
            target_dir = os.path.join(self.organize_root, zone)
            os.makedirs(target_dir, exist_ok=True)

            target_path = os.path.join(target_dir, filename)

            # 如果文件已在目标位置，跳过
            if os.path.abspath(filepath) == os.path.abspath(target_path):
                return

            # 处理重名
            if os.path.exists(target_path):
                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(os.path.join(target_dir, f"{base}_{counter}{ext}")):
                    counter += 1
                target_path = os.path.join(target_dir, f"{base}_{counter}{ext}")

            # 移动文件
            import shutil
            shutil.move(filepath, target_path)
            self.file_moved.emit(filepath, target_path)

        except Exception as e:
            print(f"归档文件失败 {filepath}: {e}")

    def organize_all(self):
        """整理桌面上所有现有的文件"""
        if not os.path.exists(self.desktop_path):
            return

        results = {
            'total': 0,
            'organized': {},
            'skipped': 0,
            'errors': []
        }

        try:
            for item in os.listdir(self.desktop_path):
                filepath = os.path.join(self.desktop_path, item)

                # 跳过文件夹、隐藏文件、快捷方式（可选）
                if os.path.isdir(filepath):
                    if self.organize_root in filepath:
                        continue
                    # 不自动移动文件夹，只分类
                    continue
                if item.startswith('.') or item.startswith('~$'):
                    results['skipped'] += 1
                    continue
                if item.endswith('.lnk'):  # 快捷方式
                    results['skipped'] += 1
                    continue

                results['total'] += 1

                try:
                    zone, confidence = self.engine.classify(filepath)
                    if zone is None:
                        zone = "其他"

                    if zone not in results['organized']:
                        results['organized'][zone] = []
                    results['organized'][zone].append(filepath)

                    # 自动归档
                    self._auto_organize(filepath, zone)

                except Exception as e:
                    results['errors'].append((filepath, str(e)))

        except Exception as e:
            results['errors'].append(('system', str(e)))

        self.organize_completed.emit(results)
        return results

    def get_zone_path(self, zone_name):
        """获取某个分类区域的文件夹路径"""
        return os.path.join(self.organize_root, zone_name)

    def ensure_zone_folders(self):
        """确保所有分类文件夹都存在"""
        zones = self.engine.get_all_zones()
        for zone_name in zones:
            zone_path = self.get_zone_path(zone_name)
            os.makedirs(zone_path, exist_ok=True)
        # "其他" 文件夹
        os.makedirs(self.get_zone_path("其他"), exist_ok=True)
