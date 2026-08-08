"""
Liquid Glass Animation Engine
基于苹果 Spring Physics + QEasingCurve 的高级动画引擎

参考:
- Apple Spring Animation (mass-spring-damper model)
- MFW-PyQt6 LiquidGlassHeroCard (QTimer 补间)
- QEasingCurve OutBounce / OutElastic
"""

import math
from PyQt5.QtCore import (
    QPropertyAnimation, QEasingCurve, QTimer, QPoint, QSize, Qt,
    QParallelAnimationGroup, QSequentialAnimationGroup, pyqtProperty,
    QPointF
)
from PyQt5.QtWidgets import QWidget, QGraphicsOpacityEffect


# ============================================================
#  Spring Physics Engine - 苹果级弹簧物理动画
# ============================================================

class SpringAnimation:
    """
    基于真实弹簧-质量-阻尼物理模型的动画引擎
    模拟 Apple iOS/macOS 的 spring(duration:bounce:) API

    物理公式: F = -k*x - c*v  (胡克定律 + 粘性阻尼)
    """

    @staticmethod
    def create(target, property_name, start_value, end_value,
               stiffness=200, damping=20, mass=1.0):
        """
        创建弹簧动画

        参数:
            stiffness: 弹簧刚度 (越大越Q弹, Apple默认200)
            damping:   阻尼系数 (越小弹跳越多, Apple默认20)
            mass:      质量 (越大越迟钝)
        """
        anim = QPropertyAnimation(target, property_name)
        anim.setDuration(SpringAnimation._calculate_duration(
            stiffness, damping, mass
        ))
        anim.setStartValue(start_value)
        anim.setEndValue(end_value)

        # 使用 OutElastic 模拟弹簧振荡
        curve = QEasingCurve(QEasingCurve.OutElastic)
        curve.setAmplitude(max(1.0, damping / 10.0))
        curve.setPeriod(max(0.1, mass / (stiffness / 100)))
        anim.setEasingCurve(curve)

        return anim

    @staticmethod
    def create_bounce(target, property_name, start_value, end_value,
                      bounce=0.5, duration=600):
        """
        创建Q弹动画 (类似 Apple spring(bounce:) API)

        参数:
            bounce: 弹跳系数 0.0=不弹 ~ 1.0=最大弹
        """
        anim = QPropertyAnimation(target, property_name)
        anim.setDuration(duration)
        anim.setStartValue(start_value)
        anim.setEndValue(end_value)

        # bounce 越大用 OutBounce, 适中用 OutElastic
        if bounce > 0.7:
            curve = QEasingCurve(QEasingCurve.OutBounce)
        elif bounce > 0.3:
            curve = QEasingCurve(QEasingCurve.OutElastic)
            curve.setAmplitude(bounce * 2.0)
            curve.setPeriod(0.3 + (1.0 - bounce) * 0.3)
        else:
            curve = QEasingCurve(QEasingCurve.OutBack)
            curve.setOvershoot(1.0 + bounce * 2.0)

        anim.setEasingCurve(curve)
        return anim

    @staticmethod
    def _calculate_duration(stiffness, damping, mass):
        """根据弹簧参数计算自然动画时长"""
        if damping <= 0:
            return 2000
        # 阻尼振动周期
        omega = math.sqrt(stiffness / mass)
        decay = damping / (2 * mass)
        if decay >= omega:
            # 过阻尼
            return int(800 + 200 * mass / damping)
        # 欠阻尼: 3个衰减周期后基本停止
        period = 2 * math.pi / math.sqrt(omega * omega - decay * decay)
        duration = period * 3 * 1000 / (2 * math.pi)
        return min(max(int(duration), 300), 2000)


# ============================================================
#  Smooth Tween - 平滑插值动画 (参考 MFW-PyQt6)
# ============================================================

