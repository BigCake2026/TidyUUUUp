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


CATEGORY_FOLDER_ICONS = {
    '图片': '🖼️', '视频': '🎬', '音频': '🎵', '文档': '📄',
    '表格': '📊', '演示': '📽️', '压缩包': '📦', '代码': '💻',
    '可执行': '⚙️', '电子书': '📚', '字体': '🔤', '设计': '🎨',
    '3D模型': '🧊', '数据': '📋', '垃圾缓存': '🗑️', '其他': '📝'
}


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

        # 标题栏
        header = QHBoxLayout()
        header.setSpacing(10)

        self.icon_label = QLabel("📁")
        self.icon_label.setFixedSize(28, 28)
        self.icon_label.setAlignment(Qt.AlignCenter)
        self.icon_label.setStyleSheet("""
            background: rgba(100, 150, 255, 0.2);
            border-radius: 8px;
            font-size: 16px;
        """)
        header.addWidget(self.icon_label)

        self.title_label = QLabel("目录树")
        self.title_label.setStyleSheet("""
            color: white;
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
            background: rgba(100, 150, 255, 0.25);
            border: 1px solid rgba(100, 150, 255, 0.4);
            border-radius: 14px;
            padding: 2px 10px;
            color: rgba(160, 190, 255, 0.95);
            font-size: 11px;
            font-weight: 600;
        """)
        header.addWidget(self.count_badge)

        inner.addLayout(header)

        # 分隔线
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background: rgba(255,255,255,0.08); border: none; max-height: 1px;")
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
                color: rgba(240, 240, 255, 0.95);
                font-size: 12px;
                alternate-background-color: transparent;
            }
            QTreeWidget::item {
                padding: 5px 8px;
                border-radius: 7px;
                margin: 1px 0;
            }
            QTreeWidget::item:hover {
                background: rgba(100, 150, 255, 0.18);
            }
            QTreeWidget::item:selected {
                background: rgba(100, 150, 255, 0.32);
                color: white;
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
                background: rgba(255, 255, 255, 0.15);
                border-radius: 3px;
                min-height: 24px;
            }
            QScrollBar::handle:vertical:hover {
                background: rgba(255, 255, 255, 0.28);
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
        tip.setStyleSheet("color: rgba(255,255,255,0.35); font-size: 10px; background: transparent;")
        inner.addWidget(tip)

        layout.addWidget(container)

    def populate_from_files(self, files, zone_name, zone_icon, zone_color):
        """
        根据文件列表填充目录树
        按子目录分组显示，无子目录则直接显示文件列表
        files: list of {name, path, size, modified, category}
        """
        self.tree.clear()
        self.title_label.setText(zone_name)
        self.icon_label.setText(zone_icon)
        self.icon_label.setStyleSheet(f"""
            background: {zone_color}40;
            border-radius: 8px;
            font-size: 16px;
        """)
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
            # 多目录分组显示
            for dir_path in sorted_dirs:
                dir_name = os.path.basename(dir_path) or dir_path
                dir_icon = "📂"
                dir_item = QTreeWidgetItem([f"  {dir_icon}  {dir_name}"])
                dir_item.setData(0, Qt.UserRole, dir_path)
                dir_item.setData(0, Qt.UserRole + 1, 'folder')
                dir_item.setForeground(0, QColor(200, 220, 255, 240))
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
            empty = QTreeWidgetItem(["  📭  暂无文件"])
            empty.setForeground(0, QColor(255, 255, 255, 120))
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
        cat = info.get('category', '其他')
        cat_icon = CATEGORY_FOLDER_ICONS.get(cat, '📝')
        name = info.get('name', '未知')
        size_kb = info.get('size', 0) / 1024
        if size_kb < 1024:
            size_str = f"{size_kb:.0f} KB"
        else:
            size_str = f"{size_kb / 1024:.1f} MB"

        label = f"  {cat_icon}  {name}"
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

        # Liquid Glass 背景
        bg = QLinearGradient(0, 0, 0, self.height())
        bg.setColorAt(0.0, QColor(40, 45, 70, 220))
        bg.setColorAt(1.0, QColor(22, 24, 42, 240))
        painter.fillPath(path, QBrush(bg))

        # 边框高光
        painter.setPen(QPen(QColor(255, 255, 255, 55), 1))
        painter.drawPath(path)

        # 顶部内发光
        top_path = QPainterPath()
        top_path.addRoundedRect(QRectF(4, 3, self.width() - 8, 2), 2, 2)
        painter.fillPath(top_path, QColor(255, 255, 255, 38))

        # 小箭头（指向下方锚点）
        if self._target_anchor.x() > 0:
            arrow_w = 14
            arrow_h = 8
            # 相对位置
            local_anchor_x = self.mapFromGlobal(self._target_anchor).x()
            cx = max(arrow_w + 8, min(self.width() - arrow_w - 8, local_anchor_x))
            by = self.height()
            painter.setPen(Qt.NoPen)
            arrow_path = QPainterPath()
            arrow_path.moveTo(cx - arrow_w / 2, by - 0.5)
            arrow_path.lineTo(cx, by - 0.5 + arrow_h)
            arrow_path.lineTo(cx + arrow_w / 2, by - 0.5)
            arrow_path.closeSubpath()
            painter.fillPath(arrow_path, QColor(22, 24, 42, 240))
            # 箭头描边
            painter.setPen(QPen(QColor(255, 255, 255, 40), 1))
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

        self.setFixedSize(60, 60)
        self.setCursor(Qt.PointingHandCursor)
        self.setMouseTracking(True)
        self.setStyleSheet("background: transparent; border: none;")
        self.setProperty("baseSize", QSize(60, 60))

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
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        rect = self.rect()
        base_color = QColor(self.config.get('color', '#4A7FFF'))
        icon_text = self.config.get('icon', CATEGORY_FOLDER_ICONS.get(self.zone_name, '📁'))

        # --- 悬停 + 按下：浮动阴影层 ---
        if self._hovered or self._pressed:
            shadow_rect = QRect(rect.x() + 4, rect.y() + 6,
                                rect.width() - 8, rect.height() - 8)
            shadow_grad = QRadialGradient(
                shadow_rect.center().x(), shadow_rect.bottom(),
                shadow_rect.width() * 0.8
            )
            shadow_grad.setColorAt(0.0, QColor(base_color.red(), base_color.green(), base_color.blue(),
                                              90 if self._pressed else 55))
            shadow_grad.setColorAt(1.0, Qt.transparent)
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow_grad))
            painter.drawEllipse(shadow_rect)

        # --- 浮动缩放：hover 轻微上浮 ---
        scale = 1.0
        y_offs = 0
        if self._pressed:
            scale = 0.94
            y_offs = 1
        elif self._hovered:
            scale = 1.04
            y_offs = -2

        painter.save()
        cx = rect.width() / 2.0
        cy = rect.height() / 2.0 + y_offs
        painter.translate(cx, cy)
        painter.scale(scale, scale)
        painter.translate(-cx, -cy)

        # ---- 文件夹形状：真正的 macOS/Liquid Glass 风格 ----
        w = rect.width()
        h = rect.height()

        # 主体圆角矩形尺寸
        body_w = w - 10
        body_h = h - 20
        body_x = 5
        body_y = 14
        radius = 10

        # 顶部标签（文件夹盖的小舌头）
        tab_w = body_w * 0.42
        tab_h = 9
        tab_x = body_x + 1
        tab_y = 7
        tab_r = 4

        # 1. 文件夹盖（主体 + 标签一体：先画主体上面略短，舌头单独覆盖）
        # 主体（底部）
        body_grad = QLinearGradient(0, body_y, 0, body_y + body_h)
        body_grad.setColorAt(0.0, base_color.lighter(145))
        body_grad.setColorAt(0.35, base_color.lighter(115))
        body_grad.setColorAt(1.0, base_color.darker(118))

        path_body = QPainterPath()
        path_body.addRoundedRect(QRectF(body_x, body_y, body_w, body_h), radius, radius)

        # 文件夹顶部舌头路径（和主体合并）
        path_tab = QPainterPath()
        path_tab.addRoundedRect(QRectF(tab_x, tab_y, tab_w, tab_h + 3), tab_r, tab_r)

        # 合并并减去重叠的上边缘直线 → 画为整体 Liquid Glass 物体
        folder_path = path_body.united(path_tab)
        painter.setPen(Qt.NoPen)
        painter.fillPath(folder_path, QBrush(body_grad))

        # 2. 高光层（Liquid Glass 顶部镜面反射）
        highlight = QLinearGradient(0, body_y, 0, body_y + body_h * 0.55)
        highlight.setColorAt(0.0, QColor(255, 255, 255, 110))
        highlight.setColorAt(0.5, QColor(255, 255, 255, 35))
        highlight.setColorAt(1.0, QColor(255, 255, 255, 0))
        painter.setClipRect(body_x + 2, body_y + 2, body_w - 4, body_h * 0.6)
        painter.fillPath(folder_path, QBrush(highlight))
        painter.setClipping(False)

        # 3. 底部内阴影（增强立体感）
        shadow_grad2 = QLinearGradient(0, body_y + body_h - 10, 0, body_y + body_h)
        shadow_grad2.setColorAt(0.0, QColor(0, 0, 0, 0))
        shadow_grad2.setColorAt(1.0, QColor(0, 0, 0, 60))
        painter.setClipRect(body_x + 2, body_y + body_h - 10, body_w - 4, 10)
        painter.fillPath(folder_path, QBrush(shadow_grad2))
        painter.setClipping(False)

        # 4. 描边（半透明外框 + 内部高光描边）
        outline_pen = QPen(QColor(0, 0, 0, 60), 1.1)
        painter.setPen(outline_pen)
        painter.drawPath(folder_path)

        inner_light = QPen(QColor(255, 255, 255, 60), 0.6)
        inner_light_rect = QRectF(body_x + 1.5, body_y + 1.5, body_w - 3, body_h - 3)
        inner_path = QPainterPath()
        inner_path.addRoundedRect(inner_light_rect, max(radius - 1, 1), max(radius - 1, 1))
        painter.setPen(inner_light)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(inner_path)

        # 5. 文件夹内部：浅色块 + 图标
        inner_body = QRectF(body_x + 4, body_y + 6, body_w - 8, body_h - 12)
        inner_grad = QLinearGradient(0, inner_body.top(), 0, inner_body.bottom())
        inner_grad.setColorAt(0.0, QColor(255, 255, 255, 28))
        inner_grad.setColorAt(1.0, QColor(0, 0, 0, 18))
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(inner_grad))
        painter.drawRoundedRect(inner_body, 6, 6)

        # 图标（大号居中 + 白色带投影）
        painter.setPen(QColor(0, 0, 0, 60))
        f = QFont()
        f.setPointSize(14)
        f.setBold(True)
        painter.setFont(f)
        painter.drawText(inner_body.translated(0, 1), Qt.AlignCenter, icon_text)
        painter.setPen(QColor(255, 255, 255, 245))
        painter.drawText(inner_body, Qt.AlignCenter, icon_text)

        painter.restore()

        # --- 文件数量角标（右上角，不随缩放变形）---
        if self.file_count > 0:
            badge_text = str(self.file_count) if self.file_count < 100 else "99+"
            if len(badge_text) == 1:
                badge_w, badge_h = 18, 18
            elif len(badge_text) == 2:
                badge_w, badge_h = 22, 18
            else:
                badge_w, badge_h = 26, 18
            badge_x = w - badge_w + 2
            badge_y = -1

            # 红色渐变徽章
            badge_path = QPainterPath()
            badge_path.addRoundedRect(QRectF(badge_x, badge_y, badge_w, badge_h), badge_h / 2, badge_h / 2)

            badge_grad = QLinearGradient(0, badge_y, 0, badge_y + badge_h)
            badge_grad.setColorAt(0.0, QColor(255, 110, 110, 250))
            badge_grad.setColorAt(1.0, QColor(230, 55, 65, 255))
            painter.fillPath(badge_path, QBrush(badge_grad))

            # 徽章高光
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 55))
            hl_rect = QRectF(badge_x + 2, badge_y + 1.5, badge_w - 4, badge_h * 0.35)
            painter.drawRoundedRect(hl_rect, badge_h * 0.18, badge_h * 0.18)

            # 徽章外描边
            painter.setPen(QPen(QColor(0, 0, 0, 50), 0.8))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(badge_path)

            # 数字
            painter.setPen(QColor(255, 255, 255))
            bf = QFont()
            bf.setPointSize(9 if len(badge_text) == 1 else 8)
            bf.setBold(True)
            bf.setStyleStrategy(QFont.PreferAntialias)
            painter.setFont(bf)
            painter.drawText(QRectF(badge_x, badge_y, badge_w, badge_h),
                             Qt.AlignCenter, badge_text)


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
        # 背景容器
        container = QWidget(self)
        container.setStyleSheet("""
            QWidget {
                background: rgba(25, 25, 45, 0.95);
                backdrop-filter: blur(30px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 18px;
            }
        """)

        layout = QVBoxLayout(container)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        # 标题栏
        header = QHBoxLayout()
        self.icon_label = QLabel("📁")
        self.icon_label.setStyleSheet("font-size: 24px; background: transparent; border: none;")
        header.addWidget(self.icon_label)

        self.title_label = QLabel("智能分类")
        self.title_label.setStyleSheet("font-size: 18px; font-weight: 700; color: white; background: transparent; border: none;")
        header.addWidget(self.title_label)
        header.addStretch()

        self.count_label = QLabel("0 个文件")
        self.count_label.setStyleSheet("font-size: 12px; color: rgba(255,255,255,0.5); background: transparent; border: none;")
        header.addWidget(self.count_label)

        layout.addLayout(header)

        # 分隔线
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background: rgba(255,255,255,0.08); border: none; max-height: 1px;")
        layout.addWidget(line)

        # 文件列表
        self.file_list = QListWidget()
        self.file_list.setStyleSheet("""
            QListWidget {
                background: transparent;
                border: none;
                outline: none;
                color: white;
            }
            QListWidget::item {
                background: rgba(255,255,255,0.04);
                border-radius: 8px;
                padding: 6px 8px;
                margin: 2px 0;
            }
            QListWidget::item:hover {
                background: rgba(255,255,255,0.1);
            }
        """)
        self.file_list.itemDoubleClicked.connect(self._on_file_double_clicked)
        layout.addWidget(self.file_list, 1)

        # 底部操作
        footer = QHBoxLayout()
        open_folder_btn = QPushButton("📂  打开文件夹")
        open_folder_btn.setFixedHeight(36)
        open_folder_btn.setCursor(Qt.PointingHandCursor)
        open_folder_btn.setStyleSheet("""
            QPushButton {
                background: rgba(100, 150, 255, 0.25);
                border: 1px solid rgba(100, 150, 255, 0.4);
                border-radius: 8px;
                color: white;
                font-size: 13px;
                font-weight: 500;
            }
            QPushButton:hover {
                background: rgba(120, 170, 255, 0.4);
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
        color = zone_config.get('color', '#4A7FFF')
        icon = zone_config.get('icon', '📁')

        self.icon_label.setText(icon)
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
