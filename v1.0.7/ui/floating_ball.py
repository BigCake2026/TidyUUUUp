"""
悬浮球组件 - Floating Ball (Liquid Glass Pro)
不用时缩成小圆球，不占空间

升级特性 (Apple Liquid Glass):
- 弹性吸附: 使用 Spring 物理模型吸附到屏幕边缘
- 液态呼吸: 平滑的多层光晕脉动
- Q弹放大: 悬停时弹性放大, 带 OutElastic 回弹
- 鼠标响应: 光晕跟随鼠标移动
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
from .animations import SpringAnimation, SmoothTween


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
        self.setFixedSize(self._base_size, self._base_size)

        self._is_dragging = False
        self._drag_offset = QPoint()
        self._is_hovered = False

        # 液态呼吸状态 (SmoothTween 平滑插值)
        self._breath_phase = 0.0
        self._hover_strength = 0.0
        self._target_hover = 0.0
        self._glow_x = 0.5  # 光晕跟随鼠标 (归一化)
        self._glow_y = 0.5
        self._target_glow_x = 0.5
        self._target_glow_y = 0.5

        # 60fps 液态动画驱动器
        self._liquid_timer = QTimer(self)
        self._liquid_timer.setInterval(16)  # ~60fps
        self._liquid_timer.timeout.connect(self._tick_liquid)
        self._liquid_timer.start()

        # 默认位置：右下角
        screen = QApplication.primaryScreen().geometry()
        self.move(screen.width() - self._base_size - 20,
                  screen.height() - self._base_size - 100)

        self.setCursor(Qt.PointingHandCursor)
        self.setMouseTracking(True)

    def _tick_liquid(self):
        """液态动画主循环 - 苹果级平滑插值"""
        # 呼吸相位 (慢速正弦)
        self._breath_phase = (self._breath_phase + 0.04) % (2 * math.pi)

        # 悬停强度插值 (factor=0.18 苹果默认)
        self._hover_strength += (self._target_hover - self._hover_strength) * 0.18

        # 光晕位置插值 (factor=0.15 更丝滑)
        self._glow_x += (self._target_glow_x - self._glow_x) * 0.15
        self._glow_y += (self._target_glow_y - self._glow_y) * 0.15

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        rect = self.rect()
        w = rect.width()
        h = rect.height()
        center_x = w / 2
        center_y = h / 2

        # ===== 液态呼吸光晕 (多层) =====
        # 慢速正弦呼吸
        breath = 0.5 + 0.5 * math.sin(self._breath_phase)
        # 悬停时增强
        hover_boost = self._hover_strength * 0.5
        glow_intensity = breath * 0.4 + hover_boost

        glow_size = 10 + glow_intensity * 12

        # 第1层: 外层大光晕
        outer_glow = QRadialGradient(center_x, center_y,
                                     self._base_size / 2 + glow_size * 2)
        alpha_outer = int(60 * glow_intensity)
        outer_glow.setColorAt(0.0, QColor(100, 150, 255, alpha_outer))
        outer_glow.setColorAt(0.5, QColor(150, 100, 255, int(alpha_outer * 0.4)))
        outer_glow.setColorAt(1.0, QColor(150, 100, 255, 0))
        painter.setBrush(QBrush(outer_glow))
        painter.setPen(Qt.NoPen)
        outer_rect = QRect(
            int(center_x - self._base_size / 2 - glow_size * 2),
            int(center_y - self._base_size / 2 - glow_size * 2),
            int(self._base_size + glow_size * 4),
            int(self._base_size + glow_size * 4)
        )
        painter.drawEllipse(outer_rect)

        # 第2层: 中层光晕
        mid_glow = QRadialGradient(center_x, center_y,
                                   self._base_size / 2 + glow_size)
        alpha_mid = int(120 * glow_intensity)
        mid_glow.setColorAt(0.0, QColor(120, 160, 255, alpha_mid))
        mid_glow.setColorAt(0.6, QColor(160, 120, 255, int(alpha_mid * 0.5)))
        mid_glow.setColorAt(1.0, QColor(160, 120, 255, 0))
        painter.setBrush(QBrush(mid_glow))
        mid_rect = QRect(
            int(center_x - self._base_size / 2 - glow_size),
            int(center_y - self._base_size / 2 - glow_size),
            int(self._base_size + glow_size * 2),
            int(self._base_size + glow_size * 2)
        )
        painter.drawEllipse(mid_rect)

        # ===== 球体主体 - Liquid Glass 多层渲染 =====
        # 鼠标响应光晕位置
        glow_cx = self._glow_x * w
        glow_cy = self._glow_y * h

        # 玻璃主体渐变 (偏移光源到鼠标位置)
        ball_gradient = QRadialGradient(
            glow_cx - 6, glow_cy - 6, 0,
            center_x, center_y, self._base_size / 2
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
        painter.drawEllipse(2, 2, self._base_size - 4, self._base_size - 4)

        # ===== 鼠标响应式内光晕 (悬停时增强) =====
        if self._hover_strength > 0.05:
            inner_glow = QRadialGradient(
                QPointF(glow_cx, glow_cy),
                self._base_size * 0.6
            )
            inner_alpha = int(80 * self._hover_strength)
            inner_glow.setColorAt(0.0, QColor(255, 255, 255, inner_alpha))
            inner_glow.setColorAt(0.4, QColor(200, 220, 255, int(inner_alpha * 0.5)))
            inner_glow.setColorAt(1.0, QColor(200, 220, 255, 0))
            painter.setBrush(QBrush(inner_glow))
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(2, 2, self._base_size - 4, self._base_size - 4)

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
        painter.drawEllipse(3, 3, self._base_size - 6, self._base_size - 6)

        # ===== 图标 - 菱形 (带液态光泽) =====
        painter.setPen(QPen(QColor(255, 255, 255, 240), 2))
        painter.setBrush(Qt.NoBrush)
        icon_size = 13
        painter.drawPolygon(
            QPoint(center_x, center_y - icon_size),
            QPoint(center_x + icon_size, center_y),
            QPoint(center_x, center_y + icon_size),
            QPoint(center_x - icon_size, center_y)
        )

    def mouseMoveEvent(self, event):
        """鼠标移动 - 更新光晕跟随位置"""
        w = max(self.width(), 1)
        h = max(self.height(), 1)
        self._target_glow_x = event.pos().x() / w
        self._target_glow_y = event.pos().y() / h

        if self._is_dragging and event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self._drag_offset)
        super().mouseMoveEvent(event)

    def enterEvent(self, event):
        self._is_hovered = True
        self._target_hover = 1.0
        # Q弹放大 - 使用 Spring 弹性动画
        self._animate_spring_scale(1.18)

    def leaveEvent(self, event):
        self._is_hovered = False
        self._target_hover = 0.0
        # 弹性恢复
        self._animate_spring_scale(1.0)

        # 如果没在拖动，吸附到屏幕边缘
        if not self._is_dragging:
            QTimer.singleShot(150, self._snap_to_edge_spring)

    def _animate_spring_scale(self, scale):
        """Spring 物理弹性缩放 - Q弹放大"""
        new_size = int(self._base_size * scale)
        # 使用 OutElastic 弹性曲线
        anim = QPropertyAnimation(self, b"size")
        anim.setDuration(400)
        anim.setStartValue(self.size())
        anim.setEndValue(QSize(new_size, new_size))

        curve = QEasingCurve(QEasingCurve.OutElastic)
        curve.setAmplitude(1.2)
        curve.setPeriod(0.4)
        anim.setEasingCurve(curve)

        # 保持动画对象存活
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

    # 兼容旧调用
    def _snap_to_edge(self):
        self._snap_to_edge_spring()
