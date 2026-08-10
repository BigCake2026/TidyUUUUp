"""
悬浮球组件 - Floating Ball (Minimalist)
极简灰色半透明圆球：克制设计，无彩虹光晕、无呼吸动画、无多层渐变。

功能：
- clicked / right_clicked / double_clicked 信号
- 鼠标拖动
- 左右屏幕边缘吸附（QPropertyAnimation 滑动，200ms InOutCubic）
- show / hide 滑动动画（非缩放）
"""
from PyQt5.QtCore import (
    Qt, QPoint, QPointF, QRectF,
    QPropertyAnimation, QEasingCurve, pyqtSignal
)
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush


class FloatingBall(QWidget):
    """悬浮球 - 极简灰色半透明圆球 + 拖动 + 左右边缘吸附"""

    clicked = pyqtSignal()
    right_clicked = pyqtSignal(QPoint)
    double_clicked = pyqtSignal()

    BALL_SIZE = 40
    DRAG_THRESHOLD = 5  # 超过此距离视为拖动，否则视为点击

    # 配色
    _BG_NORMAL = QColor(255, 255, 255, 184)    # rgba(255,255,255,0.72)
    _BG_HOVER = QColor(255, 255, 255, 224)     # rgba(255,255,255,0.88)
    _BG_PRESSED = QColor(0, 0, 0, 15)          # rgba(0,0,0,0.06)
    _BORDER = QColor(0, 0, 0, 15)              # rgba(0,0,0,0.06) 1px
    _ICON_NORMAL = QColor(134, 134, 139)       # #86868B
    _ICON_HOVER = QColor(29, 29, 31)           # #1D1D1F

    _ANIM_DURATION = 200  # 吸附 / 滑动动画时长 ms

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)

        self.setFixedSize(self.BALL_SIZE, self.BALL_SIZE)

        # 交互状态
        self._is_dragging = False
        self._drag_started = False       # 是否真正发生了拖动（超过阈值）
        self._drag_offset = QPoint()
        self._press_pos = QPoint()
        self._is_hovered = False
        self._is_pressed = False

        # 动画引用（防止被 GC）
        self._snap_anim = None
        self._show_anim = None
        self._hide_anim = None
        self._target_pos = None          # 当前期望的屏幕内位置

        # 默认位置：屏幕右侧中部
        screen = QApplication.primaryScreen().availableGeometry()
        self._target_pos = QPoint(
            screen.right() - self.BALL_SIZE - 8,
            screen.height() // 2 - self.BALL_SIZE // 2
        )
        self.move(self._target_pos)

        self.setCursor(Qt.PointingHandCursor)

    # ------------------------------------------------------------------
    # 绘制
    # ------------------------------------------------------------------
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        size = self.BALL_SIZE
        ball_rect = QRectF(0.5, 0.5, size - 1, size - 1)

        # 圆球背景
        if self._is_pressed:
            bg = self._BG_PRESSED
        elif self._is_hovered:
            bg = self._BG_HOVER
        else:
            bg = self._BG_NORMAL

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(bg))
        painter.drawEllipse(ball_rect)

        # 1px 边框
        painter.setBrush(Qt.NoBrush)
        painter.setPen(QPen(self._BORDER, 1.0))
        painter.drawEllipse(ball_rect)

        # 3 条水平线图标（中间一条较短）
        icon_color = self._ICON_HOVER if self._is_hovered else self._ICON_NORMAL
        painter.setPen(QPen(icon_color, 1.6, Qt.SolidLine, Qt.RoundCap))

        cx = size / 2.0
        cy = size / 2.0
        w_long = 14.0
        w_short = 9.0
        gap = 4.0
        painter.drawLine(QPointF(cx - w_long / 2, cy - gap),
                         QPointF(cx + w_long / 2, cy - gap))
        painter.drawLine(QPointF(cx - w_short / 2, cy),
                         QPointF(cx + w_short / 2, cy))
        painter.drawLine(QPointF(cx - w_long / 2, cy + gap),
                         QPointF(cx + w_long / 2, cy + gap))

    # ------------------------------------------------------------------
    # 鼠标交互
    # ------------------------------------------------------------------
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = True
            self._drag_started = False
            self._drag_offset = event.globalPos() - self.frameGeometry().topLeft()
            self._press_pos = event.globalPos()
            self._is_pressed = True
            self.update()
        elif event.button() == Qt.RightButton:
            self.right_clicked.emit(event.globalPos())

    def mouseMoveEvent(self, event):
        if self._is_dragging and event.buttons() & Qt.LeftButton:
            if not self._drag_started:
                moved = (event.globalPos() - self._press_pos).manhattanLength()
                if moved > self.DRAG_THRESHOLD:
                    self._drag_started = True
            if self._drag_started:
                self.move(event.globalPos() - self._drag_offset)
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self._is_dragging:
            self._is_dragging = False
            self._is_pressed = False
            self.update()
            if not self._drag_started:
                # 未拖动 → 视为点击
                self._on_clicked()
            else:
                # 拖动结束 → 吸附到最近的屏幕边缘
                self.screen_edge_check()

    def mouseDoubleClickEvent(self, event):
        self.double_clicked.emit()

    def enterEvent(self, event):
        self._is_hovered = True
        self.update()

    def leaveEvent(self, event):
        self._is_hovered = False
        self._is_pressed = False
        self.update()

    # ------------------------------------------------------------------
    # 点击处理
    # ------------------------------------------------------------------
    def _on_clicked(self):
        """点击处理 - 发送 clicked 信号"""
        self.clicked.emit()

    # ------------------------------------------------------------------
    # 位置 & 边缘吸附
    # ------------------------------------------------------------------
    def set_position(self, x, y):
        """设置悬浮球位置"""
        self._target_pos = QPoint(x, y)
        self.move(x, y)

    def screen_edge_check(self):
        """检查并吸附到最近的屏幕边缘（左右吸附）"""
        screen = QApplication.primaryScreen().availableGeometry()
        geo = self.frameGeometry()

        margin = 8
        # 只吸附左右边缘：根据中心点判断吸附到左侧还是右侧
        if geo.center().x() < screen.center().x():
            target_x = screen.left() + margin
        else:
            target_x = screen.right() - geo.width() - margin
        target_y = geo.y()

        # 已经接近目标位置就不动画
        if abs(target_x - geo.x()) < 2 and abs(target_y - geo.y()) < 2:
            self._target_pos = QPoint(target_x, target_y)
            return

        self._animate_slide_to(target_x, target_y)

    def _animate_slide_to(self, x, y):
        """滑动到目标位置 - QPropertyAnimation 200ms InOutCubic"""
        if self._snap_anim is not None:
            self._snap_anim.stop()

        anim = QPropertyAnimation(self, b"pos")
        anim.setDuration(self._ANIM_DURATION)
        anim.setStartValue(self.pos())
        anim.setEndValue(QPoint(x, y))
        anim.setEasingCurve(QEasingCurve.InOutCubic)

        self._snap_anim = anim
        self._target_pos = QPoint(x, y)
        anim.start()

    # ------------------------------------------------------------------
    # show / hide 滑动动画（非缩放）
    # ------------------------------------------------------------------
    def _edge_out_pos(self, target_pos):
        """根据目标位置计算最近屏幕边缘外侧的位置（用于滑入/滑出）"""
        screen = QApplication.primaryScreen().availableGeometry()
        center_x = target_pos.x() + self.BALL_SIZE / 2
        if center_x < screen.center().x():
            return QPoint(screen.left() - self.BALL_SIZE - 4, target_pos.y())
        return QPoint(screen.right() + 4, target_pos.y())

    def show(self):
        """显示 - 从最近的屏幕边缘滑入"""
        # 如果正在隐藏，取消隐藏动画并继续滑入
        hide_running = (self._hide_anim is not None and
                        self._hide_anim.state() == QPropertyAnimation.Running)
        if hide_running:
            self._hide_anim.stop()
        elif self.isVisible():
            # 已可见且未在隐藏中，不重复播放滑入动画
            super().show()
            return

        target = self._target_pos if self._target_pos is not None else self.pos()
        start = self._edge_out_pos(target)
        self.move(start)
        super().show()

        if self._show_anim is not None:
            self._show_anim.stop()
        anim = QPropertyAnimation(self, b"pos")
        anim.setDuration(self._ANIM_DURATION)
        anim.setStartValue(start)
        anim.setEndValue(target)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        self._show_anim = anim
        anim.start()

    def hide(self):
        """隐藏 - 滑出到最近的屏幕边缘后隐藏"""
        if not self.isVisible():
            super().hide()
            return

        # 记住当前位置作为再次显示的目标
        self._target_pos = self.pos()
        end = self._edge_out_pos(self._target_pos)

        if self._hide_anim is not None:
            self._hide_anim.stop()

        anim = QPropertyAnimation(self, b"pos")
        anim.setDuration(self._ANIM_DURATION)
        anim.setStartValue(self.pos())
        anim.setEndValue(end)
        anim.setEasingCurve(QEasingCurve.InCubic)
        anim.finished.connect(self._on_hide_finished)
        self._hide_anim = anim
        anim.start()

    def _on_hide_finished(self):
        super().hide()
        # 恢复到目标位置，以便下次 show 时从边缘滑入到正确位置
        if self._target_pos is not None:
            self.move(self._target_pos)
