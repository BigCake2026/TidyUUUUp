"""
Liquid Glass 液态玻璃效果组件
基于 2025-26 顶级液态玻璃 UI 配方设计
参考: design.dev/tools/liquid-glass-generator/

特点:
- 径向渐变背景（模拟玻璃曲面折射）
- 多层内阴影（顶部高光 + 底部内阴影 + 细边框）
- 外投影（柔和下沉感）
- 镜面光泽层（Specular Sheen）
- 内边框（Inner Rim）玻璃边缘透镜效果
"""

from PyQt5.QtCore import Qt, QRectF, QPointF, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QLinearGradient, QRadialGradient,
    QPainterPath, QPen, QBrush, QFont
)
from PyQt5.QtWidgets import QWidget


class LiquidGlassWidget(QWidget):
    """
    液态玻璃容器 - 用 paintEvent 绘制专业玻璃效果

    使用方法:
        glass = LiquidGlassWidget(parent)
        glass.set_glass_style('dark')  # 可选: dark, light, neon, aurora
        # 然后把你的布局放到 glass.layout() 里
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 玻璃样式配置
        self._style = 'dark'
        self._border_radius = 24
        self._blur_intensity = 0.6
        self._tint_opacity = 0.10

        # 预设样式
        self._presets = {
            'dark': {
                'tint_color': QColor(255, 255, 255),
                'bg_stops': [
                    (0.0, QColor(255, 255, 255, 46)),
                    (0.45, QColor(255, 255, 255, 26)),
                    (1.0, QColor(255, 255, 255, 13)),
                ],
                'text_color': QColor(255, 255, 255),
                'shadow_color': QColor(0, 0, 0, 72),
                'rim_color': QColor(255, 255, 255, 135),
            },
            'light': {
                'tint_color': QColor(255, 255, 255),
                'bg_stops': [
                    (0.0, QColor(255, 255, 255, 180)),
                    (0.45, QColor(255, 255, 255, 140)),
                    (1.0, QColor(255, 255, 255, 100)),
                ],
                'text_color': QColor(30, 30, 50),
                'shadow_color': QColor(0, 0, 0, 50),
                'rim_color': QColor(255, 255, 255, 200),
            },
            'neon': {
                'tint_color': QColor(100, 150, 255),
                'bg_stops': [
                    (0.0, QColor(150, 180, 255, 60)),
                    (0.5, QColor(180, 100, 255, 40)),
                    (1.0, QColor(100, 200, 255, 25)),
                ],
                'text_color': QColor(255, 255, 255),
                'shadow_color': QColor(100, 100, 255, 60),
                'rim_color': QColor(200, 220, 255, 150),
            },
            'aurora': {
                'tint_color': QColor(200, 255, 220),
                'bg_stops': [
                    (0.0, QColor(200, 255, 220, 50)),
                    (0.33, QColor(255, 200, 240, 40)),
                    (0.66, QColor(200, 220, 255, 35)),
                    (1.0, QColor(255, 240, 200, 25)),
                ],
                'text_color': QColor(255, 255, 255),
                'shadow_color': QColor(100, 150, 130, 50),
                'rim_color': QColor(255, 255, 255, 140),
            },
            'dock': {
                'tint_color': QColor(255, 255, 255),
                'bg_stops': [
                    (0.0, QColor(255, 255, 255, 35)),
                    (0.5, QColor(255, 255, 255, 22)),
                    (1.0, QColor(255, 255, 255, 15)),
                ],
                'text_color': QColor(255, 255, 255),
                'shadow_color': QColor(0, 0, 0, 90),
                'rim_color': QColor(255, 255, 255, 100),
            },
            'panel': {
                'tint_color': QColor(255, 255, 255),
                'bg_stops': [
                    (0.0, QColor(255, 255, 255, 40)),
                    (0.5, QColor(255, 255, 255, 25)),
                    (1.0, QColor(255, 255, 255, 18)),
                ],
                'text_color': QColor(255, 255, 255),
                'shadow_color': QColor(0, 0, 0, 60),
                'rim_color': QColor(255, 255, 255, 120),
            },
        }

    def set_glass_style(self, style_name):
        """设置玻璃样式: dark, light, neon, aurora, dock, panel"""
        if style_name in self._presets:
            self._style = style_name
            self.update()

    def set_border_radius(self, radius):
        """设置圆角半径"""
        self._border_radius = radius
        self.update()

    def _get_preset(self):
        return self._presets.get(self._style, self._presets['dark'])

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        preset = self._get_preset()
        rect = self.rect()
        w = rect.width()
        h = rect.height()
        r = self._border_radius

        # 创建圆角路径
        path = QPainterPath()
        path.addRoundedRect(QRectF(rect), r, r)
        painter.setClipPath(path)

        # ========== 第1层：外投影（模拟玻璃悬浮感） ==========
        # 用多层阴影模拟柔和投影
        for i in range(3):
            shadow_color = QColor(preset['shadow_color'])
            shadow_color.setAlpha(int(shadow_color.alpha() * (0.6 - i * 0.15)))
            offset = 3 + i * 4
            blur = 15 + i * 10
            painter.save()
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(0, 0, 0, 0))
            # Qt 没有直接的 box-shadow，我们用渐变模拟
            shadow_rect = QRectF(
                rect.x() + offset,
                rect.y() + offset,
                rect.width(),
                rect.height()
            )
            shadow_grad = QRadialGradient(
                shadow_rect.center(),
                max(shadow_rect.width(), shadow_rect.height())
            )
            shadow_grad.setColorAt(0.0, QColor(0, 0, 0, shadow_color.alpha()))
            shadow_grad.setColorAt(0.7, QColor(0, 0, 0, int(shadow_color.alpha() * 0.5)))
            shadow_grad.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setBrush(QBrush(shadow_grad))
            painter.drawRoundedRect(shadow_rect, r, r)
            painter.restore()

        # ========== 第2层：玻璃主体背景（径向渐变） ==========
        bg_grad = QRadialGradient(
            QPointF(w * 0.5, h * 0.15),  # 焦点偏上，模拟光照
            max(w, h) * 1.2
        )
        for pos, color in preset['bg_stops']:
            bg_grad.setColorAt(pos, color)

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(bg_grad))
        painter.drawRoundedRect(QRectF(rect), r, r)

        # ========== 第3层：顶部镜面光泽（Specular Sheen） ==========
        # 模拟玻璃顶部的弧面高光
        sheen_grad = QRadialGradient(
            QPointF(w * 0.5, -h * 0.15),
            w * 1.1
        )
        sheen_grad.setColorAt(0.0, QColor(255, 255, 255, 140))
        sheen_grad.setColorAt(0.3, QColor(255, 255, 255, 60))
        sheen_grad.setColorAt(0.7, QColor(255, 255, 255, 0))
        sheen_grad.setColorAt(1.0, QColor(255, 255, 255, 0))

        painter.setBrush(QBrush(sheen_grad))
        painter.drawRoundedRect(QRectF(rect), r, r)

        # ========== 第4层：内边框（Inner Rim） ==========
        # 模拟玻璃边缘的透镜效果
        rim_color = preset['rim_color']
        painter.setBrush(Qt.NoBrush)

        # 顶部高光边
        top_rim = QPen(rim_color, 1.5)
        top_rim.setColor(QColor(255, 255, 255, 204))
        painter.setPen(top_rim)
        painter.drawLine(
            QPointF(r * 0.5, 1.5),
            QPointF(w - r * 0.5, 1.5)
        )

        # 底部内阴影
        bottom_rim = QPen(QColor(0, 0, 0, 45), 1)
        painter.setPen(bottom_rim)
        painter.drawLine(
            QPointF(r * 0.5, h - 2),
            QPointF(w - r * 0.5, h - 2)
        )

        # ========== 第5层：整体细边框（1px hairline） ==========
        border_pen = QPen(QColor(255, 255, 255, 97), 1)
        painter.setPen(border_pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawRoundedRect(
            QRectF(0.5, 0.5, w - 1, h - 1),
            r, r
        )

        # ========== 第6层：内部多层内阴影 ==========
        # 用 QPainterPath 的减法模拟 inset 阴影
        inner_shadow1 = QColor(0, 0, 0, 15)
        inner_shadow2 = QColor(255, 255, 255, 25)
        inner_shadow3 = QColor(255, 255, 255, 39)

        # 这部分用多次描边模拟
        for i in range(4):
            alpha = max(0, 30 - i * 8)
            if alpha <= 0:
                continue
            shadow_pen = QPen(QColor(0, 0, 0, alpha), 1)
            painter.setPen(shadow_pen)
            inset = i + 1
            painter.drawRoundedRect(
                QRectF(inset, inset, w - inset * 2, h - inset * 2),
                max(0, r - inset), max(0, r - inset)
            )

        painter.end()


class DockGlassWidget(LiquidGlassWidget):
    """专门为 Dock 栏设计的玻璃效果"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_glass_style('dock')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        rect = self.rect()
        w = rect.width()
        h = rect.height()
        r = 24  # 顶部圆角

        # Dock 栏特殊形状：顶部圆角，底部直角
        path = QPainterPath()
        path.moveTo(r, 0)
        path.lineTo(w - r, 0)
        path.quadTo(w, 0, w, r)
        path.lineTo(w, h)
        path.lineTo(0, h)
        path.lineTo(0, r)
        path.quadTo(0, 0, r, 0)
        path.closeSubpath()
        painter.setClipPath(path)

        # 外投影
        shadow_grad = QLinearGradient(0, 0, 0, h)
        shadow_grad.setColorAt(0.0, QColor(0, 0, 0, 80))
        shadow_grad.setColorAt(0.3, QColor(0, 0, 0, 50))
        shadow_grad.setColorAt(1.0, QColor(0, 0, 0, 0))

        # 玻璃主体背景
        bg_grad = QRadialGradient(
            QPointF(w * 0.5, -h * 0.2),
            max(w, h) * 1.5
        )
        bg_grad.setColorAt(0.0, QColor(255, 255, 255, 55))
        bg_grad.setColorAt(0.4, QColor(255, 255, 255, 30))
        bg_grad.setColorAt(1.0, QColor(255, 255, 255, 18))

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(bg_grad))
        painter.drawPath(path)

        # 镜面光泽
        sheen_grad = QRadialGradient(
            QPointF(w * 0.5, -h * 0.3),
            w * 1.2
        )
        sheen_grad.setColorAt(0.0, QColor(255, 255, 255, 160))
        sheen_grad.setColorAt(0.25, QColor(255, 255, 255, 70))
        sheen_grad.setColorAt(0.6, QColor(255, 255, 255, 0))
        sheen_grad.setColorAt(1.0, QColor(255, 255, 255, 0))

        painter.setBrush(QBrush(sheen_grad))
        painter.drawPath(path)

        # 顶部高光边
        painter.setPen(QPen(QColor(255, 255, 255, 210), 1.5))
        painter.drawLine(QPointF(r * 0.5, 1.5), QPointF(w - r * 0.5, 1.5))

        # 边框
        painter.setPen(QPen(QColor(255, 255, 255, 90), 1))
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path)

        painter.end()


