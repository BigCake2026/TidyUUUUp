"""
智能分类文件夹面板 - Smart Zone Panel
在Dock栏上显示虚拟分类文件夹，点击快速查看对应分类的文件
升级：Liquid Glass 3D 文件夹图标 + 鼠标悬停显示目录树弹出面板
"""
import os
import sys
import subprocess
from PyQt5.QtCore import (
    Qt, QPoint, QSize, QPropertyAnimation, QEasingCurve,
    pyqtSignal, QTimer, QRect, QRectF, pyqtProperty
)
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QListWidget, QListWidgetItem, QScrollArea, QFrame, QGraphicsOpacityEffect,
    QTreeWidget, QTreeWidgetItem, QToolTip
)
from PyQt5.QtGui import (
    QPainter, QColor, QIcon, QPixmap, QFont, QCursor, QLinearGradient, QBrush,
    QPen, QRadialGradient, QPainterPath
)

from core.smart_engine import SmartRuleEngine


# Apple HIG: 侧边栏使用纯文字标签 + 统一 accent 色（#0A84FF）
# 不再使用 emoji 分类图标，回归 macOS Finder 风格


class DirectoryTreePopup(QWidget):
    """
    Liquid Glass 风格目录树弹出面板
    鼠标悬停在 ZoneFolderButton 上时显示该分类下的文件目录树
    """

    file_activated = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(None)  # 独立窗口，Popup 类型
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Popup |
            Qt.NoDropShadowWindowHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setFixedWidth(360)
        self.setMaximumHeight(420)

        self._target_anchor = QPoint(0, 0)
        self._opacity_effect = QGraphicsOpacityEffect(self)
        self._opacity_effect.setOpacity(0.0)
        self.setGraphicsEffect(self._opacity_effect)
        self._fade_anim = None
        self._auto_hide_timer = QTimer(self)
        self._auto_hide_timer.setSingleShot(True)
        self._auto_hide_timer.timeout.connect(self.fade_out)

        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(1, 1, 1, 1)
        layout.setSpacing(0)

        # Liquid Glass 背景容器（1px 边框绘制在 paintEvent）
        container = QWidget()
        container.setObjectName("TreePopupBg")
        inner = QVBoxLayout(container)
        inner.setContentsMargins(14, 14, 14, 14)
        inner.setSpacing(10)

        # 标题栏（纯文字，Apple HIG 风格）
        header = QHBoxLayout()
        header.setSpacing(10)

        self.title_label = QLabel("目录树")
        self.title_label.setStyleSheet("""
            color: #1D1D1F;
            font-size: 15px;
            font-weight: 700;
            background: transparent;
        """)
        header.addWidget(self.title_label)

        header.addStretch()

        self.count_badge = QLabel("0")
        self.count_badge.setAlignment(Qt.AlignCenter)
        self.count_badge.setMinimumWidth(28)
        self.count_badge.setStyleSheet("""
            background: rgba(10, 132, 255, 0.12);
            border: 1px solid rgba(10, 132, 255, 0.22);
            border-radius: 14px;
            padding: 2px 10px;
            color: #0A84FF;
            font-size: 11px;
            font-weight: 700;
        """)
        header.addWidget(self.count_badge)

        inner.addLayout(header)

        # 分隔线
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background: rgba(120, 130, 160, 0.14); border: none; max-height: 1px;")
        inner.addWidget(line)

        # 目录树
        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.tree.setIndentation(14)
        self.tree.setRootIsDecorated(False)
        self.tree.setStyleSheet("""
            QTreeWidget {
                background: transparent;
                border: none;
                outline: none;
                color: #1D1D1F;
                font-size: 12px;
                alternate-background-color: transparent;
            }
            QTreeWidget::item {
                padding: 5px 8px;
                border-radius: 7px;
                margin: 1px 0;
            }
            QTreeWidget::item:hover {
                background: rgba(10, 132, 255, 0.10);
            }
            QTreeWidget::item:selected {
                background: rgba(10, 132, 255, 0.18);
                color: #0A84FF;
            }
            QTreeWidget::branch {
                background: transparent;
            }
            QScrollBar:vertical {
                background: transparent;
                width: 6px;
                margin: 4px 0;
            }
            QScrollBar::handle:vertical {
                background: rgba(120, 130, 160, 0.28);
                border-radius: 3px;
                min-height: 24px;
            }
            QScrollBar::handle:vertical:hover {
                background: rgba(120, 130, 160, 0.45);
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: transparent;
            }
        """)
        self.tree.itemDoubleClicked.connect(self._on_item_activated)
        self.tree.itemClicked.connect(self._on_item_single_click)
        inner.addWidget(self.tree, 1)

        # 底部提示
        tip = QLabel("双击打开文件 · 点击跳转")
        tip.setAlignment(Qt.AlignCenter)
        tip.setStyleSheet("color: rgba(120, 130, 160, 0.75); font-size: 10px; background: transparent;")
        inner.addWidget(tip)

        layout.addWidget(container)

    def populate_from_files(self, files, zone_name, zone_icon, zone_color):
        """
        根据文件列表填充目录树
        按子目录分组显示，无子目录则直接显示文件列表
        files: list of {name, path, size, modified, category}
        zone_icon / zone_color 参数保留以兼容调用方，但视觉上统一使用 Apple 蓝
        """
        self.tree.clear()
        self.title_label.setText(zone_name)
        self.count_badge.setText(str(len(files)))

        # 按目录分组
        dir_groups = {}
        for info in files:
            path = info.get('path', '')
            dirname = os.path.dirname(path)
            if dirname not in dir_groups:
                dir_groups[dirname] = []
            dir_groups[dirname].append(info)

        # 构建目录树
        dir_items = {}
        sorted_dirs = sorted(dir_groups.keys())

        # 单目录或内容少 -> 直接扁平化显示
        if len(sorted_dirs) <= 1:
            for info in sorted(files, key=lambda x: x.get('modified', 0), reverse=True):
                self._add_file_item(None, info, zone_color)
        else:
            # 多目录分组显示（纯文字，无 emoji 图标）
            for dir_path in sorted_dirs:
                dir_name = os.path.basename(dir_path) or dir_path
                dir_item = QTreeWidgetItem([f"  {dir_name}"])
                dir_item.setData(0, Qt.UserRole, dir_path)
                dir_item.setData(0, Qt.UserRole + 1, 'folder')
                dir_item.setForeground(0, QColor(29, 29, 31, 240))
                font = dir_item.font(0)
                font.setBold(True)
                font.setPointSize(12)
                dir_item.setFont(0, font)
                self.tree.addTopLevelItem(dir_item)
                dir_items[dir_path] = dir_item

                for info in sorted(dir_groups[dir_path], key=lambda x: x.get('modified', 0), reverse=True):
                    self._add_file_item(dir_item, info, zone_color)
            # 自动展开前3个
            for i, (dp, it) in enumerate(dir_items.items()):
                if i < 3:
                    it.setExpanded(True)

        # 计算高度
        item_count = self.tree.topLevelItemCount()
        if item_count == 0:
            empty = QTreeWidgetItem(["  暂无文件"])
            empty.setForeground(0, QColor(110, 110, 115, 200))
            self.tree.addTopLevelItem(empty)
            self.setFixedHeight(180)
        else:
            total = 0
            max_visible = 10
            visible = min(item_count, max_visible)
            # 估算：每个顶级项目 ~28px，嵌套的 ~26px
            def count_visible(item, depth=0):
                cnt = 1
                if item.isExpanded():
                    for i in range(item.childCount()):
                        cnt += count_visible(item.child(i), depth + 1)
                return cnt
            total_vis = 0
            for i in range(min(item_count, max_visible)):
                total_vis += count_visible(self.tree.topLevelItem(i))
            calc_h = 94 + min(total_vis, 14) * 28
            self.setFixedHeight(min(max(calc_h, 180), 420))

    def _add_file_item(self, parent, info, zone_color):
        name = info.get('name', '未知')
        size_kb = info.get('size', 0) / 1024
        if size_kb < 1024:
            size_str = f"{size_kb:.0f} KB"
        else:
            size_str = f"{size_kb / 1024:.1f} MB"

        # 纯文字标签，无分类 emoji
        label = f"  {name}"
        item = QTreeWidgetItem([label])
        item.setData(0, Qt.UserRole, info.get('path', ''))
        item.setData(0, Qt.UserRole + 1, 'file')
        sub_font = item.font(0)
        sub_font.setPointSize(11)
        sub_font.setBold(False)
        item.setFont(0, sub_font)
        item.setToolTip(0, f"{name}\n大小: {size_str}\n路径: {info.get('path', '')}")
        if parent is None:
            self.tree.addTopLevelItem(item)
        else:
            parent.addChild(item)

    def _on_item_activated(self, item, column):
        kind = item.data(0, Qt.UserRole + 1)
        path = item.data(0, Qt.UserRole)
        if kind == 'file' and path:
            self.file_activated.emit(path)
            try:
                if sys.platform == 'win32':
                    os.startfile(path)
                elif sys.platform == 'darwin':
                    subprocess.Popen(['open', path])
                else:
                    subprocess.Popen(['xdg-open', path])
            except Exception:
                pass

    def _on_item_single_click(self, item, column):
        kind = item.data(0, Qt.UserRole + 1)
        if kind == 'folder':
            # 点击文件夹切换展开
            item.setExpanded(not item.isExpanded())

    def show_above(self, anchor_global, offset_x=0):
        """显示在锚点上方（Dock 栏按钮正上方居中）"""
        self._target_anchor = anchor_global
        w = self.width()
        h = self.height()
        # 居中于按钮上方
        x = anchor_global.x() - w // 2 - offset_x
        y = anchor_global.y() - h - 12

        # 屏幕边界约束
        from PyQt5.QtWidgets import QApplication
        screen = QApplication.primaryScreen().availableGeometry()
        if x < screen.left() + 4:
            x = screen.left() + 4
        if x + w > screen.right() - 4:
            x = screen.right() - w - 4
        if y < screen.top() + 4:
            y = anchor_global.y() + h + 12

        self.move(x, y)

        # 淡入
        if self._fade_anim is not None:
            self._fade_anim.stop()
        self._fade_anim = QPropertyAnimation(self._opacity_effect, b"opacity")
        self._fade_anim.setDuration(180)
        self._fade_anim.setStartValue(0.0)
        self._fade_anim.setEndValue(1.0)
        self._fade_anim.setEasingCurve(QEasingCurve.OutCubic)
        self.show()
        self._fade_anim.start()

        # 重置自动隐藏
        self._auto_hide_timer.stop()

    def fade_out(self):
        if not self.isVisible():
            return
        if self._fade_anim is not None:
            self._fade_anim.stop()
        self._fade_anim = QPropertyAnimation(self._opacity_effect, b"opacity")
        self._fade_anim.setDuration(140)
        self._fade_anim.setStartValue(1.0)
        self._fade_anim.setEndValue(0.0)
        self._fade_anim.setEasingCurve(QEasingCurve.InCubic)

        def on_fin():
            self.hide()
        self._fade_anim.finished.connect(on_fin)
        self._fade_anim.start()

    def restart_auto_hide(self, delay_ms=300):
        """鼠标离开按钮后启动自动隐藏；若鼠标又进入面板则取消"""
        self._auto_hide_timer.stop()
        self._auto_hide_timer.start(delay_ms)

    def enterEvent(self, event):
        # 鼠标在面板内部，停止自动隐藏
        self._auto_hide_timer.stop()

    def leaveEvent(self, event):
        # 离开面板，快速收起
        self._auto_hide_timer.start(180)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), Qt.transparent)

        path = QPainterPath()
        rect_path = QRectF(self.rect()).adjusted(0.5, 0.5, -0.5, -0.5)
        path.addRoundedRect(rect_path, 18, 18)

        # Liquid Glass 浅色磨砂玻璃背景（Apple 风）
        bg = QLinearGradient(0, 0, 0, self.height())
        bg.setColorAt(0.0, QColor(250, 251, 255, 242))   # 顶：冷白
        bg.setColorAt(1.0, QColor(238, 242, 252, 248))   # 底：稍暗冷白
        painter.fillPath(path, QBrush(bg))

        # 外边框：极淡灰蓝 hairline
        painter.setPen(QPen(QColor(120, 130, 160, 55), 0.8))
        painter.drawPath(path)

        # 顶部内高光（1px 白带）
        top_path = QPainterPath()
        top_path.addRoundedRect(QRectF(5, 3, self.width() - 10, 1.2), 0.6, 0.6)
        painter.fillPath(top_path, QColor(255, 255, 255, 120))

        # 小箭头（指向下方锚点）
        if self._target_anchor.x() > 0:
            arrow_w = 14
            arrow_h = 8
            local_anchor_x = self.mapFromGlobal(self._target_anchor).x()
            cx = max(arrow_w + 8, min(self.width() - arrow_w - 8, local_anchor_x))
            by = self.height()
            painter.setPen(Qt.NoPen)
            arrow_path = QPainterPath()
            arrow_path.moveTo(cx - arrow_w / 2, by - 0.5)
            arrow_path.lineTo(cx, by - 0.5 + arrow_h)
            arrow_path.lineTo(cx + arrow_w / 2, by - 0.5)
            arrow_path.closeSubpath()
            painter.fillPath(arrow_path, QColor(238, 242, 252, 248))
            painter.setPen(QPen(QColor(120, 130, 160, 45), 0.7))
            painter.drawPath(arrow_path)


