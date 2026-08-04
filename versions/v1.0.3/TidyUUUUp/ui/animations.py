from PyQt5.QtCore import (
    QPropertyAnimation, QEasingCurve, QTimer, QPoint, QSize, Qt,
    QParallelAnimationGroup, QSequentialAnimationGroup
)
from PyQt5.QtWidgets import QWidget, QGraphicsOpacityEffect


class BounceAnimation:
    """苹果风格的Q弹动画"""

    @staticmethod
    def spring_animation(target, property_name, start_value, end_value, duration=500):
        """弹性动画 - 模拟弹簧效果"""
        anim = QPropertyAnimation(target, property_name)
        anim.setDuration(duration)
        anim.setStartValue(start_value)
        anim.setEndValue(end_value)
        anim.setEasingCurve(QEasingCurve.OutBack)
        return anim

    @staticmethod
    def scale_in(widget, duration=400):
        """缩放进入动画 - 从小到大弹入"""
        widget.setScale(0.0)
        anim = QPropertyAnimation(widget, b"scale")
        anim.setDuration(duration)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.setEasingCurve(QEasingCurve.OutBack)
        return anim

    @staticmethod
    def scale_out(widget, duration=300):
        """缩放映出动画"""
        anim = QPropertyAnimation(widget, b"scale")
        anim.setDuration(duration)
        anim.setStartValue(1.0)
        anim.setEndValue(0.0)
        anim.setEasingCurve(QEasingCurve.InBack)
        return anim

    @staticmethod
    def fade_in(widget, duration=300):
        """淡入动画"""
        effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(effect)
        anim = QPropertyAnimation(effect, b"opacity")
        anim.setDuration(duration)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        return anim

    @staticmethod
    def fade_out(widget, duration=250):
        """淡出动画"""
        effect = widget.graphicsEffect()
        if not effect or not hasattr(effect, 'opacity'):
            effect = QGraphicsOpacityEffect(widget)
            widget.setGraphicsEffect(effect)
        anim = QPropertyAnimation(effect, b"opacity")
        anim.setDuration(duration)
        anim.setStartValue(1.0)
        anim.setEndValue(0.0)
        anim.setEasingCurve(QEasingCurve.InCubic)
        return anim

    @staticmethod
    def slide_in_up(widget, duration=400, offset=30):
        """从下往上滑入"""
        pos = widget.pos()
        widget.move(pos.x(), pos.y() + offset)
        anim = QPropertyAnimation(widget, b"pos")
        anim.setDuration(duration)
        anim.setStartValue(QPoint(pos.x(), pos.y() + offset))
        anim.setEndValue(pos)
        anim.setEasingCurve(QEasingCurve.OutBack)
        return anim

    @staticmethod
    def slide_in_down(widget, duration=400, offset=30):
        """从上往下滑入"""
        pos = widget.pos()
        widget.move(pos.x(), pos.y() - offset)
        anim = QPropertyAnimation(widget, b"pos")
        anim.setDuration(duration)
        anim.setStartValue(QPoint(pos.x(), pos.y() - offset))
        anim.setEndValue(pos)
        anim.setEasingCurve(QEasingCurve.OutBack)
        return anim

    @staticmethod
    def slide_in_left(widget, duration=400, offset=30):
        """从右往左滑入"""
        pos = widget.pos()
        widget.move(pos.x() + offset, pos.y())
        anim = QPropertyAnimation(widget, b"pos")
        anim.setDuration(duration)
        anim.setStartValue(QPoint(pos.x() + offset, pos.y()))
        anim.setEndValue(pos)
        anim.setEasingCurve(QEasingCurve.OutBack)
        return anim

    @staticmethod
    def pulse(widget, duration=600):
        """脉冲动画 - 轻微放大再缩小"""
        original_size = widget.size()
        original_pos = widget.pos()

        group = QSequentialAnimationGroup()

        # 放大
        anim1 = QPropertyAnimation(widget, b"geometry")
        anim1.setDuration(duration // 2)
        expand = 4
        anim1.setStartValue(widget.geometry())
        anim1.setEndValue(widget.geometry().adjusted(-expand, -expand, expand, expand))
        anim1.setEasingCurve(QEasingCurve.OutQuad)
        group.addAnimation(anim1)

        # 缩小
        anim2 = QPropertyAnimation(widget, b"geometry")
        anim2.setDuration(duration // 2)
        anim2.setStartValue(widget.geometry().adjusted(-expand, -expand, expand, expand))
        anim2.setEndValue(widget.geometry())
        anim2.setEasingCurve(QEasingCurve.InQuad)
        group.addAnimation(anim2)

        return group

    @staticmethod
    def shake(widget, duration=500, intensity=5):
        """抖动动画"""
        pos = widget.pos()
        group = QSequentialAnimationGroup()

        for i in range(6):
            anim = QPropertyAnimation(widget, b"pos")
            anim.setDuration(duration // 6)
            offset = intensity if i % 2 == 0 else -intensity
            if i == 5:
                offset = 0
            anim.setStartValue(pos)
            anim.setEndValue(QPoint(pos.x() + offset, pos.y()))
            anim.setEasingCurve(QEasingCurve.InOutQuad)
            group.addAnimation(anim)

        return group

    @staticmethod
    def hover_scale(widget, scale_factor=1.08, duration=200):
        """悬停放大效果"""
        original_scale = 1.0

        def on_enter():
            anim = QPropertyAnimation(widget, b"windowOpacity")
            anim.setDuration(duration)
            anim.setStartValue(1.0)
            anim.setEndValue(scale_factor)
            anim.start()

        def on_leave():
            anim = QPropertyAnimation(widget, b"windowOpacity")
            anim.setDuration(duration)
            anim.setStartValue(scale_factor)
            anim.setEndValue(original_scale)
            anim.start()

        return on_enter, on_leave


class ToastManager:
    """浮动提示管理"""

    def __init__(self, parent):
        self.parent = parent
        self.toasts = []

    def show_toast(self, message, duration=3000, toast_type='info'):
        toast = QWidget(self.parent)
        toast.setObjectName('Toast')
        toast.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        toast.setAttribute(Qt.WA_TranslucentBackground)

        from PyQt5.QtWidgets import QHBoxLayout, QLabel
        layout = QHBoxLayout(toast)
        layout.setContentsMargins(16, 12, 16, 12)

        label = QLabel(message, toast)
        label.setStyleSheet("color: white; background: transparent; border: none;")
        layout.addWidget(label)

        toast.adjustSize()

        # 定位到右下角
        parent_geo = self.parent.geometry()
        x = parent_geo.right() - toast.width() - 20
        y = parent_geo.bottom() - toast.height() - 80 - (len(self.toasts) * (toast.height() + 10))
        toast.move(x, y + 30)

        # 淡入动画
        effect = QGraphicsOpacityEffect(toast)
        toast.setGraphicsEffect(effect)
        effect.setOpacity(0.0)

        fade_in = QPropertyAnimation(effect, b"opacity")
        fade_in.setDuration(300)
        fade_in.setStartValue(0.0)
        fade_in.setEndValue(1.0)
        fade_in.setEasingCurve(QEasingCurve.OutCubic)

        slide = QPropertyAnimation(toast, b"pos")
        slide.setDuration(400)
        slide.setStartValue(QPoint(x, y + 30))
        slide.setEndValue(QPoint(x, y))
        slide.setEasingCurve(QEasingCurve.OutBack)

        toast.show()
        fade_in.start()
        slide.start()

        self.toasts.append(toast)

        def remove_toast():
            if toast in self.toasts:
                self.toasts.remove(toast)
                # 淡出
                fade_out = QPropertyAnimation(effect, b"opacity")
                fade_out.setDuration(250)
                fade_out.setStartValue(1.0)
                fade_out.setEndValue(0.0)
                fade_out.setEasingCurve(QEasingCurve.InCubic)
                fade_out.start()

                def delete_later():
                    toast.close()
                    toast.deleteLater()
                    # 重新排列其他toast
                    for i, t in enumerate(self.toasts):
                        ty = parent_geo.bottom() - t.height() - 80 - (i * (t.height() + 10))
                        anim = QPropertyAnimation(t, b"pos")
                        anim.setDuration(300)
                        anim.setEndValue(QPoint(t.x(), ty))
                        anim.setEasingCurve(QEasingCurve.OutBack)
                        anim.start()

                QTimer.singleShot(250, delete_later)

        QTimer.singleShot(duration, remove_toast)


class DockMagnifyEffect:
    """Dock栏放大效果 - 类似macOS"""

    def __init__(self, dock_widget, items, magnify_scale=1.5, radius=80):
        self.dock = dock_widget
        self.items = items
        self.magnify_scale = magnify_scale
        self.radius = radius
        self.animations = {}

    def update_magnification(self, mouse_pos):
        dock_center_y = self.dock.height() // 2

        for item in self.items:
            if not item.isVisible():
                continue

            item_center = item.mapTo(self.dock, item.rect().center())
            distance = abs(mouse_pos.x() - item_center.x())

            if distance < self.radius:
                # 使用高斯分布计算放大倍数
                scale = 1.0 + (self.magnify_scale - 1.0) * (
                    1.0 - (distance / self.radius) ** 2
                )
            else:
                scale = 1.0

            self._apply_scale(item, scale)

    def _apply_scale(self, item, target_scale):
        if item in self.animations:
            self.animations[item].stop()

        anim = QPropertyAnimation(item, b"maximumSize")
        anim.setDuration(150)

        base_size = item.property("baseSize")
        if base_size is None:
            base_size = item.size()
            item.setProperty("baseSize", base_size)

        new_width = int(base_size.width() * target_scale)
        new_height = int(base_size.height() * target_scale)

        anim.setStartValue(item.maximumSize())
        anim.setEndValue(QSize(new_width, new_height))
        anim.setEasingCurve(QEasingCurve.OutCubic)
        anim.start()

        self.animations[item] = anim

    def reset(self):
        for item in self.items:
            base_size = item.property("baseSize")
            if base_size:
                item.setMaximumSize(base_size)