class SmoothTween:
    """
    QTimer 驱动的平滑插值动画
    value += (target - value) * factor
    比 QPropertyAnimation 更流畅, 适合实时跟随鼠标的场景

    性能优化:
    - QTimer 带 parent, 随父对象自动清理
    - 收敛后自动停止, 不空转 CPU
    """

    def __init__(self, callback, factor=0.15, fps=60, parent=None):
        """
        参数:
            callback: 每帧调用, 传入当前插值后的值
            factor:   插值系数 (0.05=丝滑, 0.2=灵敏, 0.15=苹果默认)
            fps:      帧率
            parent:   QTimer 的父对象 (防止内存泄漏)
        """
        self._callback = callback
        self._factor = factor
        self._timer = QTimer(parent)
        self._timer.setInterval(int(1000 / fps))
        self._timer.timeout.connect(self._tick)

        self._current = 0.0
        self._target = 0.0
        self._start = 0.0
        self._running = False

    @property
    def current(self):
        return self._current

    @property
    def target(self):
        return self._target

    def set_target(self, value, start_from_current=True):
        self._target = value
        if start_from_current:
            self._start = self._current
        else:
            self._start = value
            self._current = value
        if not self._running:
            self._timer.start()
            self._running = True

    def stop(self):
        self._timer.stop()
        self._running = False

    def _tick(self):
        diff = self._target - self._current
        self._current += diff * self._factor

        if abs(diff) < 0.005:
            self._current = self._target
            self._callback(self._current)
            self.stop()
        else:
            self._callback(self._current)


class SmoothPointTween:
    """QPointF 版本的平滑插值, 用于鼠标跟随"""

    def __init__(self, callback, factor=0.18, fps=60, parent=None):
        self._callback = callback
        self._factor = factor
        self._timer = QTimer(parent)
        self._timer.setInterval(int(1000 / fps))
        self._timer.timeout.connect(self._tick)

        self._current = QPointF(0.5, 0.5)
        self._target = QPointF(0.5, 0.5)
        self._running = False

    @property
    def current(self):
        return self._current

    def set_target(self, x, y):
        self._target = QPointF(x, y)
        if not self._running:
            self._timer.start()
            self._running = True

    def stop(self):
        self._timer.stop()
        self._running = False

    def _tick(self):
        dx = self._target.x() - self._current.x()
        dy = self._target.y() - self._current.y()
        self._current = QPointF(
            self._current.x() + dx * self._factor,
            self._current.y() + dy * self._factor
        )

        if abs(dx) < 0.003 and abs(dy) < 0.003:
            self._current = self._target
            self._callback(self._current)
            self.stop()
        else:
            self._callback(self._current)


# ============================================================
#  BounceAnimation - Q弹动画工具类 (升级版)
# ============================================================

