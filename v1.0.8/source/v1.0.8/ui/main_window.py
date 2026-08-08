import os
import subprocess
import sys
from datetime import datetime
from PyQt5.QtCore import (
    Qt, QSize, QTimer, QPropertyAnimation, QEasingCurve, QPoint, pyqtSignal
)
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
    QListWidget, QListWidgetItem, QLabel, QPushButton, QSplitter,
    QFrame, QFileDialog, QComboBox, QCheckBox, QProgressBar, QMessageBox,
    QTabWidget, QGridLayout, QSizePolicy, QGraphicsOpacityEffect, QDialog
)
from PyQt5.QtGui import QIcon, QPainter, QColor, QPixmap, QFont, QCursor

from core.file_index import FileIndex
from core.file_organizer import FileOrganizer
from .animations import BounceAnimation, ToastManager


CATEGORY_ICONS = {
    '图片': '🖼️', '视频': '🎬', '音频': '🎵', '文档': '📄',
    '表格': '📊', '演示': '📽️', '压缩包': '📦', '代码': '💻',
    '可执行': '⚙️', '电子书': '📚', '字体': '🔤', '设计': '🎨',
    '3D模型': '🧊', '数据': '📋', '垃圾缓存': '🗑️', '其他': '📝'
}


class FileItemWidget(QWidget):
    def __init__(self, file_info, parent=None):
        super().__init__(parent)
        self.file_info = file_info
        self._setup_ui()

    def _setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 6, 8, 6)
        layout.setSpacing(10)

        # 图标
        icon_label = QLabel()
        icon_label.setFixedSize(36, 36)
        icon_label.setStyleSheet("background: rgba(255,255,255,0.1); border-radius: 8px;")
        icon_label.setAlignment(Qt.AlignCenter)

        cat = self.file_info.get('category', '其他')
        icon_label.setText(CATEGORY_ICONS.get(cat, '📝'))
        icon_label.setStyleSheet("font-size: 22px;")
        layout.addWidget(icon_label)

        # 文件信息
        info_layout = QVBoxLayout()
        info_layout.setSpacing(2)

        name_label = QLabel(self.file_info.get('name', '未知'))
        name_label.setStyleSheet("color: white; font-size: 13px; font-weight: 500;")
        name_label.setWordWrap(False)
        info_layout.addWidget(name_label)

        # 元数据
        size = self._format_size(self.file_info.get('size', 0))
        mtime = datetime.fromtimestamp(self.file_info.get('modified', 0)).strftime('%Y-%m-%d %H:%M')
        meta_label = QLabel(f"{size} · {mtime}")
        meta_label.setStyleSheet("color: rgba(255,255,255,0.5); font-size: 11px;")
        info_layout.addWidget(meta_label)

        layout.addLayout(info_layout, 1)

        # 分类标签
        cat_label = QLabel(cat)
        cat_label.setObjectName("CategoryBadge")
        cat_label.setAlignment(Qt.AlignCenter)
        cat_label.setStyleSheet("""
            background: rgba(100, 150, 255, 0.3);
            border-radius: 6px;
            padding: 3px 10px;
            color: rgba(200, 220, 255, 0.95);
            font-size: 11px;
            font-weight: 500;
        """)
        layout.addWidget(cat_label)

    def _format_size(self, size):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} PB"

    def mouseDoubleClickEvent(self, event):
        self._open_file()

    def _open_file(self):
        path = self.file_info.get('path', '')
        if os.path.exists(path):
            try:
                if sys.platform == 'win32':
                    os.startfile(path)
                elif sys.platform == 'darwin':
                    subprocess.Popen(['open', path])
                else:
                    subprocess.Popen(['xdg-open', path])
            except Exception as e:
                print(f"打开失败: {e}")


