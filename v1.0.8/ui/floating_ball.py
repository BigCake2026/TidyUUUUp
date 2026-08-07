"""
悬浮球组件 - Floating Ball (Liquid Glass Pro)
不用时缩成小圆球，不占空间

升级特性 (Apple Liquid Glass):
- 弹性吸附: 使用 Spring 物理模型吸附到屏幕边缘
- 液态呼吸: 平滑的多层光晕脉动
- Q弹放大: 悬停时弹性放大, 带 OutElastic 回弹
- 鼠标响应: 光晕跟随鼠标移动

性能优化:
- 智能定时器管理 (无变化时自动停止, 避免空转 CPU)
- 收敛检测 (插值到位后停止重绘)
- 隐藏时暂停动画
- 修复 setFixedSize 阻止 size 动画的 bug (改用 geometry 动画)
"""
import math
from PyQt5.QtCore import (
    Qt, QPoint, QSize, QTimer, QPropertyAnimation, QEasingCurve,
    pyqtSignal, QRect, QPointF
)
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import (
    QPainter, QColor, QRadialGradient, QBrush, QPen, QCursor,
    QLinearGradient
)


class FloatingBall(QWidget):
    """悬浮小球 - Liquid Glass Pro 弹性吸附 + 液态呼吸"""

    clicked = pyqtSignal()
    right_clicked = pyqtSignal(QPoint)
    double_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)

        self._base_size = 48
        # 注意: 不用 setFixedSize, 否则 size 动画无效
        self.setMinimumSize(1, 1)
        self.setMaximumSize(200, 200)
        self.resize(self._base_size, self._base_size)

        self._is_dragging = False
        self._drag_offset = QPoint()
        self._is_hovered = False

        # 液态呼吸状态 (平滑插值)
        self._breath_phase = 0.0
        self._hover_strength = 0.0
        self._target_hover = 0.0
        self._glow_x = 0.5  # 光晕跟随鼠标 (归一化)
        self._glow_y = 0.5
        self._target_glow_x = 0.5
        self._target_glow_y = 0.5

        # 60fps 液态动画驱动器 (智能启停)
        self._liquid_timer = QTimer(self)
        self._liquid_timer.setInterval(16)  # ~60fps
        self._liquid_timer.timeout.connect(self._tick_liquid)
        # 呼吸动画用独立慢速定时器 (2fps 即可, 省电)
        self._breath_timer = QTimer(self)
        self._breath_timer.setInterval(50)  # 20fps 呼吸
        self._breath_timer.timeout.connect(self._tick_breath)
        self._breath_timer.start()

        # 默认位置：右下角
        screen = QApplication.primaryScreen().geometry()
        self.move(screen.width() - self._base_size - 20,
                  screen.height() - self._base_size - 100)

        self.setCursor(Qt.PointingHandCursor)
        self.setMouseTracking(True)

        # 动画对象引用 (防止被 GC)
        self._scale_anim = None
        self._pulse_anim = None
        self._snap_anim = None

    def _tick_breath(self):
        """呼吸动画 - 慢速正弦, 始终运行"""
        self._breath_phase = (self._breath_phase + 0.04) % (2 * math.pi)
        self.update()

    def _tick_liquid(self):
        """液态动画主循环 - 苹果级平滑插值 (智能停止)"""
        # 悬停强度插值 (factor=0.18 苹果默认)
        hover_diff = self._target_hover - self._hover_strength
        self._hover_strength += hover_diff * 0.18

        # 光晕位置插值 (factor=0.15 更丝滑)
        glow_dx = self._target_glow_x - self._glow_x
        glow_dy = self._target_glow_y - self._glow_y
        self._glow_x += glow_dx * 0.15
        self._glow_y += glow_dy * 0.15

        # 收敛检测 - 全部到位则停止定时器 (省 CPU)
        if (abs(hover_diff) < 0.003 and
            abs(glow_dx) < 0.002 and
            abs(glow_dy) < 0.002):
            self._hover_strength = self._target_hover
            self._glow_x = self._target_glow_x
            self._glow_y = self._target_glow_y
            self._liquid_timer.stop()
            self.update()  # 最后一次更新
        else:
            self.update()

    def _ensure_liquid_running(self):
        """确保液态动画定时器在运行"""
        if not self._liquid_timer.isActive():
            self._liquid_timer.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        rect = self.rect()
        w = rect.width()
        h = rect.height()
        # 使用当前实际尺寸而非 _base_size, 适配缩放
        current_size = min(w, h)
        center_x = w / 2
        center_y = h / 2

        # ===== 液态呼吸光晕 (多层) =====
        breath = 0.5 + 0.5 * math.sin(self._breath_phase)
        hover_boost = self._hover_strength * 0.5
        glow_intensity = breath * 0.4 + hover_boost

        glow_size = 10 + glow_intensity * 12

        # 第1层: 外层大光晕
        outer_glow = QRadialGradient(center_x, center_y,
                                     current_size / 2 + glow_size * 2)
        alpha_outer = int(60 * glow_intensity)
        outer_glow.setColorAt(0.0, QColor(100, 150, 255, alpha_outer))
        outer_glow.setColorAt(0.5, QColor(150, 100, 255, int(alpha_outer * 0.4)))
        outer_glow.setColorAt(1.0, QColor(150, 100, 255, 0))
        painter.setBrush(QBrush(outer_glow))
        painter.setPen(Qt.NoPen)
        outer_rect = QRect(
            int(center_x - current_size / 2 - glow_size * 2),
            int(center_y - current_size / 2 - glow_size * 2),
            int(current_size + glow_size * 4),
            int(current_size + glow_size * 4)
        )
        painter.drawEllipse(outer_rect)

        # 第2层: 中层光晕
        mid_glow = QRadialGradient(center_x, center_y,
                                   current_size / 2 + glow_size)
        alpha_mid = int(120 * glow_intensity)
        mid_glow.setColorAt(0.0, QColor(120, 160, 255, alpha_mid))
        mid_glow.setColorAt(0.6, QColor(160, 120, 255, int(alpha_mid * 0.5)))
        mid_glow.setColorAt(1.0, QColor(160, 120, 255, 0))
        painter.setBrush(QBrush(mid_glow))
        mid_rect = QRect(
            int(center_x - current_size / 2 - glow_size),
            int(center_y - current_size / 2 - glow_size),
            int(current_size + glow_size * 2),
            int(current_size + glow_size * 2)
        )
        painter.drawEllipse(mid_rect)

        # ===== 球体主体 - Liquid Glass 多层渲染 =====
        glow_cx = self._glow_x * w
        glow_cy = self._glow_y * h

        # 玻璃主体渐变 (偏移光源到鼠标位置)
        ball_gradient = QRadialGradient(
            glow_cx - 6, glow_cy - 6, 0,
            center_x, center_y, current_size / 2
        )
        if self._is_hovered:
            ball_gradient.setColorAt(0.0, QColor(200, 220, 255, 255))
            ball_gradient.setColorAt(0.4, QColor(130, 160, 255, 240))
            ball_gradient.setColorAt(1.0, QColor(80, 100, 220, 230))
        else:
            ball_gradient.setColorAt(0.0, QColor(170, 190, 245, 245))
            ball_gradient.setColorAt(0.4, QColor(110, 140, 235, 235))
            ball_gradient.setColorAt(1.0, QColor(60, 80, 200, 225))

        painter.setBrush(QBrush(ball_gradient))
        painter.setPen(QPen(QColor(255, 255, 255, 80), 1))
        painter.drawEllipse(2, 2, current_size - 4, current_size - 4)

        # ===== 鼠标响应式内光晕 (悬停时增强) =====
        if self._hover_strength > 0.05:
            inner_glow = QRadialGradient(
                QPointF(glow_cx, glow_cy),
                current_size * 0.6
            )
            inner_alpha = int(80 * self._hover_strength)
            inner_glow.setColorAt(0.0, QColor(255, 255, 255, inner_alpha))
            inner_glow.setColorAt(0.4, QColor(200, 220, 255, int(inner_alpha * 0.5)))
            inner_glow.setColorAt(1.0, QColor(200, 220, 255, 0))
            painter.setBrush(QBrush(inner_glow))
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(2, 2, current_size - 4, current_size - 4)

        # ===== 顶部镜面高光 (Specular Sheen) =====
        highlight = QRadialGradient(
            center_x - 10, center_y - 12, 0,
            center_x - 8, center_y - 10, 18
        )
        highlight.setColorAt(0.0, QColor(255, 255, 255, 220))
        highlight.setColorAt(0.5, QColor(255, 255, 255, 80))
        highlight.setColorAt(1.0, QColor(255, 255, 255, 0))
        painter.setBrush(QBrush(highlight))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(int(center_x - 18), int(center_y - 20), 22, 22)

        # ===== 内边框 (Inner Rim) =====
        rim_alpha = 120 + int(60 * self._hover_strength)
        painter.setBrush(Qt.NoBrush)
        painter.setPen(QPen(QColor(255, 255, 255, rim_alpha), 1))
        painter.drawEllipse(3, 3, current_size - 6, current_size - 6)

        # ===== 图标 - 菱形 (带液态光泽) =====
        # 使用 int 避免 QPoint 不接受 float 的 TypeError (PyQt5 严格类型)
        cx = int(center_x)
        cy = int(center_y)
        icon_size = max(8, int(current_size * 0.27))
        painter.setPen(QPen(QColor(255, 255, 255, 240), 2))
        painter.setBrush(Qt.NoBrush)
        painter.drawPolygon(
            QPoint(cx, cy - icon_size),
            QPoint(cx + icon_size, cy),
            QPoint(cx, cy + icon_size),
            QPoint(cx - icon_size, cy)
        )

    def mouseMoveEvent(self, event):
        """鼠标移动 - 更新光晕跟随位置"""
        w = max(self.width(), 1)
        h = max(self.height(), 1)
        self._target_glow_x = event.pos().x() / w
        self._target_glow_y = event.pos().y() / h
        self._ensure_liquid_running()

        if self._is_dragging and event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self._drag_offset)
        super().mouseMoveEvent(event)

    def enterEvent(self, event):
        self._is_hovered = True
        self._target_hover = 1.0
        self._ensure_liquid_running()
        # Q弹放大 - 使用 Spring 弹性动画
        self._animate_spring_scale(1.18)

    def leaveEvent(self, event):
        self._is_hovered = False
        self._target_hover = 0.0
        self._ensure_liquid_running()
        # 弹性恢复
        self._animate_spring_scale(1.0)

        # 如果没在拖动，吸附到屏幕边缘
        if not self._is_dragging:
            QTimer.singleShot(150, self._snap_to_edge_spring)

    def _animate_spring_scale(self, scale):
        """Spring 物理弹性缩放 - 通过 geometry 动画 (避免 setFixedSize 冲突)"""
        new_size = int(self._base_size * scale)
        # 保持中心位置不变
        cur_geo = self.geometry()
        cx = cur_geo.center().x()
        cy = cur_geo.center().y()
        new_geo = QRect(cx - new_size // 2, cy - new_size // 2, new_size, new_size)

        # 停止之前的缩放动画
        if self._scale_anim is not None:
            self._scale_anim.stop()

        anim = QPropertyAnimation(self, b"geometry")
        anim.setDuration(400)
        anim.setStartValue(cur_geo)
        anim.setEndValue(new_geo)

        curve = QEasingCurve(QEasingCurve.OutElastic)
        curve.setAmplitude(1.2)
        curve.setPeriod(0.4)
        anim.setEasingCurve(curve)

        # 保持动画对象存活 (防止 GC)
        self._scale_anim = anim
        anim.start()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = True
            self._drag_offset = event.globalPos() - self.frameGeometry().topLeft()
            # 按下 Q弹缩小
            self._animate_spring_scale(0.92)
        elif event.button() == Qt.RightButton:
            self.right_clicked.emit(event.globalPos())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self._is_dragging:
            self._is_dragging = False
            # 释放 Q弹回弹
            if self._is_hovered:
                self._animate_spring_scale(1.18)
            else:
                self._animate_spring_scale(1.0)
            self._snap_to_edge_spring()

    def mouseDoubleClickEvent(self, event):
        # 双击 Q弹脉冲
        self._bounce_pulse()
        self.double_clicked.emit()

    def _bounce_pulse(self):
        """双击 Q弹脉冲 - Liquid Glass 弹性放大"""
        if self._pulse_anim is not None:
            self._pulse_anim.stop()

        original = self.geometry()
        expand = 8

        # 快速放大
        anim1 = QPropertyAnimation(self, b"geometry")
        anim1.setDuration(120)
        anim1.setStartValue(original)
        anim1.setEndValue(original.adjusted(-expand, -expand, expand, expand))
        anim1.setEasingCurve(QEasingCurve.OutQuad)

        # Q弹回弹 (OutElastic)
        anim2 = QPropertyAnimation(self, b"geometry")
        anim2.setDuration(450)
        anim2.setStartValue(original.adjusted(-expand, -expand, expand, expand))
        anim2.setEndValue(original)
        curve = QEasingCurve(QEasingCurve.OutElastic)
        curve.setAmplitude(1.4)
        curve.setPeriod(0.35)
        anim2.setEasingCurve(curve)

        from PyQt5.QtCore import QSequentialAnimationGroup
        group = QSequentialAnimationGroup(self)
        group.addAnimation(anim1)
        group.addAnimation(anim2)
        self._pulse_anim = group
        group.start()

    def _snap_to_edge_spring(self):
        """弹性吸附到屏幕边缘 - Spring 物理模型"""
        screen = QApplication.primaryScreen().availableGeometry()
        geo = self.frameGeometry()

        # 计算距离各边的距离
        left_dist = geo.left() - screen.left()
        right_dist = screen.right() - geo.right()
        top_dist = geo.top() - screen.top()
        bottom_dist = screen.bottom() - geo.bottom()

        # 找到最近的边
        min_dist = min(left_dist, right_dist, top_dist, bottom_dist)

        target_x = geo.x()
        target_y = geo.y()

        margin = 2

        if min_dist == left_dist:
            target_x = screen.left() + margin
        elif min_dist == right_dist:
            target_x = screen.right() - geo.width() - margin
        elif min_dist == top_dist:
            target_y = screen.top() + margin
        else:
            target_y = screen.bottom() - geo.height() - margin

        # 如果已经接近目标位置, 不需要动画
        if abs(target_x - geo.x()) < 2 and abs(target_y - geo.y()) < 2:
            return

        # 停止之前的吸附动画
        if self._snap_anim is not None:
            self._snap_anim.stop()

        # Spring 物理弹性吸附
        anim = QPropertyAnimation(self, b"pos")
        anim.setDuration(500)
        anim.setStartValue(self.pos())
        anim.setEndValue(QPoint(target_x, target_y))

        # 使用 OutBack 带轻微过冲的弹性曲线
        curve = QEasingCurve(QEasingCurve.OutBack)
        curve.setOvershoot(0.8)
        anim.setEasingCurve(curve)

        self._snap_anim = anim
        anim.start()

    def hideEvent(self, event):
        """隐藏时暂停所有动画 (省电)"""
        self._breath_timer.stop()
        self._liquid_timer.stop()
        super().hideEvent(event)

    def showEvent(self, event):
        """显示时恢复呼吸动画"""
        if not self._breath_timer.isActive():
            self._breath_timer.start()
        super().showEvent(event)

    # 兼容旧调用
    def _snap_to_edge(self):
        self._snap_to_edge_spring()
