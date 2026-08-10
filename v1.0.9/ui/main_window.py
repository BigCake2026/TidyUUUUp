import os
import subprocess
import sys
from datetime import datetime

from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPen, QPainterPath
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
    QListWidget, QListWidgetItem, QLabel, QPushButton, QStackedWidget,
    QFileDialog, QComboBox, QCheckBox, QProgressBar
)

from core.file_index import FileIndex
from core.file_organizer import FileOrganizer
from .animations import ToastManager
from .styles import TIDY_QSS


# 保留分类图标映射 (仅用于内部文件类型判断, UI 中不显示 emoji)
CATEGORY_ICONS = {
    '图片': '🖼️', '视频': '🎬', '音频': '🎵', '文档': '📄',
    '表格': '📊', '演示': '📽️', '压缩包': '📦', '代码': '💻',
    '可执行': '⚙️', '电子书': '📚', '字体': '🔤', '设计': '🎨',
    '3D模型': '🧊', '数据': '📋', '垃圾缓存': '🗑️', '其他': '📝'
}

# 侧边栏虚拟分类 -> file_index 文件类型集合 (用于过滤)
# '全部文件' 为 None 表示不过滤
SIDEBAR_CATEGORY_MAP = {
    '全部文件': None,
    '工作': {'文档', '表格', '演示'},
    '学习': {'电子书', '代码'},
    '图片': {'图片'},
    '下载': {'压缩包', '可执行'},
    '临时文件': {'垃圾缓存'},
}
SIDEBAR_ITEMS = list(SIDEBAR_CATEGORY_MAP.keys())


# 基于 TIDY_QSS 追加的局部样式 (视图切换等自定义控件)
_EXTRA_QSS = """
/* 视图切换文字按钮 */
QPushButton#ViewTab {
    background: transparent;
    border: none;
    color: #86868B;
    font-size: 13px;
    padding: 6px 10px;
}
QPushButton#ViewTab:hover {
    color: #1D1D1F;
}
QPushButton#ViewTab:checked {
    color: #1D1D1F;
    font-weight: 600;
}

/* 表单标签 */
QLabel#FormLabel {
    color: #86868B;
    font-size: 12px;
    background: transparent;
    border: none;
}
"""