class ZoneFolderButton(QPushButton):
    """
    智能分类文件夹按钮（Dock栏上的）
    升级：Liquid Glass 3D 图标 + 鼠标悬停显示目录树弹出面板
    """

    zone_clicked = pyqtSignal(str)
    zone_hovered = pyqtSignal(object, QPoint)   # 用于在外部显示目录树
    zone_left = pyqtSignal()

    def __init__(self, zone_name, zone_config, parent=None):
        super().__init__(parent)
        self.zone_name = zone_name
        self.config = zone_config
        self.file_count = 0
        self._hovered = False
        self._pressed = False

        # 宽度 72 用于容纳文字标签
        self.setFixedSize(72, 56)
        self.setCursor(Qt.PointingHandCursor)
        self.setMouseTracking(True)
        self.setStyleSheet("background: transparent; border: none;")
        self.setProperty("baseSize", QSize(72, 56))

        self.setToolTip(f"{zone_name}（{zone_config.get('description', '')}）· 悬停查看目录")

        self.clicked.connect(lambda: self.zone_clicked.emit(self.zone_name))

    def set_file_count(self, count):
        self.file_count = count
        self.update()

    def enterEvent(self, event):
        self._hovered = True
        self.update()
        # 计算按钮中心（全局坐标）
        center = self.mapToGlobal(QPoint(self.width() // 2, 0))
        self.zone_hovered.emit(self, center)

    def leaveEvent(self, event):
        self._hovered = False
        self.update()
        self.zone_left.emit()

    def mousePressEvent(self, event):
        self._pressed = True
        self.update()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self._pressed = False
        self.update()
        super().mouseReleaseEvent(event)

    def paintEvent(self, event):
        """
        纯文字标签风格（Apple HIG：macOS Finder 侧边栏）
        - 不画文件夹形状、不画 emoji
        - 圆角矩形 + 中央文字（zone_name）
        - 统一 Apple 蓝 #0A84FF 作为 accent 色
        - 悬停：背景稍亮 + 轻微上浮
        - 按压：背景变蓝 accent + 文字变白
        """
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)

        rect = self.rect()
        w = float(rect.width())
        h = float(rect.height())

        # Apple 统一 accent 色（不再使用 per-zone 多色）
        accent = QColor(0x0A, 0x84, 0xFF)

        # 浮动偏移（悬停上浮 2px，按压下沉 1px）
        y_offs = 0
        if self._pressed:
            y_offs = 1
        elif self._hovered:
            y_offs = -2

        painter.save()
        painter.translate(0, y_offs)

        # === 圆角矩形主体（Liquid Glass：浅色半透明 + 细边框） ===
        margin_x = 4.0
        margin_y = 6.0
        body_w = w - margin_x * 2.0
        body_h = h - margin_y * 2.0
        body_x = margin_x
        body_y = margin_y
        radius = 12.0

        body_rect = QRectF(body_x, body_y, body_w, body_h)
        body_path = QPainterPath()
        body_path.addRoundedRect(body_rect, radius, radius)

        # 背景填充：根据状态切换
        if self._pressed:
            # 按压：accent 蓝填充
            bg = QLinearGradient(0, body_y, 0, body_y + body_h)
            bg.setColorAt(0.0, QColor(0x2E, 0x9B, 0xFF, 255))
            bg.setColorAt(1.0, QColor(0x0A, 0x84, 0xFF, 255))
            painter.setPen(Qt.NoPen)
            painter.fillPath(body_path, QBrush(bg))
            border_color = QColor(0x0A, 0x84, 0xFF, 255)
        elif self._hovered:
            # 悬停：稍亮的浅色玻璃
            bg = QLinearGradient(0, body_y, 0, body_y + body_h)
            bg.setColorAt(0.0, QColor(255, 255, 255, 248))
            bg.setColorAt(1.0, QColor(245, 247, 252, 244))
            painter.setPen(Qt.NoPen)
            painter.fillPath(body_path, QBrush(bg))
            border_color = QColor(0x0A, 0x84, 0xFF, 140)
        else:
            # 默认：极浅玻璃
            bg = QLinearGradient(0, body_y, 0, body_y + body_h)
            bg.setColorAt(0.0, QColor(255, 255, 255, 220))
            bg.setColorAt(1.0, QColor(244, 246, 250, 210))
            painter.setPen(Qt.NoPen)
            painter.fillPath(body_path, QBrush(bg))
            border_color = QColor(120, 130, 160, 70)

        # 细边框
        painter.setPen(QPen(border_color, 0.8))
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(body_path)

        # 顶部内高光（仅默认/悬停状态，按压时不画）
        if not self._pressed:
            hl = QRectF(body_x + 4.0, body_y + 1.5, body_w - 8.0, 1.0)
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 120))
            painter.drawRoundedRect(hl, 0.5, 0.5)

        # === 中央文字标签（zone_name） ===
        # 按压时文字变白，否则用 #1D1D1F
        if self._pressed:
            text_color = QColor(255, 255, 255, 255)
        else:
            text_color = QColor(0x1D, 0x1D, 0x1F, 240)

        f = QFont()
        f.setPointSizeF(13.0)
        f.setWeight(QFont.DemiBold)
        f.setStyleStrategy(QFont.PreferAntialias)
        painter.setFont(f)
        painter.setPen(text_color)

        # 给文字留出右侧角标空间
        text_rect = QRectF(body_x + 2.0, body_y, body_w - 4.0, body_h)
        painter.drawText(text_rect, Qt.AlignCenter, self.zone_name)

        painter.restore()

        # === 角标：文件计数（Apple 蓝，不再用红色） ===
        if self.file_count > 0:
            badge_text = str(self.file_count) if self.file_count < 100 else "99+"
            if len(badge_text) == 1:
                bw, bh = 16.0, 16.0
            elif len(badge_text) == 2:
                bw, bh = 20.0, 16.0
            else:
                bw, bh = 25.0, 16.0
            # 角标放在右上角内侧
            bx = w - bw - 5.0
            by = 3.0
            badge_rect = QRectF(bx, by, bw, bh)

            painter.setPen(Qt.NoPen)
            # 按压状态下角标变白底蓝字以保持对比；否则 Apple 蓝底白字
            if self._pressed:
                painter.setBrush(QColor(255, 255, 255, 235))
            else:
                painter.setBrush(QColor(0x0A, 0x84, 0xFF, 235))
            painter.drawRoundedRect(badge_rect, bh / 2.0, bh / 2.0)

            painter.setPen(QPen(QColor(255, 255, 255, 130), 0.7))
            painter.setBrush(Qt.NoBrush)
            painter.drawRoundedRect(badge_rect, bh / 2.0, bh / 2.0)

            bf = QFont()
            bf.setPointSizeF(8.5 if len(badge_text) == 1 else 7.5)
            bf.setWeight(QFont.Bold)
            bf.setStyleStrategy(QFont.PreferAntialias)
            painter.setFont(bf)
            if self._pressed:
                painter.setPen(QColor(0x0A, 0x84, 0xFF, 255))
            else:
                painter.setPen(QColor(255, 255, 255, 255))
            painter.drawText(badge_rect, Qt.AlignCenter, badge_text)

    @staticmethod
    def _mix_color(a: QColor, b: QColor, t: float) -> QColor:
        """在 a 与 b 之间线性插值（t=0 → a, t=1 → b）"""
        t = max(0.0, min(1.0, t))
        return QColor(
            int(a.red()   + (b.red()   - a.red())   * t),
            int(a.green() + (b.green() - a.green()) * t),
            int(a.blue()  + (b.blue()  - a.blue())  * t),
            int(a.alpha() + (b.alpha() - a.alpha()) * t),
        )