def apply_glass_effect(widget, style='dark'):
    """
    给任意 QWidget 应用液态玻璃背景
    注意：该 widget 必须设置 WA_TranslucentBackground
    """
    widget.setAttribute(Qt.WA_TranslucentBackground)
    glass = LiquidGlassWidget(widget)
    glass.set_glass_style(style)
    layout = widget.layout()
    if layout:
        # 把玻璃放到最底层
        layout.insertWidget(0, glass)
        glass.lower()
    return glass


class MouseReactiveGlassWidget(LiquidGlassWidget):
    """
    鼠标响应式液态玻璃 - Liquid Glass Pro

    参考 MFW-PyQt6 LiquidGlassHeroCard:
    - 鼠标移动时光晕跟随, 带 SmoothTween 惯性
    - 悬停时玻璃边缘高亮增强
    - 离开时光晕弹性消失

    Apple Liquid Glass 特色:
    - 光晕随鼠标平滑跟随 (factor=0.18)
    - 玻璃折射感随悬停强度变化
    - Q弹的光晕出现/消失
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 鼠标跟随光晕状态
        self._hover_strength = 0.0          # 当前悬停强度 (0.0~1.0)
        self._target_hover = 0.0            # 目标悬停强度
        self._glow_x = 0.5                  # 当前光晕X位置 (归一化 0~1)
        self._glow_y = 0.45                 # 当前光晕Y位置
        self._target_glow_x = 0.5           # 目标光晕X
        self._target_glow_y = 0.45          # 目标光晕Y

        # 60fps 平滑动画定时器
        self._anim_timer = QTimer(self)
        self._anim_timer.setInterval(16)    # ~60fps
        self._anim_timer.timeout.connect(self._tick_liquid)

    def _tick_liquid(self):
        """平滑插值动画 - 苹果级惯性"""
        # 悬停强度插值 (factor=0.18 苹果默认)
        self._hover_strength += (self._target_hover - self._hover_strength) * 0.18

        # 光晕位置插值 (factor=0.15 更丝滑)
        self._glow_x += (self._target_glow_x - self._glow_x) * 0.15
        self._glow_y += (self._target_glow_y - self._glow_y) * 0.15

        # 收敛检测
        if (abs(self._hover_strength - self._target_hover) < 0.005 and
            abs(self._glow_x - self._target_glow_x) < 0.003 and
            abs(self._glow_y - self._target_glow_y) < 0.003):
            self._hover_strength = self._target_hover
            self._glow_x = self._target_glow_x
            self._glow_y = self._target_glow_y
            self._anim_timer.stop()

        self.update()

    def mouseMoveEvent(self, event):
        w = max(self.width(), 1)
        h = max(self.height(), 1)
        self._target_glow_x = event.pos().x() / w
        self._target_glow_y = event.pos().y() / h
        self._target_hover = 1.0
        if not self._anim_timer.isActive():
            self._anim_timer.start()
        super().mouseMoveEvent(event)

    def enterEvent(self, event):
        self._target_hover = 1.0
        if not self._anim_timer.isActive():
            self._anim_timer.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._target_hover = 0.0
        if not self._anim_timer.isActive():
            self._anim_timer.start()
        super().leaveEvent(event)

    def paintEvent(self, event):
        # 先绘制父类的标准玻璃效果
        super().paintEvent(event)

        # 如果有悬停强度, 绘制鼠标跟随光晕
        if self._hover_strength > 0.01:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing, True)

            rect = self.rect()
            w = rect.width()
            h = rect.height()
            r = self._border_radius

            path = QPainterPath()
            path.addRoundedRect(QRectF(rect), r, r)
            painter.setClipPath(path)

            # 鼠标跟随光晕 - 液态玻璃折射感
            glow_cx = self._glow_x * w
            glow_cy = self._glow_y * h
            glow_radius = min(w, h) * 0.6

            glow_grad = QRadialGradient(
                QPointF(glow_cx, glow_cy),
                glow_radius
            )

            # 光晕颜色随悬停强度变化
            alpha1 = int(60 * self._hover_strength)
            alpha2 = int(30 * self._hover_strength)
            alpha3 = int(10 * self._hover_strength)

            glow_grad.setColorAt(0.0, QColor(255, 255, 255, alpha1))
            glow_grad.setColorAt(0.3, QColor(200, 220, 255, alpha2))
            glow_grad.setColorAt(0.7, QColor(150, 180, 255, alpha3))
            glow_grad.setColorAt(1.0, QColor(0, 0, 0, 0))

            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(glow_grad))
            painter.drawRoundedRect(QRectF(rect), r, r)

            # 边缘高亮增强 - 悬停时边框更亮
            if self._hover_strength > 0.3:
                edge_alpha = int(50 * self._hover_strength)
                painter.setPen(QPen(QColor(255, 255, 255, edge_alpha), 2))
                painter.setBrush(Qt.NoBrush)
                painter.drawRoundedRect(
                    QRectF(1, 1, w - 2, h - 2),
                    r - 1, r - 1
                )

            painter.end()