class EmptyFolderIcon(QWidget):
    """用 QPainter 绘制的极简文件夹轮廓 (Empty State 图标, 灰色 #D1D1D6)"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(88, 64)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        color = QColor("#D1D1D6")
        pen = QPen(color)
        pen.setWidthF(2.2)
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)
        p.setPen(pen)
        p.setBrush(Qt.NoBrush)

        # 文件夹轮廓: 左上带 tab 的剪影
        path = QPainterPath()
        path.moveTo(10, 18)
        path.lineTo(36, 18)
        path.lineTo(42, 10)
        path.lineTo(78, 10)
        path.lineTo(78, 52)
        path.lineTo(10, 52)
        path.closeSubpath()
        p.drawPath(path)


class FileItemWidget(QWidget):
    """极简文件列表项: 文件名 + 灰色分类 badge + 灰色元数据, 底部极淡分隔线"""

    def __init__(self, file_info, parent=None):
        super().__init__(parent)
        self.file_info = file_info
        self._setup_ui()

    def _setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(16, 8, 16, 8)
        layout.setSpacing(10)

        name_label = QLabel(self.file_info.get('name', '未知'))
        name_label.setStyleSheet(
            "color: #1D1D1F; font-size: 13px; "
            "background: transparent; border: none;"
        )
        name_label.setWordWrap(False)
        layout.addWidget(name_label, 1)

        cat = self.file_info.get('category', '其他')
        cat_label = QLabel(cat)
        cat_label.setObjectName("BadgeGray")
        cat_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(cat_label)

        size = self._format_size(self.file_info.get('size', 0))
        mtime = datetime.fromtimestamp(
            self.file_info.get('modified', 0)
        ).strftime('%Y-%m-%d')
        meta_label = QLabel(f"{size} · {mtime}")
        meta_label.setStyleSheet(
            "color: #86868B; font-size: 11px; "
            "background: transparent; border: none;"
        )
        layout.addWidget(meta_label)

    def _format_size(self, size):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} PB"

    def paintEvent(self, event):
        super().paintEvent(event)
        # 底部 1px 极淡分隔线 rgba(0,0,0,0.03)
        p = QPainter(self)
        p.setPen(QColor(0, 0, 0, 8))
        h = self.height()
        p.drawLine(0, h - 1, self.width(), h - 1)

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
        self.setWindowTitle("TidyUUUUp")
        self.resize(1100, 700)
        self.setMinimumSize(900, 600)

        self.file_index = FileIndex()
        self.organizer = FileOrganizer(self.file_index)
        self.toast = ToastManager(self)

        self._setup_ui()
        self._connect_signals()

        # 初始化扫描
        QTimer.singleShot(500, self._initial_scan)

    # ==================== UI 构建 ====================

    def _setup_ui(self):
        # 应用设计系统 + 自定义补充 (设置在 MainWindow 上, 覆盖全部子控件含 Toast)
        self.setStyleSheet(TIDY_QSS + _EXTRA_QSS)

        central = QWidget()
        central.setObjectName("WindowBackground")
        self.setCentralWidget(central)

        root = QVBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        root.addWidget(self._build_topbar())
        root.addWidget(self._build_body(), 1)

    def _build_topbar(self):
        bar = QWidget()
        bar.setObjectName("TopBar")
        bar.setFixedHeight(48)

        layout = QHBoxLayout(bar)
        layout.setContentsMargins(16, 0, 16, 0)
        layout.setSpacing(12)

        # Logo (纯文字, 不用 emoji)
        logo = QLabel("TidyUUUUp")
        logo.setObjectName("LogoLabel")
        layout.addWidget(logo)

        # 搜索框 (Spotlight 风格)
        self.search_box = QLineEdit()
        self.search_box.setObjectName("SearchBox")
        self.search_box.setPlaceholderText("搜索文件、应用或文件夹")
        self.search_box.setFixedHeight(30)
        layout.addWidget(self.search_box, 1)

        # 扫描按钮 (轻量文字按钮, 不抢焦点)
        self.scan_btn = QPushButton("扫描")
        self.scan_btn.setObjectName("TextButton")
        self.scan_btn.setCursor(Qt.PointingHandCursor)
        self.scan_btn.setFocusPolicy(Qt.NoFocus)
        layout.addWidget(self.scan_btn)

        return bar

    def _build_body(self):
        body = QWidget()
        body.setObjectName("WindowBackground")
        layout = QHBoxLayout(body)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(self._build_sidebar())
        layout.addWidget(self._build_content(), 1)
        return body

    def _build_sidebar(self):
        sidebar = QWidget()
        sidebar.setObjectName("Sidebar")
        sidebar.setFixedWidth(180)

        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(12, 14, 12, 14)
        layout.setSpacing(2)

        title = QLabel("分类")
        title.setObjectName("SidebarHeader")
        layout.addWidget(title)
        layout.addSpacing(6)

        self.category_buttons = {}
        self.all_btn = None
        for name in SIDEBAR_ITEMS:
            btn = QPushButton(name)
            btn.setObjectName("SidebarItem")
            btn.setCheckable(True)
            btn.setAutoExclusive(True)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFocusPolicy(Qt.NoFocus)
            btn.setFixedHeight(32)
            if name == '全部文件':
                btn.setChecked(True)
                self.all_btn = btn
            else:
                self.category_buttons[name] = btn
            layout.addWidget(btn)

        layout.addStretch()

        self.stats_label = QLabel("已索引 0 个文件")
        self.stats_label.setObjectName("MetaLabel")
        self.stats_label.setContentsMargins(8, 0, 0, 0)
        layout.addWidget(self.stats_label)

        return sidebar

    def _build_content(self):
        content = QWidget()
        content.setObjectName("ContentBackground")

        layout = QVBoxLayout(content)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 视图切换栏 (文字按钮, 替代 Tab)
        switcher = QWidget()
        switcher.setObjectName("ContentBackground")
        sw_layout = QHBoxLayout(switcher)
        sw_layout.setContentsMargins(16, 10, 16, 6)
        sw_layout.setSpacing(4)

        self.view_buttons = []
        for idx, label in enumerate(["文件", "整理", "重复清理"]):
            btn = QPushButton(label)
            btn.setObjectName("ViewTab")
            btn.setCheckable(True)
            btn.setAutoExclusive(True)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFocusPolicy(Qt.NoFocus)
            btn.clicked.connect(lambda _=False, i=idx: self._set_view(i))
            if idx == 0:
                btn.setChecked(True)
            sw_layout.addWidget(btn)
            self.view_buttons.append(btn)
        sw_layout.addStretch()
        layout.addWidget(switcher)

        # 视图栈 (命名为 tabs, 兼容外部 main.py 的 setCurrentIndex 调用)
        # 索引: 0=文件, 1=整理, 2=重复清理
        self.tabs = QStackedWidget()
        self.tabs.addWidget(self._build_files_view())
        self.tabs.addWidget(self._build_organize_view())
        self.tabs.addWidget(self._build_dup_view())
        layout.addWidget(self.tabs, 1)

        return content

    def _build_files_view(self):
        view = QWidget()
        view.setObjectName("ContentBackground")
        layout = QVBoxLayout(view)
        layout.setContentsMargins(16, 6, 16, 16)
        layout.setSpacing(8)

        # 工具栏: 排序下拉 + 文件数量
        toolbar = QWidget()
        toolbar.setObjectName("ContentBackground")
        tb_layout = QHBoxLayout(toolbar)
        tb_layout.setContentsMargins(0, 0, 0, 0)
        tb_layout.setSpacing(8)

        sort_label = QLabel("排序")
        sort_label.setStyleSheet(
            "color: #86868B; font-size: 12px; "
            "background: transparent; border: none;"
        )
        tb_layout.addWidget(sort_label)

        self.sort_combo = QComboBox()
        self.sort_combo.addItems(["修改时间", "创建时间", "名称", "大小"])
        self.sort_combo.setFixedHeight(28)
        self.sort_combo.setFocusPolicy(Qt.NoFocus)
        tb_layout.addWidget(self.sort_combo)

        tb_layout.addStretch()

        self.file_count_label = QLabel("0 个文件")
        self.file_count_label.setStyleSheet(
            "color: #86868B; font-size: 12px; "
            "background: transparent; border: none;"
        )
        tb_layout.addWidget(self.file_count_label)
        layout.addWidget(toolbar)

        # 内容栈: 文件列表 / 空状态
        self.files_stack = QStackedWidget()
        self.files_stack.addWidget(self._build_file_list())    # index 0
        self.files_stack.addWidget(self._build_empty_state())  # index 1
        layout.addWidget(self.files_stack, 1)

        return view

    def _build_file_list(self):
        self.file_list = QListWidget()
        self.file_list.setObjectName("FileList")
        self.file_list.setFocusPolicy(Qt.NoFocus)
        self.file_list.itemDoubleClicked.connect(self._open_item)
        return self.file_list

    def _build_empty_state(self):
        state = QWidget()
        state.setObjectName("ContentBackground")
        layout = QVBoxLayout(state)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignCenter)

        icon = EmptyFolderIcon()
        layout.addWidget(icon, 0, Qt.AlignCenter)

        title = QLabel("暂无文件")
        title.setObjectName("EmptyStateTitle")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        desc = QLabel("扫描桌面，TidyUUUUp 会自动帮你整理文件")
        desc.setObjectName("EmptyStateDesc")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)

        layout.addSpacing(8)

        self.empty_scan_btn = QPushButton("开始扫描")
        self.empty_scan_btn.setCursor(Qt.PointingHandCursor)
        self.empty_scan_btn.setFixedHeight(30)
        self.empty_scan_btn.setFixedWidth(96)
        self.empty_scan_btn.clicked.connect(self._rescan)
        layout.addWidget(self.empty_scan_btn, 0, Qt.AlignCenter)

        return state

    def _build_organize_view(self):
        view = QWidget()
        view.setObjectName("ContentBackground")
        layout = QVBoxLayout(view)
        layout.setContentsMargins(24, 14, 24, 24)
        layout.setSpacing(14)

        title = QLabel("智能整理")
        title.setObjectName("TitleLabel")
        layout.addWidget(title)

        subtitle = QLabel("一键整理杂乱的文件夹，自动分类归档")
        subtitle.setObjectName("SubtitleLabel")
        layout.addWidget(subtitle)

        layout.addSpacing(6)

        # 极简表单 (无卡片包裹)
        self.source_edit = self._add_form_dir_row(
            layout, "源目录", "选择要整理的文件夹..."
        )
        self.target_edit = self._add_form_dir_row(
            layout, "目标目录", "选择目标文件夹（可选，默认与源目录相同）"
        )

        # 整理方式
        strategy_row = QHBoxLayout()
        strategy_row.setSpacing(12)
        s_label = QLabel("整理方式")
        s_label.setObjectName("FormLabel")
        s_label.setFixedWidth(64)
        strategy_row.addWidget(s_label)
        self.strategy_combo = QComboBox()
        self.strategy_combo.addItems(["按文件类型", "按修改日期", "按文件扩展名"])
        self.strategy_combo.setFixedHeight(30)
        self.strategy_combo.setFocusPolicy(Qt.NoFocus)
        strategy_row.addWidget(self.strategy_combo, 1)
        layout.addLayout(strategy_row)

        # 选项
        options_row = QHBoxLayout()
        options_row.setSpacing(24)
        self.subfolder_check = QCheckBox("使用日期子文件夹")
        self.subfolder_check.setChecked(True)
        options_row.addWidget(self.subfolder_check)
        self.dry_run_check = QCheckBox("模拟运行（不移动文件）")
        options_row.addWidget(self.dry_run_check)
        options_row.addStretch()
        layout.addLayout(options_row)

        # 进度区域
        self.progress_widget = QWidget()
        self.progress_widget.setObjectName("ContentBackground")
        pl = QVBoxLayout(self.progress_widget)
        pl.setContentsMargins(0, 6, 0, 0)
        pl.setSpacing(6)
        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(4)
        self.progress_bar.setTextVisible(False)
        pl.addWidget(self.progress_bar)
        self.progress_label = QLabel("")
        self.progress_label.setStyleSheet(
            "color: #86868B; font-size: 12px; "
            "background: transparent; border: none;"
        )
        pl.addWidget(self.progress_label)
        self.progress_widget.hide()
        layout.addWidget(self.progress_widget)

        # 结果
        self.result_text = QLabel("")
        self.result_text.setStyleSheet(
            "color: #1D1D1F; font-size: 12px; "
            "background: transparent; border: none;"
        )
        self.result_text.setWordWrap(True)
        self.result_text.hide()
        layout.addWidget(self.result_text)

        layout.addStretch()

        # 执行按钮
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        self.cancel_org_btn = QPushButton("取消")
        self.cancel_org_btn.setObjectName("SecondaryButton")
        self.cancel_org_btn.setFixedHeight(30)
        self.cancel_org_btn.setFixedWidth(84)
        self.cancel_org_btn.setFocusPolicy(Qt.NoFocus)
        self.cancel_org_btn.setCursor(Qt.PointingHandCursor)
        self.cancel_org_btn.hide()
        btn_row.addWidget(self.cancel_org_btn)

        self.organize_btn = QPushButton("开始整理")
        self.organize_btn.setFixedHeight(30)
        self.organize_btn.setFixedWidth(108)
        self.organize_btn.setCursor(Qt.PointingHandCursor)
        btn_row.addWidget(self.organize_btn)
        layout.addLayout(btn_row)

        return view

    def _add_form_dir_row(self, parent_layout, label_text, placeholder):
        """添加一行: 标签 + 输入框 + 浏览按钮, 返回输入框"""
        row = QHBoxLayout()
        row.setSpacing(12)

        label = QLabel(label_text)
        label.setObjectName("FormLabel")
        label.setFixedWidth(64)
        row.addWidget(label)

        edit = QLineEdit()
        edit.setPlaceholderText(placeholder)
        edit.setFixedHeight(30)
        row.addWidget(edit, 1)

        browse_btn = QPushButton("浏览")
        browse_btn.setObjectName("SecondaryButton")
        browse_btn.setFixedHeight(30)
        browse_btn.setFixedWidth(64)
        browse_btn.setFocusPolicy(Qt.NoFocus)
        browse_btn.setCursor(Qt.PointingHandCursor)
        browse_btn.clicked.connect(lambda: self._choose_dir(edit))
        row.addWidget(browse_btn)

        parent_layout.addLayout(row)
        return edit

    def _build_dup_view(self):
        view = QWidget()
        view.setObjectName("ContentBackground")
        layout = QVBoxLayout(view)
        layout.setContentsMargins(24, 14, 24, 24)
        layout.setSpacing(14)

        title = QLabel("重复清理")
        title.setObjectName("TitleLabel")
        layout.addWidget(title)

        subtitle = QLabel("查找重复文件，释放磁盘空间")
        subtitle.setObjectName("SubtitleLabel")
        layout.addWidget(subtitle)

        layout.addSpacing(6)

        self.dup_dir_edit = self._add_form_dir_row(
            layout, "扫描目录", "选择要扫描的文件夹..."
        )

        type_row = QHBoxLayout()
        type_row.setSpacing(24)
        self.dup_images_only = QCheckBox("仅扫描图片")
        self.dup_images_only.setChecked(True)
        type_row.addWidget(self.dup_images_only)
        type_row.addStretch()
        layout.addLayout(type_row)

        # 进度
        self.dup_progress_bar = QProgressBar()
        self.dup_progress_bar.setFixedHeight(4)
        self.dup_progress_bar.setTextVisible(False)
        self.dup_progress_bar.hide()
        layout.addWidget(self.dup_progress_bar)

        self.dup_progress_label = QLabel("")
        self.dup_progress_label.setStyleSheet(
            "color: #86868B; font-size: 12px; "
            "background: transparent; border: none;"
        )
        self.dup_progress_label.hide()
        layout.addWidget(self.dup_progress_label)

        # 结果列表
        self.dup_list = QListWidget()
        self.dup_list.setStyleSheet(
            "QListWidget { background: transparent; border: none; outline: none; }"
        )
        layout.addWidget(self.dup_list, 1)

        # 按钮
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        self.scan_dup_btn = QPushButton("开始扫描")
        self.scan_dup_btn.setFixedHeight(30)
        self.scan_dup_btn.setFixedWidth(108)
        self.scan_dup_btn.setCursor(Qt.PointingHandCursor)
        btn_row.addWidget(self.scan_dup_btn)
        layout.addLayout(btn_row)

        return view

    def _choose_dir(self, line_edit):
        directory = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if directory:
            line_edit.setText(directory)

    # ==================== 信号连接 ====================

    def _connect_signals(self):
        # 搜索
        self.search_box.textChanged.connect(self._on_search)
        self.scan_btn.clicked.connect(self._rescan)

        # 分类
        self.all_btn.clicked.connect(lambda: self._filter_by_category('全部文件'))
        for cat_name, btn in self.category_buttons.items():
            btn.clicked.connect(lambda _=False, c=cat_name: self._filter_by_category(c))

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

    # ==================== 视图切换 ====================

    def _set_view(self, index):
        """切换内容视图: 0=文件, 1=整理, 2=重复清理"""
        self.tabs.setCurrentIndex(index)
        if 0 <= index < len(self.view_buttons):
            self.view_buttons[index].setChecked(True)

    # ==================== 扫描 / 搜索 / 过滤 ====================

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
        self._set_view(0)
        self._refresh_file_list(query=self._search_query)

    def _filter_by_category(self, category):
        self._set_view(0)
        self._refresh_file_list(category=category)

    def _resolve_category(self, category):
        """将侧边栏标签解析为 file_index 文件类型集合 (None 表示不过滤)"""
        if category is None:
            return None
        if category in SIDEBAR_CATEGORY_MAP:
            return SIDEBAR_CATEGORY_MAP[category]
        # 兼容直接传入 file_index 原始分类的情况
        return {category}

    def _refresh_file_list(self, query=None, category=None):
        self.file_list.clear()
        cat_set = self._resolve_category(category)

        if query:
            results = self.file_index.search(query, category=None, limit=200)
            if cat_set:
                results = [r for r in results if r.get('category') in cat_set]
        elif cat_set:
            results = []
            for cat in cat_set:
                results.extend(self.file_index.get_by_category(cat))
            results.sort(key=lambda x: x.get('modified', 0), reverse=True)
            results = results[:200]
        else:
            results = self.file_index.get_recent(200)

        for info in results:
            item = QListWidgetItem(self.file_list)
            widget = FileItemWidget(info)
            item.setSizeHint(widget.sizeHint())
            self.file_list.addItem(item)
            self.file_list.setItemWidget(item, widget)

        self.file_count_label.setText(f"{len(results)} 个文件")
        # 空状态切换
        self.files_stack.setCurrentIndex(1 if not results else 0)

    def _open_item(self, item):
        widget = self.file_list.itemWidget(item)
        if widget and hasattr(widget, '_open_file'):
            widget._open_file()

    def _update_stats(self):
        stats = self.file_index.get_stats()
        total = sum(s['count'] for s in stats.values())
        self.stats_label.setText(f"已索引 {total} 个文件")

    # ==================== 智能整理 ====================

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

        msg = "整理完成\n\n"
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

    # ==================== 重复清理 ====================

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
            text = f"第 {i + 1} 组 · {len(group)} 个重复\n"
            for path in group:
                size = os.path.getsize(path) if os.path.exists(path) else 0
                text += f"   {path}  [{size / 1024 / 1024:.1f} MB]\n"
            item.setText(text)
            item.setForeground(QColor("#1D1D1F"))

        self.toast.show_toast(
            f"发现 {len(groups)} 组重复文件", 3000, 'success'
        )

    # ==================== 绘制 ====================

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor("#F5F5F7"))
