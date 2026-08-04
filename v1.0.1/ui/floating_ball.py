"""
悬浮球组件 - Floating Ball
不用时缩成小圆球，不占空间
"""
from PyQt5.QtCore import (
    Qt, QPoint, QSize, QTimer, QPropertyAnimation, QEasingCurve,
    pyqtSignal, QRect
)
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import (
    QPainter, QColor, QRadialGradient, QBrush, QPen, QCursor,
    QLinearGradient
)


class FloatingBall(QWidget):
    """悬浮小球 - 可拖动，点击展开/收起"""

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

        self._size = 48
        self.setFixedSize(self._size, self._size)

        self._is_dragging = False
        self._drag_offset = QPoint()
        self._is_hovered = False
        self._pulse_phase = 0

        # 脉冲动画
        self._pulse_timer = QTimer(self)
        self._pulse_timer.timeout.connect(self._on_pulse)
        self._pulse_timer.start(50)

        # 默认位置：右下角
        screen = QApplication.primaryScreen().geometry()
        self.move(screen.width() - self._size - 20, screen.height() - self._size - 100)

        self.setCursor(Qt.PointingHandCursor)

    def _on_pulse(self):
        self._pulse_phase = (self._pulse_phase + 0.1) % 6.28
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect()
        center_x = rect.width() / 2
        center_y = rect.height() / 2

        # 呼吸光晕效果
        pulse = 0.5 + 0.5 * (1 + __import__('math').sin(self._pulse_phase)) * 0.3
        glow_size = 8 + pulse * 6

        gradient = QRadialGradient(center_x, center_y, self._size / 2 + glow_size)
        gradient.setColorAt(0, QColor(100, 150, 255, int(180 * pulse)))
        gradient.setColorAt(0.5, QColor(150, 100, 255, int(80 * pulse)))
        gradient.setColorAt(1, QColor(150, 100, 255, 0))

        painter.setBrush(QBrush(gradient))
        painter.setPen(Qt.NoPen)
        glow_rect = QRect(
            int(center_x - self._size / 2 - glow_size),
            int(center_y - self._size / 2 - glow_size),
            int(self._size + glow_size * 2),
            int(self._size + glow_size * 2)
        )
        painter.drawEllipse(glow_rect)

        # 球体主体 - Liquid Glass 效果
        ball_gradient = QRadialGradient(
            center_x - 6, center_y - 6, 0,
            center_x, center_y, self._size / 2
        )
        if self._is_hovered:
            ball_gradient.setColorAt(0, QColor(180, 200, 255, 255))
            ball_gradient.setColorAt(0.4, QColor(120, 150, 255, 240))
            ball_gradient.setColorAt(1, QColor(80, 100, 220, 230))
        else:
            ball_gradient.setColorAt(0, QColor(160, 180, 240, 245))
            ball_gradient.setColorAt(0.4, QColor(100, 130, 230, 235))
            ball_gradient.setColorAt(1, QColor(60, 80, 200, 225))

        painter.setBrush(QBrush(ball_gradient))
        painter.setPen(QPen(QColor(255, 255, 255, 60), 1))
        painter.drawEllipse(2, 2, self._size - 4, self._size - 4)

        # 高光
        highlight = QRadialGradient(
            center_x - 10, center_y - 10, 0,
            center_x - 8, center_y - 8, 16
        )
        highlight.setColorAt(0, QColor(255, 255, 255, 200))
        highlight.setColorAt(1, QColor(255, 255, 255, 0))
        painter.setBrush(QBrush(highlight))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(int(center_x - 18), int(center_y - 18), 20, 20)

        # 图标 - 菱形
        painter.setPen(QPen(QColor(255, 255, 255, 230), 2))
        painter.setBrush(Qt.NoBrush)
        icon_size = 14
        painter.drawPolygon(
            QPoint(center_x, center_y - icon_size),
            QPoint(center_x + icon_size, center_y),
            QPoint(center_x, center_y + icon_size),
            QPoint(center_x - icon_size, center_y)
        )

    def enterEvent(self, event):
        self._is_hovered = True
        self.update()

        # 放大效果
        self._animate_scale(1.15)

    def leaveEvent(self, event):
        self._is_hovered = False
        self.update()

        # 恢复大小
        self._animate_scale(1.0)

        # 如果没在拖动，吸附到屏幕边缘
        if not self._is_dragging:
            QTimer.singleShot(200, self._snap_to_edge)

    def _animate_scale(self, scale):
        anim = QPropertyAnimation(self, b"size")
        anim.setDuration(200)
        new_size = int(self._size * scale)
        anim.setStartValue(self.size())
        anim.setEndValue(QSize(new_size, new_size))
        anim.setEasingCurve(QEasingCurve.OutBack)
        anim.start()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = True
            self._drag_offset = event.globalPos() - self.frameGeometry().topLeft()
        elif event.button() == Qt.RightButton:
            self.right_clicked.emit(event.globalPos())

    def mouseMoveEvent(self, event):
        if self._is_dragging and event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self._drag_offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self._is_dragging:
            self._is_dragging = False
            self._snap_to_edge()

    def mouseDoubleClickEvent(self, event):
        self.double_clicked.emit()

    def _snap_to_edge(self):
        """吸附到屏幕最近的边缘"""
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

        # 平滑移动
        anim = QPropertyAnimation(self, b"pos")
        anim.setDuration(300)
        anim.setStartValue(self.pos())
        anim.setEndValue(QPoint(target_x, target_y))
        anim.setEasingCurve(QEasingCurve.OutBack)
        anim.start()