class ZonePanel(QWidget):
    """智能分类面板 - 点击Dock上的文件夹后弹出"""

    open_folder = pyqtSignal(str)
    open_file = pyqtSignal(str)

    def __init__(self, smart_engine=None, file_index=None, parent=None):
        super().__init__(parent)
        self.engine = smart_engine or SmartRuleEngine()
        self.file_index = file_index
        self.current_zone = None

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Popup |
            Qt.NoDropShadowWindowHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedWidth(380)
        self.setMaximumHeight(480)

        self._setup_ui()

    def _setup_ui(self):
        # 背景容器 - Apple 浅色磨砂玻璃
        container = QWidget(self)
        container.setStyleSheet("""
            QWidget {
                background: rgba(250, 251, 255, 0.96);
                border: 1px solid rgba(120, 130, 160, 0.18);
                border-radius: 18px;
            }
        """)

        layout = QVBoxLayout(container)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        # 标题栏（纯文字，无 emoji 图标）
        header = QHBoxLayout()
        self.title_label = QLabel("智能分类")
        self.title_label.setStyleSheet("font-size: 18px; font-weight: 700; color: #1D1D1F; background: transparent; border: none;")
        header.addWidget(self.title_label)
        header.addStretch()

        self.count_label = QLabel("0 个文件")
        self.count_label.setStyleSheet("font-size: 12px; color: #6E6E73; background: transparent; border: none;")
        header.addWidget(self.count_label)

        layout.addLayout(header)

        # 分隔线
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background: rgba(120, 130, 160, 0.14); border: none; max-height: 1px;")
        layout.addWidget(line)

        # 文件列表 - 深色文字 + Apple 风悬停
        self.file_list = QListWidget()
        self.file_list.setStyleSheet("""
            QListWidget {
                background: transparent;
                border: none;
                outline: none;
                color: #1D1D1F;
            }
            QListWidget::item {
                background: rgba(120, 130, 160, 0.05);
                border-radius: 9px;
                padding: 8px 10px;
                margin: 2px 0;
            }
            QListWidget::item:hover {
                background: rgba(10, 132, 255, 0.10);
                border: 1px solid rgba(10, 132, 255, 0.18);
            }
            QListWidget::item:selected {
                background: rgba(10, 132, 255, 0.18);
                color: #0A84FF;
            }
        """)
        self.file_list.itemDoubleClicked.connect(self._on_file_double_clicked)
        layout.addWidget(self.file_list, 1)

        # 底部操作 - Apple 蓝按钮（纯文字）
        footer = QHBoxLayout()
        open_folder_btn = QPushButton("打开文件夹")
        open_folder_btn.setFixedHeight(36)
        open_folder_btn.setCursor(Qt.PointingHandCursor)
        open_folder_btn.setStyleSheet("""
            QPushButton {
                background: rgba(10, 132, 255, 0.14);
                border: 1px solid rgba(10, 132, 255, 0.25);
                border-radius: 10px;
                color: #0A84FF;
                font-size: 13px;
                font-weight: 600;
                padding: 8px 18px;
            }
            QPushButton:hover {
                background: rgba(10, 132, 255, 0.24);
                border: 1px solid rgba(10, 132, 255, 0.40);
            }
            QPushButton:pressed {
                background: rgba(10, 132, 255, 0.35);
            }
        """)
        open_folder_btn.clicked.connect(self._on_open_folder)
        footer.addWidget(open_folder_btn)

        layout.addLayout(footer)

        # 调整容器大小
        container.setGeometry(0, 0, 380, 480)

    def show_zone(self, zone_name, pos):
        """显示某个分类的面板"""
        self.current_zone = zone_name

        zone_config = self.engine.get_all_zones().get(zone_name, {})
        # Apple HIG：统一使用 Apple 蓝，不再使用 per-zone 颜色/emoji 图标
        _color = zone_config.get('color', '#0A84FF')
        _icon = zone_config.get('icon', '')

        self.title_label.setText(zone_name)

        # 加载文件列表
        self._load_files(zone_name)

        # 定位
        self.move(pos.x() - 380 // 2, pos.y() - 480 - 10)

        # 淡入动画
        self.show()

    def _load_files(self, zone_name):
        """加载某个分类下的文件（从桌面扫描，虚拟分类）"""
        self.file_list.clear()

        files = []

        # 优先从文件索引获取
        if self.file_index:
            all_files = self.file_index.index
            for filepath, info in all_files.items():
                zone, _ = self.engine.classify(filepath)
                if zone == zone_name:
                    files.append(info)
        else:
            # 直接从桌面扫描（虚拟分类模式）
            from core.desktop_watcher import DesktopWatcher
            watcher = DesktopWatcher(self.engine)
            desktop_path = watcher.desktop_path
            if os.path.exists(desktop_path):
                for filename in os.listdir(desktop_path):
                    filepath = os.path.join(desktop_path, filename)
                    if os.path.isfile(filepath) and not filename.startswith('.') and not filename.startswith('~$'):
                        zone, _ = self.engine.classify(filepath)
                        if zone == zone_name:
                            try:
                                stat = os.stat(filepath)
                                files.append({
                                    'name': filename,
                                    'path': filepath,
                                    'size': stat.st_size,
                                    'modified': stat.st_mtime,
                                })
                            except OSError:
                                pass

        # 按修改时间排序
        files.sort(key=lambda x: x.get('modified', 0), reverse=True)

        self.count_label.setText(f"{len(files)} 个文件")

        # 显示前30个
        for info in files[:30]:
            item = QListWidgetItem()
            item.setText(f"  {info.get('name', '未知')}")
            item.setData(Qt.UserRole, info.get('path', ''))
            self.file_list.addItem(item)

    def _on_file_double_clicked(self, item):
        filepath = item.data(Qt.UserRole)
        if filepath and os.path.exists(filepath):
            self.open_file.emit(filepath)
            # 打开文件 - 跨平台支持
            try:
                if sys.platform == 'win32':
                    os.startfile(filepath)
                elif sys.platform == 'darwin':
                    subprocess.Popen(['open', filepath])
                else:
                    subprocess.Popen(['xdg-open', filepath])
            except Exception:
                pass

    def _on_open_folder(self):
        # 虚拟模式下打开桌面（文件都在桌面上）
        from core.desktop_watcher import DesktopWatcher
        watcher = DesktopWatcher(self.engine)
        open_path = watcher.desktop_path
        try:
            if sys.platform == 'win32':
                os.startfile(open_path)
            elif sys.platform == 'darwin':
                subprocess.Popen(['open', open_path])
            else:
                subprocess.Popen(['xdg-open', open_path])
        except Exception:
            pass

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), Qt.transparent)
