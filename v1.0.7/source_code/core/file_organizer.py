import os
import shutil
import hashlib
import threading
from pathlib import Path
from datetime import datetime
from PyQt5.QtCore import QObject, pyqtSignal
from send2trash import send2trash


class FileOrganizer(QObject):
    progress = pyqtSignal(int, int, str)
    completed = pyqtSignal(dict)
    error = pyqtSignal(str)

    def __init__(self, file_index=None):
        super().__init__()
        self.file_index = file_index
        self._cancel = False

    def cancel(self):
        self._cancel = True

    def organize_directory(self, source_dir, target_dir=None, strategy='category', use_subfolders=True, dry_run=False):
        self._cancel = False
        source_dir = os.path.abspath(source_dir)

        if target_dir is None:
            target_dir = source_dir
        target_dir = os.path.abspath(target_dir)

        if not os.path.exists(source_dir):
            self.error.emit(f"源目录不存在: {source_dir}")
            return

        results = {
            'moved': [],
            'skipped': [],
            'errors': [],
            'duplicates': [],
            'total_files': 0,
            'organized_count': 0,
        }

        # 收集所有文件
        all_files = []
        for root, dirs, files in os.walk(source_dir):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for filename in files:
                if filename.startswith('.'):
                    continue
                filepath = os.path.join(root, filename)
                # 跳过目标目录中的文件
                if target_dir in filepath and source_dir != target_dir:
                    continue
                all_files.append(filepath)

        results['total_files'] = len(all_files)

        if not all_files:
            self.completed.emit(results)
            return

        date_str = datetime.now().strftime('%Y-%m-%d')

        for i, filepath in enumerate(all_files):
            if self._cancel:
                break

            self.progress.emit(i + 1, len(all_files), f"处理: {os.path.basename(filepath)}")

            try:
                filename = os.path.basename(filepath)
                category = self._categorize(filepath)

                if strategy == 'category':
                    dest_folder = os.path.join(target_dir, category)
                elif strategy == 'date':
                    mtime = os.path.getmtime(filepath)
                    file_date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
                    dest_folder = os.path.join(target_dir, file_date)
                elif strategy == 'extension':
                    ext = os.path.splitext(filepath)[1].lower() or '无扩展名'
                    dest_folder = os.path.join(target_dir, ext)
                else:
                    dest_folder = target_dir

                if use_subfolders and date_str not in dest_folder:
                    dest_folder = os.path.join(dest_folder, date_str)

                dest_path = os.path.join(dest_folder, filename)

                # 如果文件已在目标位置，跳过
                if os.path.abspath(filepath) == os.path.abspath(dest_path):
                    results['skipped'].append(filepath)
                    continue

                # 处理重名
                if os.path.exists(dest_path):
                    # 检查是否是重复文件
                    if self._files_are_same(filepath, dest_path):
                        results['duplicates'].append((filepath, dest_path))
                        continue
                    else:
                        base, ext = os.path.splitext(filename)
                        counter = 1
                        while os.path.exists(os.path.join(dest_folder, f"{base}_{counter}{ext}")):
                            counter += 1
                        dest_path = os.path.join(dest_folder, f"{base}_{counter}{ext}")

                if not dry_run:
                    try:
                        os.makedirs(dest_folder, exist_ok=True)
                    except OSError as e:
                        results['errors'].append((filepath, f"无法创建目标目录: {e}"))
                        continue
                    try:
                        shutil.move(filepath, dest_path)
                    except Exception as e:
                        results['errors'].append((filepath, f"移动文件失败: {e}"))
                        continue

                results['moved'].append((filepath, dest_path))
                results['organized_count'] += 1

            except Exception as e:
                results['errors'].append((filepath, str(e)))

        self.progress.emit(len(all_files), len(all_files), "完成")
        self.completed.emit(results)

    def find_duplicate_images(self, directory):
        self._cancel = False
        directory = os.path.abspath(directory)

        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}
        images = []

        for root, dirs, files in os.walk(directory):
            for filename in files:
                ext = os.path.splitext(filename)[1].lower()
                if ext in image_extensions:
                    images.append(os.path.join(root, filename))

        results = {
            'duplicates': [],
            'total_scanned': len(images),
            'groups': 0,
        }

        if not images:
            self.completed.emit(results)
            return

        # 按大小分组
        size_groups = {}
        for i, img_path in enumerate(images):
            if self._cancel:
                break
            try:
                size = os.path.getsize(img_path)
                if size not in size_groups:
                    size_groups[size] = []
                size_groups[size].append(img_path)
            except OSError:
                pass

            self.progress.emit(i + 1, len(images), f"扫描: {os.path.basename(img_path)}")

        # 对相同大小的文件比较内容哈希
        for size, paths in size_groups.items():
            if len(paths) < 2:
                continue

            hash_groups = {}
            for path in paths:
                try:
                    file_hash = self._hash_file(path)
                    if file_hash not in hash_groups:
                        hash_groups[file_hash] = []
                    hash_groups[file_hash].append(path)
                except OSError:
                    pass

            for file_hash, group in hash_groups.items():
                if len(group) > 1:
                    results['duplicates'].append(group)
                    results['groups'] += 1

        self.completed.emit(results)
        return results

    def find_duplicate_files(self, directory):
        self._cancel = False
        directory = os.path.abspath(directory)

        files = []
        for root, dirs, filenames in os.walk(directory):
            for filename in filenames:
                files.append(os.path.join(root, filename))

        results = {
            'duplicates': [],
            'total_scanned': len(files),
            'groups': 0,
        }

        # 按大小分组
        size_groups = {}
        for i, filepath in enumerate(files):
            if self._cancel:
                break
            try:
                size = os.path.getsize(filepath)
                if size not in size_groups:
                    size_groups[size] = []
                size_groups[size].append(filepath)
            except OSError:
                pass
            self.progress.emit(i + 1, len(files), f"扫描: {os.path.basename(filepath)}")

        for size, paths in size_groups.items():
            if len(paths) < 2:
                continue

            hash_groups = {}
            for path in paths:
                try:
                    file_hash = self._hash_file(path)
                    if file_hash not in hash_groups:
                        hash_groups[file_hash] = []
                    hash_groups[file_hash].append(path)
                except OSError:
                    pass

            for file_hash, group in hash_groups.items():
                if len(group) > 1:
                    results['duplicates'].append(group)
                    results['groups'] += 1

        self.completed.emit(results)
        return results

    def delete_to_trash(self, files):
        results = {'success': [], 'failed': []}
        for filepath in files:
            try:
                send2trash(filepath)
                results['success'].append(filepath)
            except Exception as e:
                results['failed'].append((filepath, str(e)))
        return results

    def _categorize(self, filepath):
        ext = os.path.splitext(filepath)[1].lower()
        categories = {
            '图片': {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg', '.ico', '.tiff'},
            '视频': {'.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'},
            '音频': {'.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'},
            '文档': {'.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'},
            '表格': {'.xls', '.xlsx', '.csv', '.ods'},
            '演示': {'.ppt', '.pptx', '.odp'},
            '压缩包': {'.zip', '.rar', '.7z', '.tar', '.gz'},
            '代码': {'.py', '.js', '.ts', '.html', '.css', '.java', '.cpp', '.c', '.h'},
            '可执行': {'.exe', '.msi', '.apk'},
            '电子书': {'.epub', '.mobi', '.azw'},
            '字体': {'.ttf', '.otf', '.woff', '.woff2'},
            '垃圾缓存': {'.tmp', '.temp', '.log', '.crdownload', '.part', '.cache'},
        }
        for category, extensions in categories.items():
            if ext in extensions:
                return category
        return '其他'

    def _hash_file(self, filepath, chunk_size=8192):
        hasher = hashlib.md5()
        try:
            with open(filepath, 'rb') as f:
                while True:
                    chunk = f.read(chunk_size)
                    if not chunk:
                        break
                    hasher.update(chunk)
        except OSError:
            return None
        return hasher.hexdigest()

    def _files_are_same(self, file1, file2):
        try:
            if os.path.getsize(file1) != os.path.getsize(file2):
                return False
            return self._hash_file(file1) == self._hash_file(file2)
        except OSError:
            return False

    def organize_async(self, *args, **kwargs):
        thread = threading.Thread(target=self.organize_directory, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()

    def find_duplicates_async(self, directory, images_only=True):
        thread = threading.Thread(
            target=self.find_duplicate_images if images_only else self.find_duplicate_files,
            args=(directory,)
        )
        thread.daemon = True
        thread.start()