class BounceAnimation:
    """苹果风格 Liquid Glass Q弹动画"""

    # 苹果标准弹簧参数预设
    SPRING_SNAPPY = {'stiffness': 300, 'damping': 26, 'mass': 1.0}   # 快速Q弹
    SPRING_SMOOTH = {'stiffness': 200, 'damping': 22, 'mass': 1.0}   # 平滑Q弹
    SPRING_BOUNCY = {'stiffness': 150, 'damping': 12, 'mass': 1.0}   # 弹跳明显
    SPRING_GENTLE = {'stiffness': 120, 'damping': 18, 'mass': 1.2}   # 柔和弹性

    @staticmethod
    def spring_animation(target, property_name, start_value, end_value, duration=500):
        """弹性动画 - 苹果级弹簧效果"""
        anim = SpringAnimation.create(
            target, property_name, start_value, end_value,
            **BounceAnimation.SPRING_SMOOTH
        )
        if duration:
            anim.setDuration(duration)
        return anim

    @staticmethod
    def scale_in(widget, duration=500):
        """缩放进入动画 - Q弹弹入"""
        widget.setScale(0.0)
        anim = QPropertyAnimation(widget, b"scale")
        anim.setDuration(duration)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        # 使用 OutBack 带回弹的缩放
        curve = QEasingCurve(QEasingCurve.OutBack)
        curve.setOvershoot(1.2)
        anim.setEasingCurve(curve)
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
    def fade_in(widget, duration=350):
        """淡入动画 - 带微弹"""
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
    def slide_in_up(widget, duration=500, offset=30):
        """从下往上滑入 - Q弹效果"""
        pos = widget.pos()
        widget.move(pos.x(), pos.y() + offset)
        anim = QPropertyAnimation(widget, b"pos")
        anim.setDuration(duration)
        anim.setStartValue(QPoint(pos.x(), pos.y() + offset))
        anim.setEndValue(pos)
        # 使用弹性曲线
        curve = QEasingCurve(QEasingCurve.OutBack)
        curve.setOvershoot(1.1)
        anim.setEasingCurve(curve)
        return anim

    @staticmethod
    def slide_in_down(widget, duration=500, offset=30):
        """从上往下滑入"""
        pos = widget.pos()
        widget.move(pos.x(), pos.y() - offset)
        anim = QPropertyAnimation(widget, b"pos")
        anim.setDuration(duration)
        anim.setStartValue(QPoint(pos.x(), pos.y() - offset))
        anim.setEndValue(pos)
        curve = QEasingCurve(QEasingCurve.OutBack)
        curve.setOvershoot(1.1)
        anim.setEasingCurve(curve)
        return anim

    @staticmethod
    def slide_in_left(widget, duration=500, offset=30):
        """从右往左滑入"""
        pos = widget.pos()
        widget.move(pos.x() + offset, pos.y())
        anim = QPropertyAnimation(widget, b"pos")
        anim.setDuration(duration)
        anim.setStartValue(QPoint(pos.x() + offset, pos.y()))
        anim.setEndValue(pos)
        curve = QEasingCurve(QEasingCurve.OutBack)
        curve.setOvershoot(1.1)
        anim.setEasingCurve(curve)
        return anim

    @staticmethod
    def pulse(widget, duration=600):
        """脉冲动画 - Q弹放大再缩小"""
        original_size = widget.size()
        original_pos = widget.pos()

        group = QSequentialAnimationGroup()

        # Q弹放大
        anim1 = QPropertyAnimation(widget, b"geometry")
        anim1.setDuration(int(duration * 0.4))
        expand = 5
        anim1.setStartValue(widget.geometry())
        anim1.setEndValue(widget.geometry().adjusted(-expand, -expand, expand, expand))
        anim1.setEasingCurve(QEasingCurve.OutBack)
        group.addAnimation(anim1)

        # 弹性缩小
        anim2 = QPropertyAnimation(widget, b"geometry")
        anim2.setDuration(int(duration * 0.6))
        anim2.setStartValue(widget.geometry().adjusted(-expand, -expand, expand, expand))
        anim2.setEndValue(widget.geometry())
        anim2.setEasingCurve(QEasingCurve.OutBounce)
        group.addAnimation(anim2)

        return group

    @staticmethod
    def shake(widget, duration=500, intensity=5):
        """抖动动画 - Q弹左右晃"""
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
            anim.setEasingCurve(QEasingCurve.OutElastic)
            group.addAnimation(anim)

        return group

    @staticmethod
    def hover_scale(widget, scale_factor=1.08, duration=250):
        """悬停放大效果 - Q弹"""
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

    @staticmethod
    def liquid_bounce(widget, amplitude=1.3, duration=600):
        """
        液态Q弹 - Apple Liquid Glass 风格的弹性回弹
        模拟液滴落下的弹跳效果
        """
        anim = QPropertyAnimation(widget, b"geometry")
        anim.setDuration(duration)

        original = widget.geometry()
        expand = int(8 * amplitude)
        anim.setStartValue(original.adjusted(-expand, -expand, expand, expand))
        anim.setEndValue(original)

        curve = QEasingCurve(QEasingCurve.OutBounce)
        anim.setEasingCurve(curve)
        return anim


# ============================================================
#  ToastManager - 浮动提示 (升级弹性动画)
# ============================================================