class MainWindow(QMainWindow):
    show_dock = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("TidyUUUUp - 智能工作台")
        self.resize(1100, 700)
        self.setMinimumSize(900, 600)

        self.file_index = FileIndex()
        self.organizer = FileOrganizer(self.file_index)
        self.toast = ToastManager(self)

        self._setup_ui()
        self._connect_signals()

        # 初始化扫描
        QTimer.singleShot(500, self._initial_scan)

    def _setup_ui(self):
        central = QWidget()
        central.setStyleSheet("background: rgba(15, 15, 25, 0.95);")
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 顶部标题栏
        header = QWidget()
        header.setFixedHeight(70)
        header.setStyleSheet("""
            background: rgba(25, 25, 40, 0.8);
            border-bottom: 1px solid rgba(255,255,255,0.06);
        """)

        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(24, 0, 24, 0)
        header_layout.setSpacing(16)

        # Logo
        logo_label = QLabel("◇ TidyUUUUp")
        logo_label.setStyleSheet("font-size: 22px; font-weight: 700; color: white;")
        header_layout.addWidget(logo_label)

        # 搜索框
        self.search_box = QLineEdit()
        self.search_box.setObjectName("SearchBox")
        self.search_box.setPlaceholderText("🔍  搜索文件、应用...")
        self.search_box.setFixedHeight(40)
        self.search_box.setMinimumWidth(400)
        header_layout.addWidget(self.search_box, 1)

        # 操作按钮
        self.scan_btn = QPushButton("扫描")
        self.scan_btn.setObjectName("SecondaryButton")
        self.scan_btn.setFixedHeight(36)
        header_layout.addWidget(self.scan_btn)

        self.dock_btn = QPushButton("显示Dock")
        self.dock_btn.setFixedHeight(36)
        self.dock_btn.clicked.connect(self.show_dock.emit)
        header_layout.addWidget(self.dock_btn)

        main_layout.addWidget(header)

        # 主体区域
        body = QWidget()
        body_layout = QHBoxLayout(body)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)

        # 左侧分类栏
        sidebar = QWidget()
        sidebar.setObjectName("CategorySidebar")
        sidebar.setFixedWidth(200)

        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(12, 16, 12, 16)
        sidebar_layout.setSpacing(4)

        # 分类标题
        cat_title = QLabel("分类")
        cat_title.setStyleSheet("color: rgba(255,255,255,0.5); font-size: 11px; font-weight: 600; padding: 4px 8px;")
        sidebar_layout.addWidget(cat_title)

        # 全部
        self.all_btn = self._create_category_btn("📋", "全部")
        self.all_btn.setChecked(True)
        sidebar_layout.addWidget(self.all_btn)

        # 各分类按钮
        self.category_buttons = {}
        for cat_name in self.file_index.get_categories():
            if cat_name == '垃圾缓存':
                continue
            btn = self._create_category_btn(
                CATEGORY_ICONS.get(cat_name, '📝'), cat_name
            )
            self.category_buttons[cat_name] = btn
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()

        # 统计信息
        self.stats_label = QLabel("已索引 0 个文件")
        self.stats_label.setStyleSheet("color: rgba(255,255,255,0.4); font-size: 11px; padding: 8px;")
        sidebar_layout.addWidget(self.stats_label)

        body_layout.addWidget(sidebar)

        # 右侧内容区 - 使用Tab
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)

        # Tab 1: 文件浏览
        self.files_tab = QWidget()
        self._setup_files_tab()
        self.tabs.addTab(self.files_tab, "📁 文件")

        # Tab 2: 智能整理
        self.organize_tab = QWidget()
        self._setup_organize_tab()
        self.tabs.addTab(self.organize_tab, "🧹 智能整理")

        # Tab 3: 重复清理
        self.duplicate_tab = QWidget()
        self._setup_duplicate_tab()
        self.tabs.addTab(self.duplicate_tab, "🔍 重复清理")

        body_layout.addWidget(self.tabs, 1)

        main_layout.addWidget(body, 1)

    def _create_category_btn(self, icon, name):
        btn = QPushButton(f"  {icon}  {name}")
        btn.setObjectName("CategoryItem")
        btn.setCheckable(True)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setAutoExclusive(True)
        return btn

    def _setup_files_tab(self):
        layout = QVBoxLayout(self.files_tab)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        # 工具栏
        toolbar = QWidget()
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(0, 0, 0, 0)
        toolbar_layout.setSpacing(8)

        sort_label = QLabel("排序:")
        sort_label.setStyleSheet("color: rgba(255,255,255,0.6);")
        toolbar_layout.addWidget(sort_label)

        self.sort_combo = QComboBox()
        self.sort_combo.addItems(["修改时间", "创建时间", "名称", "大小"])
        self.sort_combo.setFixedHeight(32)
        toolbar_layout.addWidget(self.sort_combo)

        toolbar_layout.addStretch()

        self.file_count_label = QLabel("0 个文件")
        self.file_count_label.setStyleSheet("color: rgba(255,255,255,0.5); font-size: 12px;")
        toolbar_layout.addWidget(self.file_count_label)

        layout.addWidget(toolbar)

        # 文件列表
        self.file_list = QListWidget()
        self.file_list.setObjectName("FileList")
        self.file_list.setStyleSheet("""
            QListWidget {
                background: transparent;
                border: none;
                outline: none;
            }
            QListWidget::item {
                background: transparent;
                border-radius: 10px;
                margin: 2px 0;
            }
            QListWidget::item:hover {
                background: rgba(255,255,255,0.06);
            }
            QListWidget::item:selected {
                background: rgba(100, 150, 255, 0.25);
            }
        """)
        layout.addWidget(self.file_list, 1)

        self.file_list.itemDoubleClicked.connect(self._open_item)

    def _setup_organize_tab(self):
        layout = QVBoxLayout(self.organize_tab)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(20)

        # 标题
        title = QLabel("智能整理")
        title.setObjectName("TitleLabel")
        layout.addWidget(title)

        subtitle = QLabel("一键整理杂乱的文件夹，自动分类归档")
        subtitle.setObjectName("SubtitleLabel")
        layout.addWidget(subtitle)

        # 配置卡片
        card = QWidget()
        card.setObjectName("LiquidGlassPanel")
        card.setStyleSheet("""
            QWidget#LiquidGlassPanel {
                background: rgba(40, 40, 55, 0.6);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
            }
        """)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(24, 24, 24, 24)
        card_layout.setSpacing(16)

        # 源目录
        self._add_dir_row(card_layout, "源目录:", "source")
        # 目标目录
        self._add_dir_row(card_layout, "目标目录:", "target")

        # 整理策略
        strategy_row = QHBoxLayout()
        strategy_row.setSpacing(12)

        strategy_label = QLabel("整理方式:")
        strategy_label.setFixedWidth(80)
        strategy_label.setStyleSheet("color: rgba(255,255,255,0.8);")
        strategy_row.addWidget(strategy_label)

        self.strategy_combo = QComboBox()
        self.strategy_combo.addItems(["按文件类型", "按修改日期", "按文件扩展名"])
        self.strategy_combo.setFixedHeight(36)
        strategy_row.addWidget(self.strategy_combo, 1)

        card_layout.addLayout(strategy_row)

        # 选项
        options_row = QHBoxLayout()
        options_row.setSpacing(20)

        self.subfolder_check = QCheckBox("使用日期子文件夹")
        self.subfolder_check.setChecked(True)
        self.subfolder_check.setStyleSheet("color: white;")
        options_row.addWidget(self.subfolder_check)

        self.dry_run_check = QCheckBox("模拟运行（不移动文件）")
        self.dry_run_check.setStyleSheet("color: white;")
        options_row.addWidget(self.dry_run_check)

        options_row.addStretch()
        card_layout.addLayout(options_row)

        layout.addWidget(card)

        # 进度区域
        self.progress_widget = QWidget()
        progress_layout = QVBoxLayout(self.progress_widget)
        progress_layout.setContentsMargins(0, 0, 0, 0)
        progress_layout.setSpacing(8)

        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(8)
        self.progress_bar.setTextVisible(False)
        progress_layout.addWidget(self.progress_bar)

        self.progress_label = QLabel("")
        self.progress_label.setStyleSheet("color: rgba(255,255,255,0.6); font-size: 12px;")
        progress_layout.addWidget(self.progress_label)

        self.progress_widget.hide()
        layout.addWidget(self.progress_widget)

        # 结果区域
        self.result_text = QLabel("")
        self.result_text.setStyleSheet("""
            color: rgba(255,255,255,0.7);
            background: rgba(0,0,0,0.2);
            border-radius: 10px;
            padding: 16px;
            font-size: 12px;
        """)
        self.result_text.setWordWrap(True)
        self.result_text.hide()
        layout.addWidget(self.result_text)

        layout.addStretch()

        # 执行按钮
        btn_row = QHBoxLayout()
        btn_row.addStretch()

        self.cancel_org_btn = QPushButton("取消")
        self.cancel_org_btn.setObjectName("SecondaryButton")
        self.cancel_org_btn.setFixedHeight(40)
        self.cancel_org_btn.setFixedWidth(100)
        self.cancel_org_btn.hide()
        btn_row.addWidget(self.cancel_org_btn)

        self.organize_btn = QPushButton("✨  开始整理")
        self.organize_btn.setFixedHeight(40)
        self.organize_btn.setFixedWidth(160)
        btn_row.addWidget(self.organize_btn)

        layout.addLayout(btn_row)

    def _add_dir_row(self, parent_layout, label_text, mode):
        row = QHBoxLayout()
        row.setSpacing(12)

        label = QLabel(label_text)
        label.setFixedWidth(80)
        label.setStyleSheet("color: rgba(255,255,255,0.8);")
        row.addWidget(label)

        if mode == "source":
            self.source_edit = QLineEdit()
            self.source_edit.setPlaceholderText("选择要整理的文件夹...")
            self.source_edit.setObjectName("SearchBox")
            self.source_edit.setFixedHeight(36)
            row.addWidget(self.source_edit, 1)

            source_btn = QPushButton("浏览...")
            source_btn.setObjectName("SecondaryButton")
            source_btn.setFixedHeight(36)
            source_btn.clicked.connect(lambda: self._choose_dir(self.source_edit))
            row.addWidget(source_btn)
        else:
            self.target_edit = QLineEdit()
            self.target_edit.setPlaceholderText("选择目标文件夹（可选，默认与源目录相同）")
            self.target_edit.setObjectName("SearchBox")
            self.target_edit.setFixedHeight(36)
            row.addWidget(self.target_edit, 1)

            target_btn = QPushButton("浏览...")
            target_btn.setObjectName("SecondaryButton")
            target_btn.setFixedHeight(36)
            target_btn.clicked.connect(lambda: self._choose_dir(self.target_edit))
            row.addWidget(target_btn)

        parent_layout.addLayout(row)

    def _choose_dir(self, line_edit):
        directory = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if directory:
            line_edit.setText(directory)

    def _setup_duplicate_tab(self):
        layout = QVBoxLayout(self.duplicate_tab)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        title = QLabel("重复清理")
        title.setObjectName("TitleLabel")
        layout.addWidget(title)

        subtitle = QLabel("查找重复文件和相似图片，释放磁盘空间")
        subtitle.setObjectName("SubtitleLabel")
        layout.addWidget(subtitle)

        # 配置
        config_card = QWidget()
        config_card.setStyleSheet("""
            background: rgba(40, 40, 55, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
        """)
        config_layout = QVBoxLayout(config_card)
        config_layout.setContentsMargins(20, 20, 20, 20)
        config_layout.setSpacing(12)

        dir_row = QHBoxLayout()
        dir_label = QLabel("扫描目录:")
        dir_label.setFixedWidth(80)
        dir_label.setStyleSheet("color: rgba(255,255,255,0.8);")
        dir_row.addWidget(dir_label)

        self.dup_dir_edit = QLineEdit()
        self.dup_dir_edit.setObjectName("SearchBox")
        self.dup_dir_edit.setFixedHeight(36)
        self.dup_dir_edit.setPlaceholderText("选择要扫描的文件夹...")
        dir_row.addWidget(self.dup_dir_edit, 1)

        dup_browse_btn = QPushButton("浏览...")
        dup_browse_btn.setObjectName("SecondaryButton")
        dup_browse_btn.setFixedHeight(36)
        dup_browse_btn.clicked.connect(lambda: self._choose_dir(self.dup_dir_edit))
        dir_row.addWidget(dup_browse_btn)
        config_layout.addLayout(dir_row)

        type_row = QHBoxLayout()
        self.dup_images_only = QCheckBox("仅扫描图片")
        self.dup_images_only.setChecked(True)
        self.dup_images_only.setStyleSheet("color: white;")
        type_row.addWidget(self.dup_images_only)
        type_row.addStretch()
        config_layout.addLayout(type_row)

        layout.addWidget(config_card)

        # 进度
        self.dup_progress_bar = QProgressBar()
        self.dup_progress_bar.setFixedHeight(8)
        self.dup_progress_bar.setTextVisible(False)
        self.dup_progress_bar.hide()
        layout.addWidget(self.dup_progress_bar)

        self.dup_progress_label = QLabel("")
        self.dup_progress_label.setStyleSheet("color: rgba(255,255,255,0.6); font-size: 12px;")
        self.dup_progress_label.hide()
        layout.addWidget(self.dup_progress_label)

        # 结果列表
        self.dup_list = QListWidget()
        self.dup_list.setStyleSheet("""
            QListWidget {
                background: transparent;
                border: none;
            }
            QListWidget::item {
                background: rgba(255,255,255,0.04);
                border-radius: 8px;
                padding: 8px;
                margin: 4px 0;
            }
        """)
        layout.addWidget(self.dup_list, 1)

        # 按钮
        btn_row = QHBoxLayout()
        btn_row.addStretch()

        self.scan_dup_btn = QPushButton("🔍  开始扫描")
        self.scan_dup_btn.setFixedHeight(40)
        self.scan_dup_btn.setFixedWidth(140)
        btn_row.addWidget(self.scan_dup_btn)

        layout.addLayout(btn_row)

    def _connect_signals(self):
        # 搜索
        self.search_box.textChanged.connect(self._on_search)
        self.scan_btn.clicked.connect(self._rescan)

        # 分类
        self.all_btn.clicked.connect(lambda: self._filter_by_category(None))
        for cat_name, btn in self.category_buttons.items():
            btn.clicked.connect(lambda checked, c=cat_name: self._filter_by_category(c))

        # 整理
        self.organize_btn.clicked.connect(self._start_organize)
        self.cancel_org_btn.clicked.connect(self.organizer.cancel)

        self.organizer.progress.connect(self._on_organize_progress)
        self.organizer.completed.connect(self._on_organize_complete)
        self.organizer.error.connect(self._on_organize_error)

        # 重复扫描
        self.scan_dup_btn.clicked.connect(self._start_dup_scan)

        # 搜索防抖 - 用户停止输入 300ms 后才真正搜索, 避免每次按键阻塞 UI
        self._search_debounce = QTimer(self)
        self._search_debounce.setSingleShot(True)
        self._search_debounce.setInterval(300)
        self._search_debounce.timeout.connect(self._do_search)
        self._search_query = ""

    def _initial_scan(self):
        self.file_index.scan_default_locations()
        self.file_index.cleanup_missing()
        self._refresh_file_list()
        self._update_stats()

    def _rescan(self):
        self.toast.show_toast("正在扫描文件...", 2000)
        self.file_index.scan_default_locations()
        self.file_index.cleanup_missing()
        self._refresh_file_list()
        self._update_stats()
        self.toast.show_toast("扫描完成！", 2000, 'success')

    def _on_search(self, text):
        """搜索输入 - 仅触发防抖, 不立即搜索"""
        self._search_query = text
        self._search_debounce.start()

    def _do_search(self):
        """防抖结束后真正执行搜索"""
        self._refresh_file_list(query=self._search_query)

    def _filter_by_category(self, category):
        self._refresh_file_list(category=category)

    def _refresh_file_list(self, query=None, category=None):
        self.file_list.clear()

        if query:
            results = self.file_index.search(query, category=category, limit=200)
        elif category:
            results = self.file_index.get_by_category(category)
        else:
            results = self.file_index.get_recent(200)

        for info in results:
            item = QListWidgetItem(self.file_list)
            widget = FileItemWidget(info)
            item.setSizeHint(widget.sizeHint())
            self.file_list.addItem(item)
            self.file_list.setItemWidget(item, widget)

        self.file_count_label.setText(f"{len(results)} 个文件")

    def _open_item(self, item):
        widget = self.file_list.itemWidget(item)
        if widget and hasattr(widget, '_open_file'):
            widget._open_file()

    def _update_stats(self):
        stats = self.file_index.get_stats()
        total = sum(s['count'] for s in stats.values())
        self.stats_label.setText(f"已索引 {total} 个文件")

    def _start_organize(self):
        source = self.source_edit.text().strip()
        if not source:
            self.toast.show_toast("请选择源目录", 3000)
            return

        target = self.target_edit.text().strip() or None

        strategy_map = {0: 'category', 1: 'date', 2: 'extension'}
        strategy = strategy_map.get(self.strategy_combo.currentIndex(), 'category')

        use_sub = self.subfolder_check.isChecked()
        dry_run = self.dry_run_check.isChecked()

        self.progress_widget.show()
        self.result_text.hide()
        self.organize_btn.setEnabled(False)
        self.cancel_org_btn.show()

        self.organizer.organize_async(
            source, target, strategy=strategy,
            use_subfolders=use_sub, dry_run=dry_run
        )

    def _on_organize_progress(self, current, total, message):
        self.progress_bar.setMaximum(total)
        self.progress_bar.setValue(current)
        self.progress_label.setText(message)

    def _on_organize_complete(self, results):
        self.organize_btn.setEnabled(True)
        self.cancel_org_btn.hide()

        msg = f"📊 整理完成！\n\n"
        msg += f"  共扫描: {results.get('total_files', 0)} 个文件\n"
        msg += f"  已移动: {len(results.get('moved', []))} 个\n"
        msg += f"  跳过: {len(results.get('skipped', []))} 个\n"
        msg += f"  重复文件: {len(results.get('duplicates', []))} 个\n"
        if results.get('errors'):
            msg += f"  错误: {len(results.get('errors', []))} 个\n"

        self.result_text.setText(msg)
        self.result_text.show()

        self.toast.show_toast(
            f"整理完成！移动了 {len(results.get('moved', []))} 个文件",
            4000, 'success'
        )

    def _on_organize_error(self, error_msg):
        self.organize_btn.setEnabled(True)
        self.cancel_org_btn.hide()
        self.toast.show_toast(f"错误: {error_msg}", 4000)

    def _start_dup_scan(self):
        directory = self.dup_dir_edit.text().strip()
        if not directory:
            self.toast.show_toast("请选择要扫描的目录", 3000)
            return

        self.dup_progress_bar.show()
        self.dup_progress_label.show()
        self.scan_dup_btn.setEnabled(False)

        # 先断开 organize 回调, 避免两套回调互相干扰 (重复扫描时 organize_complete
        # 也会被触发, 弹出错误的"整理完成"提示并清空 organize result)
        try:
            self.organizer.progress.disconnect(self._on_organize_progress)
            self.organizer.completed.disconnect(self._on_organize_complete)
        except (TypeError, RuntimeError):
            pass  # 信号未连接时 disconnect 会抛异常, 忽略

        self.organizer.progress.connect(self._on_dup_progress)
        self.organizer.completed.connect(self._on_dup_complete)

        self.organizer.find_duplicates_async(directory, self.dup_images_only.isChecked())

    def _on_dup_progress(self, current, total, message):
        self.dup_progress_bar.setMaximum(total)
        self.dup_progress_bar.setValue(current)
        self.dup_progress_label.setText(message)

    def _on_dup_complete(self, results):
        self.scan_dup_btn.setEnabled(True)
        self.dup_progress_bar.hide()
        self.dup_progress_label.hide()

        # 恢复 organize 回调, 避免后续整理操作无响应
        try:
            self.organizer.progress.disconnect(self._on_dup_progress)
            self.organizer.completed.disconnect(self._on_dup_complete)
        except (TypeError, RuntimeError):
            pass
        self.organizer.progress.connect(self._on_organize_progress)
        self.organizer.completed.connect(self._on_organize_complete)

        self.dup_list.clear()

        groups = results.get('duplicates', [])
        if not groups:
            self.toast.show_toast("没有发现重复文件", 3000)
            return

        for i, group in enumerate(groups):
            item = QListWidgetItem(self.dup_list)
            text = f"📎 第 {i+1} 组 ({len(group)} 个重复):\n"
            for path in group:
                size = os.path.getsize(path) if os.path.exists(path) else 0
                text += f"   • {path} [{size/1024/1024:.1f} MB]\n"
            item.setText(text)
            item.setForeground(QColor(220, 220, 240))

        self.toast.show_toast(
            f"发现 {len(groups)} 组重复文件", 3000, 'success'
        )

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), QColor(15, 15, 25, 245))