class ToastManager:
    """浮动提示管理 - Liquid Glass 风格"""

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

        # 淡入动画 - 带微弹
        effect = QGraphicsOpacityEffect(toast)
        toast.setGraphicsEffect(effect)
        effect.setOpacity(0.0)

        fade_in = QPropertyAnimation(effect, b"opacity")
        fade_in.setDuration(350)
        fade_in.setStartValue(0.0)
        fade_in.setEndValue(1.0)
        fade_in.setEasingCurve(QEasingCurve.OutCubic)

        # 滑入 - Q弹效果
        slide = QPropertyAnimation(toast, b"pos")
        slide.setDuration(500)
        slide.setStartValue(QPoint(x, y + 30))
        slide.setEndValue(QPoint(x, y))
        curve = QEasingCurve(QEasingCurve.OutBack)
        curve.setOvershoot(1.2)
        slide.setEasingCurve(curve)

        # 将动画对象挂载到 toast 上, 防止被 GC 中断
        toast._fade_in_anim = fade_in
        toast._slide_in_anim = slide

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
                toast._fade_out_anim = fade_out  # 防止 GC
                fade_out.start()

                def delete_later():
                    toast.close()
                    toast.deleteLater()
                    # 重新排列其他toast - Q弹
                    for i, t in enumerate(self.toasts):
                        ty = parent_geo.bottom() - t.height() - 80 - (i * (t.height() + 10))
                        anim = QPropertyAnimation(t, b"pos")
                        anim.setDuration(400)
                        anim.setEndValue(QPoint(t.x(), ty))
                        curve = QEasingCurve(QEasingCurve.OutBack)
                        curve.setOvershoot(1.1)
                        t._rearrange_anim = anim  # 防止 GC
                        anim.setEasingCurve(curve)
                        anim.start()

                QTimer.singleShot(250, delete_later)

        QTimer.singleShot(duration, remove_toast)


# ============================================================
#  DockMagnifyEffect - macOS 风格 Dock 放大 (单一共享定时器版)
# ============================================================

class DockMagnifyEffect:
    """
    Dock栏放大效果 - 单一共享定时器版

    性能优化:
    1. 所有 item 共享一个 QTimer (而非每个 item 一个), 大幅减少定时器数量
    2. 所有 item 都收敛后才停止定时器, 避免空转
    3. 鼠标跟随有惯性, 不会跳变
    4. 离开时弹性回弹
    """

    def __init__(self, dock_widget, items, magnify_scale=1.5, radius=80):
        self.dock = dock_widget
        self.items = items
        self.magnify_scale = magnify_scale
        self.radius = radius

        # 每个 item 的当前 scale 和目标 scale
        self.current_scales = {}
        self.target_scales = {}
        for item in items:
            self.current_scales[item] = 1.0
            self.target_scales[item] = 1.0

        # 单一共享定时器 (60fps)
        self._timer = QTimer(dock_widget)
        self._timer.setInterval(16)
        self._timer.timeout.connect(self._tick_all)
        self._factor = 0.20  # 苹果级灵敏度

    def update_magnification(self, mouse_pos):
        for item in self.items:
            if not item.isVisible():
                continue

            item_center = item.mapTo(self.dock, item.rect().center())
            distance = abs(mouse_pos.x() - item_center.x())

            if distance < self.radius:
                ratio = distance / self.radius
                scale = 1.0 + (self.magnify_scale - 1.0) * (
                    0.5 * (1 + math.cos(ratio * math.pi))
                )
            else:
                scale = 1.0

            self.target_scales[item] = scale

        if not self._timer.isActive():
            self._timer.start()

    def _tick_all(self):
        """所有 item 共用一个 tick - 一次定时器触发处理所有 item"""
        all_converged = True
        for item in list(self.target_scales.keys()):
            if not item.isVisible():
                continue
            target = self.target_scales[item]
            current = self.current_scales[item]
            diff = target - current
            current += diff * self._factor

            if abs(diff) < 0.005:
                current = target
            else:
                all_converged = False

            self.current_scales[item] = current
            self._apply_scale(item, current)

        if all_converged:
            self._timer.stop()

    def _apply_scale(self, item, scale):
        base_size = item.property("baseSize")
        if base_size is None:
            base_size = item.size()
            item.setProperty("baseSize", base_size)

        new_width = int(base_size.width() * scale)
        new_height = int(base_size.height() * scale)
        item.setMaximumSize(new_width, new_height)

    def reset(self):
        """弹性回弹到原始大小"""
        for item in self.items:
            self.target_scales[item] = 1.0
        if not self._timer.isActive():
            self._timer.start()

    def add_item(self, item):
        """动态添加 item"""
        if item not in self.current_scales:
            self.current_scales[item] = 1.0
            self.target_scales[item] = 1.0
            if item not in self.items:
                self.items.append(item)

    def remove_item(self, item):
        """移除 item"""
        if item in self.current_scales:
            del self.current_scales[item]
        if item in self.target_scales:
            del self.target_scales[item]
        if item in self.items:
            self.items.remove(item)
