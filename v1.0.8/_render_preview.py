#!/usr/bin/env python3
"""
离线预览渲染脚本 - 无需显示环境即可生成 PNG 截图
渲染内容：
  1. Liquid Glass Dock 栏 (含 3D ZoneFolderButton 文件夹图标)
  2. 目录树弹出面板 DirectoryTreePopup
使用 QT_QPA_PLATFORM=offscreen 运行
"""
import os
import sys
import json

# 强制使用 offscreen 平台，需要在 import PyQt5 前设置
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PyQt5.QtCore import (
    Qt, QPoint, QPointF, QRect, QRectF, QSize, QTimer,
    QPropertyAnimation, QEasingCurve, QSequentialAnimationGroup,
    pyqtSignal, QObject
)
from PyQt5.QtGui import (
    QPainter, QPainterPath, QBrush, QPen, QColor, QLinearGradient,
    QRadialGradient, QPixmap, QImage, QFont, QFontMetrics,
    QIcon, QPainterPathStroker, QCursor, QGuiApplication
)
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QHBoxLayout, QGridLayout, QListWidget, QListWidgetItem,
    QGraphicsOpacityEffect, QFrame, QSizePolicy, QToolButton,
    QSpacerItem, QScrollArea, QTreeWidget, QTreeWidgetItem,
    QFileIconProvider, QStyle
)


# ======================================================================
# 工具函数
# ======================================================================
ZONE_CONFIG = {
    "图片":   {"icon": "🖼️", "color": (86, 182, 255)},
    "视频":   {"icon": "🎬", "color": (255, 100, 120)},
    "文档":   {"icon": "📄", "color": (100, 200, 150)},
    "代码":   {"icon": "💻", "color": (170, 130, 255)},
    "压缩包": {"icon": "🗜️", "color": (255, 190, 90)},
    "音频":   {"icon": "🎵", "color": (255, 120, 210)},
    "下载":   {"icon": "⬇️", "color": (90, 200, 255)},
    "其他":   {"icon": "📦", "color": (170, 170, 185)},
}


def set_qt_scale(app, scale=1.0):
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)


def render_widget_to_png(widget, out_path, with_shadow_bg=False, bg_color=None):
    """将 widget 渲染为 PNG 图片（离屏渲染）"""
    # 确保布局计算完成
    widget.show()
    QApplication.processEvents()
    widget.repaint()
    QApplication.processEvents()

    pixmap = widget.grab()
    if not with_shadow_bg and not bg_color:
        pixmap.save(out_path, "PNG")
        return out_path

    # 如果需要带背景的版本
    final = QPixmap(pixmap.size())
    final.fill(QColor(0, 0, 0, 0))
    painter = QPainter(final)
    painter.setRenderHint(QPainter.Antialiasing)
    if bg_color:
        painter.fillRect(final.rect(), bg_color)
    painter.drawPixmap(0, 0, pixmap)
    painter.end()
    final.save(out_path, "PNG")
    return out_path


# ======================================================================
# Liquid Glass 3D 文件夹按钮（ZoneFolderButton）
# ======================================================================
class ZoneFolderButton(QPushButton):
    """Liquid Glass 3D 文件夹图标按钮 - 独立渲染版"""

    zone_hovered = pyqtSignal(object, QPoint)
    zone_left = pyqtSignal()

    def __init__(self, zone_name="图片", file_count=127, state="normal", parent=None):
        super().__init__(parent)
        self.zone_name = zone_name
        self.zone_config = ZONE_CONFIG.get(zone_name, ZONE_CONFIG["其他"])
        self.file_count = file_count
        self.state = state  # normal / hover / pressed
        self._glow = 0.0 if state == "normal" else (1.0 if state == "hover" else 0.4)
        self._scale = 1.0 if state != "pressed" else 0.94
        self._pressed = 1.0 if state == "pressed" else 0.0
        self._hovered = 0.0 if state == "normal" else 1.0

        # 根据状态设置固定大小
        base = 54
        self.setFixedSize(int(base * self._scale), int(base * self._scale))
        self.setStyleSheet("background: transparent; border: none;")

    def set_state(self, state):
        self.state = state
        self._hovered = 0.0 if state == "normal" else 1.0
        self._pressed = 1.0 if state == "pressed" else 0.0
        self._glow = 0.0 if state == "normal" else (1.0 if state == "hover" else 0.4)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform | QPainter.HighQualityAntialiasing)

        W, H = self.width(), self.height()
        # 逻辑基准尺寸（60）
        SX, SY = W / 60.0, H / 60.0

        # 按压时整体偏移 + 缩小（视觉下陷）
        dy = self._pressed * 1.5
        painter.translate(W / 2, H / 2 + dy)
        scale = 1.0 - self._pressed * 0.06
        painter.scale(scale, scale)
        painter.translate(-W / 2, -H / 2)

        # ---- 1. 悬浮光晕 ----
        if self._hovered > 0.01:
            glow_radius = 30 * SX + 12 * SX * self._hovered
            glow = QRadialGradient(QPointF(W / 2, H / 2), glow_radius)
            cr, cg, cb = self.zone_config["color"]
            glow.setColorAt(0.0, QColor(cr, cg, cb, int(95 * self._hovered)))
            glow.setColorAt(0.4, QColor(cr, cg, cb, int(42 * self._hovered)))
            glow.setColorAt(0.7, QColor(cr, cg, cb, int(14 * self._hovered)))
            glow.setColorAt(1.0, QColor(cr, cg, cb, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(glow))
            painter.drawEllipse(QRectF(W / 2 - glow_radius, H / 2 - glow_radius, glow_radius * 2, glow_radius * 2))

        # ---- 2. 文件夹图标坐标 ----
        x, y, w, h = 9 * SX, 10 * SY, 42 * SX, 38 * SY
        tab_h = 6 * SY
        tab_w = 14 * SX
        r = 4.2 * SX  # 圆角

        # ---- 3. 外阴影（投影） ----
        shadow_offs = 1.5 * SY + self._pressed * 2.5 * SY
        shadow_blur = 4.0 * SX
        shadow_color = QColor(0, 0, 0, int((95 - 20 * self._pressed)))

        path_shadow = QPainterPath()
        path_shadow.addRoundedRect(x - shadow_blur * 0.5, y + tab_h + shadow_offs,
                                   w + shadow_blur, h - tab_h + shadow_blur * 0.5, r, r)
        sg = QRadialGradient(QPointF(x + w / 2, y + h / 2 + shadow_offs), w * 0.9)
        sg.setColorAt(0.0, shadow_color)
        sg.setColorAt(0.8, QColor(0, 0, 0, int(shadow_color.alpha() * 0.55)))
        sg.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(sg))
        painter.drawRoundedRect(QRectF(x - shadow_blur, y + tab_h + shadow_offs - shadow_blur, w + shadow_blur * 2, h - tab_h + shadow_blur * 2), r * 1.4, r * 1.4)

        # ---- 4. 文件夹主体底座（盒身深色渐变） ----
        body_path = QPainterPath()
        body_rect = QRectF(x, y + tab_h, w, h - tab_h)
        body_path.addRoundedRect(body_rect, r, r)

        cr, cg, cb = self.zone_config["color"]
        body_grad = QLinearGradient(0, y + tab_h, 0, y + h)
        body_grad.setColorAt(0.0, QColor(min(cr + 50, 255), min(cg + 50, 255), min(cb + 50, 255), 235))
        body_grad.setColorAt(0.35, QColor(cr, cg, cb, 240))
        body_grad.setColorAt(0.75, QColor(max(cr - 40, 0), max(cg - 40, 0), max(cb - 40, 0), 245))
        body_grad.setColorAt(1.0, QColor(max(cr - 75, 0), max(cg - 75, 0), max(cb - 75, 0), 245))

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(body_grad))
        painter.drawPath(body_path)

        # ---- 5. 文件夹上盖（tab，亮面渐变） ----
        tab_path = QPainterPath()
        # 上盖左边圆角 + 顶边 + 右边圆角 + 压入主体 1.5px 的小折角
        tab_path.moveTo(x, y + tab_h + 1)
        tab_path.lineTo(x, y + tab_h - tab_h * 0.1)
        tab_path.quadTo(x, y, x + r * 0.7, y)
        tab_path.lineTo(x + tab_w - r * 0.7, y)
        tab_path.quadTo(x + tab_w, y, x + tab_w + r * 0.5, y + r * 0.5)
        tab_path.lineTo(x + tab_w + 1.2, y + tab_h - 0.5)
        # 上盖底边（和盒身顶部重叠，略微压入）
        tab_path.lineTo(x + w - 0.5, y + tab_h + 1.5)
        tab_path.quadTo(x + w, y + tab_h + r * 0.7, x + w - r * 0.5, y + tab_h + 2)
        tab_path.lineTo(x + r * 0.5, y + tab_h + 2)
        tab_path.quadTo(x, y + tab_h + r * 0.7, x, y + tab_h + 1)
        tab_path.closeSubpath()

        cover_grad = QLinearGradient(0, y, 0, y + tab_h + 4)
        cover_grad.setColorAt(0.0, QColor(min(cr + 75, 255), min(cg + 75, 255), min(cb + 75, 255), 245))
        cover_grad.setColorAt(0.5, QColor(min(cr + 30, 255), min(cg + 30, 255), min(cb + 30, 255), 245))
        cover_grad.setColorAt(1.0, QColor(cr, cg, cb, 245))
        painter.setBrush(QBrush(cover_grad))
        painter.drawPath(tab_path)

        # ---- 6. 主体玻璃高光（左上半透明弧形高光） ----
        highlight = QLinearGradient(x, y + tab_h, x + w * 0.5, y + h)
        hl_alpha1 = 140 + int(45 * self._hovered)
        hl_alpha2 = 18 + int(22 * self._hovered)
        highlight.setColorAt(0.0, QColor(255, 255, 255, hl_alpha1))
        highlight.setColorAt(0.25, QColor(255, 255, 255, hl_alpha2))
        highlight.setColorAt(1.0, QColor(255, 255, 255, 0))

        hl_path = QPainterPath()
        hl_path.addRoundedRect(QRectF(x + 2 * SX, y + tab_h + 2 * SY, w * 0.52, (h - tab_h) * 0.55), r * 0.9, r * 0.9)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(highlight))
        # 裁掉超出主体的部分
        painter.setClipPath(body_path)
        painter.drawPath(hl_path)
        painter.setClipping(False)

        # ---- 7. 上盖高光线（顶部一条细线高光） ----
        top_hl = QLinearGradient(0, y, 0, y + tab_h)
        top_hl.setColorAt(0.0, QColor(255, 255, 255, 220))
        top_hl.setColorAt(0.45, QColor(255, 255, 255, 60))
        top_hl.setColorAt(1.0, QColor(255, 255, 255, 0))

        top_hl_path = QPainterPath()
        top_hl_path.addRoundedRect(QRectF(x + 1.8 * SX, y + 0.6, w * 0.32, tab_h * 0.65), r * 0.55, r * 0.55)
        painter.setBrush(QBrush(top_hl))
        painter.setClipPath(tab_path)
        painter.drawPath(top_hl_path)
        painter.setClipping(False)

        # ---- 8. 内阴影（主体下边缘 + 上盖下边缘） ----
        inner_shadow = QLinearGradient(0, y + h - 8 * SY, 0, y + h)
        inner_shadow.setColorAt(0.0, QColor(0, 0, 0, 0))
        inner_shadow.setColorAt(1.0, QColor(0, 0, 0, 65))
        is_path = QPainterPath()
        is_path.addRoundedRect(QRectF(x, y + h - 8 * SY, w, 8 * SY), r * 0.5, r * 0.5)
        painter.setBrush(QBrush(inner_shadow))
        painter.setClipPath(body_path)
        painter.drawPath(is_path)
        painter.setClipping(False)

        # ---- 9. 双层描边（外描边半透明白 + 内描边更淡） ----
        combined = QPainterPath()
        combined.addPath(body_path)
        combined.addPath(tab_path)

        # 外描边：更亮更粗
        outer_pen = QPen(QColor(255, 255, 255, 95 + int(50 * self._hovered)))
        outer_pen.setWidthF(max(1.2 * SX, 1.0))
        painter.setPen(outer_pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(body_path)
        painter.drawPath(tab_path)

        # 内描边：更淡更细
        inner_pen = QPen(QColor(255, 255, 255, 38 + int(25 * self._hovered)))
        inner_pen.setWidthF(max(0.7 * SX, 0.7))
        painter.setPen(inner_pen)
        is_body = QPainterPath()
        is_body.addRoundedRect(QRectF(x + 1.5, y + tab_h + 1.5, w - 3, h - tab_h - 3), r * 0.8, r * 0.8)
        painter.drawPath(is_body)

        # ---- 10. 边缘高光线（左上 L 型边缘高光） ----
        edge_pen = QPen(QColor(255, 255, 255, 160))
        edge_pen.setWidthF(max(1.6 * SX, 1.2))
        painter.setPen(edge_pen)
        edge_path = QPainterPath()
        # 主体左侧高光
        edge_path.moveTo(x + 1.2, y + tab_h + r * 0.8)
        edge_path.lineTo(x + 1.2, y + h - r * 1.1)
        # 主体顶边高光（上盖下方折痕线）
        edge_path.moveTo(x + 1.2, y + tab_h + 1.2)
        edge_path.lineTo(x + w - r * 0.9, y + tab_h + 1.2)
        painter.drawPath(edge_path)

        # ---- 11. 分类 emoji 图标（居中放大） ----
        icon_text = self.zone_config["icon"]
        font = QFont("Apple Color Emoji")
        font.setPointSizeF(16.0 * SX)
        font.setBold(True)
        painter.setFont(font)
        painter.setPen(QColor(255, 255, 255, 245))
        icon_rect = QRectF(x, y + tab_h + 1, w, h - tab_h - 1)
        painter.drawText(icon_rect, Qt.AlignCenter, icon_text)

        # 图标下的柔和投影（增加立体感）
        icon_shadow = QPainter()
        painter.setPen(QColor(0, 0, 0, 45))
        font.setPointSizeF(16.0 * SX)
        painter.setFont(font)
        painter.drawText(QRectF(x, y + tab_h + 3, w, h - tab_h - 1), Qt.AlignCenter, icon_text)
        # 再在正上方画一次白色
        painter.setPen(QColor(255, 255, 255, 245))
        painter.drawText(QRectF(x, y + tab_h, w, h - tab_h - 2), Qt.AlignCenter, icon_text)

        # ---- 12. 文件数量徽标（右上角红色圆形气泡） ----
        badge_r = min(9.0 * SX, 9.0)
        if self.file_count > 0 and badge_r > 3:
            count = self.file_count
            count_text = str(count) if count <= 99 else "99+"
            cx, cy = x + w - badge_r * 0.85, y + badge_r * 0.95

            # 徽标外阴影
            bd_shadow = QRadialGradient(QPointF(cx, cy + badge_r * 0.3), badge_r * 1.7)
            bd_shadow.setColorAt(0.0, QColor(0, 0, 0, 70))
            bd_shadow.setColorAt(0.5, QColor(0, 0, 0, 25))
            bd_shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(bd_shadow))
            painter.drawEllipse(QPointF(cx, cy + badge_r * 0.35), badge_r * 1.4, badge_r * 1.4)

            # 徽标红色主体渐变
            bg = QRadialGradient(QPointF(cx - badge_r * 0.35, cy - badge_r * 0.35), badge_r * 1.4)
            bg.setColorAt(0.0, QColor(255, 135, 145, 255))
            bg.setColorAt(0.55, QColor(245, 65, 85, 255))
            bg.setColorAt(1.0, QColor(205, 35, 55, 255))
            painter.setBrush(QBrush(bg))
            painter.drawEllipse(QPointF(cx, cy), badge_r, badge_r)

            # 徽标白色外圈描边
            painter.setPen(QPen(QColor(255, 255, 255, 210), max(1.1 * SX, 1.0)))
            painter.setBrush(Qt.NoBrush)
            painter.drawEllipse(QPointF(cx, cy), badge_r - 0.5 * SX, badge_r - 0.5 * SX)

            # 徽标内部高光
            hg = QRadialGradient(QPointF(cx - badge_r * 0.3, cy - badge_r * 0.3), badge_r * 0.7)
            hg.setColorAt(0.0, QColor(255, 255, 255, 130))
            hg.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(hg))
            painter.drawEllipse(QPointF(cx - badge_r * 0.15, cy - badge_r * 0.1), badge_r * 0.7, badge_r * 0.7)

            # 数字文本
            num_font = QFont("Segoe UI")
            num_font.setBold(True)
            num_font.setPointSizeF(7.4 * SX if len(count_text) <= 2 else 6.3 * SX)
            painter.setFont(num_font)
            fm = QFontMetrics(num_font)
            tw = fm.width(count_text)
            th = fm.height()
            tr = QRectF(cx - tw / 2.0, cy - th / 2.0 - fm.descent() * 0.5, tw, th)
            painter.setPen(QColor(255, 255, 255, 255))
            painter.drawText(tr, Qt.AlignCenter, count_text)

        painter.end()


# ======================================================================
# MiniDock - 迷你 Dock 栏渲染
# ======================================================================
class MiniDock(QWidget):
    """Liquid Glass 风格迷你 Dock 栏（含分隔符和文件夹图标）"""

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(780, 90)
        self._build_content()

    def _build_content(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(14, 9, 14, 9)
        layout.setSpacing(5)

        # 开始按钮
        b = QToolButton()
        b.setText("🚀")
        b.setFixedSize(52, 52)
        layout.addWidget(b)

        def sep():
            s = QFrame()
            s.setFrameShape(QFrame.VLine)
            s.setFixedWidth(2)
            s.setStyleSheet("background: rgba(255,255,255,15);")
            return s

        layout.addWidget(sep())

        # 系统功能区
        for sym, size in [("📁", 48), ("🧹", 48), ("🔎", 48)]:
            tb = QToolButton()
            tb.setText(sym)
            tb.setFixedSize(size, size)
            layout.addWidget(tb)

        layout.addWidget(sep())

        # ZoneFolderButton 区（多个分类，不同文件数量 + 不同状态）
        zones = [
            ("图片", 234, "hover"),
            ("视频", 56, "normal"),
            ("文档", 1278, "normal"),
            ("代码", 89, "normal"),
            ("压缩包", 12, "pressed"),
            ("音频", 45, "normal"),
            ("下载", 672, "normal"),
            ("其他", 8, "normal"),
        ]
        for zn, cnt, st in zones:
            zfb = ZoneFolderButton(zn, cnt, st)
            layout.addWidget(zfb)

        layout.addSpacing(6)
        layout.addWidget(sep())
        layout.addSpacing(6)

        # 右侧工具
        for sym, size in [("↩️", 46), ("⏰", 46), ("⚙️", 46)]:
            tb = QToolButton()
            tb.setText(sym)
            tb.setFixedSize(size, size)
            layout.addWidget(tb)

        layout.addStretch(1)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform | QPainter.HighQualityAntialiasing)
        W, H = self.width(), self.height()

        # ===== 1. 外发光底托（悬浮阴影） =====
        glow = QRadialGradient(QPointF(W / 2, H + 6), H * 0.75)
        glow.setColorAt(0.0, QColor(0, 0, 0, 85))
        glow.setColorAt(0.45, QColor(0, 0, 0, 45))
        glow.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(glow))
        painter.drawEllipse(QRectF(W / 2 - H * 0.75, H * 0.25, H * 1.5, H * 1.0))

        # ===== 2. Dock 主体圆角矩形区域 =====
        dock_pad = 4
        dock_rect = QRectF(dock_pad, dock_pad, W - dock_pad * 2, H - dock_pad * 2)
        r = 22  # 大圆角

        dock_path = QPainterPath()
        dock_path.addRoundedRect(dock_rect, r, r)

        # 三段式渐变（上亮 → 中 → 下深）
        body_grad = QLinearGradient(0, dock_rect.top(), 0, dock_rect.bottom())
        body_grad.setColorAt(0.0,  QColor(58, 64, 92, 200))
        body_grad.setColorAt(0.35, QColor(45, 50, 72, 212))
        body_grad.setColorAt(0.72, QColor(38, 42, 62, 220))
        body_grad.setColorAt(1.0,  QColor(22, 24, 38, 240))

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(body_grad))
        painter.drawPath(dock_path)

        # ===== 3. 顶部镜面高光（ClipRect 裁切，只在上半部分叠一层） =====
        mirror_h = dock_rect.height() * 0.50
        mirror_rect = QRectF(dock_rect.left() + 2, dock_rect.top() + 1.5,
                             dock_rect.width() - 4, mirror_h)
        mirror_grad = QLinearGradient(0, mirror_rect.top(), 0, mirror_rect.bottom())
        mirror_grad.setColorAt(0.0, QColor(255, 255, 255, 78))
        mirror_grad.setColorAt(0.35, QColor(255, 255, 255, 36))
        mirror_grad.setColorAt(0.75, QColor(255, 255, 255, 12))
        mirror_grad.setColorAt(1.0, QColor(255, 255, 255, 0))

        painter.setBrush(QBrush(mirror_grad))
        painter.setClipRect(mirror_rect)
        mirror_path = QPainterPath()
        mirror_path.addRoundedRect(mirror_rect, r * 0.92, r * 0.92)
        painter.drawPath(mirror_path)
        painter.setClipping(False)

        # ===== 4. 底部内阴影（模拟玻璃容器折射） =====
        inner_h = 10
        inner_rect = QRectF(dock_rect.left(), dock_rect.bottom() - inner_h,
                            dock_rect.width(), inner_h)
        inner_grad = QLinearGradient(0, inner_rect.top(), 0, inner_rect.bottom())
        inner_grad.setColorAt(0.0, QColor(0, 0, 0, 0))
        inner_grad.setColorAt(1.0, QColor(0, 0, 0, 60))
        painter.setBrush(QBrush(inner_grad))
        painter.setClipRect(inner_rect)
        inner_path = QPainterPath()
        inner_path.addRoundedRect(QRectF(inner_rect.left(), inner_rect.top() - inner_h * 0.5,
                                         inner_rect.width(), inner_h * 1.5), r * 0.6, r * 0.6)
        painter.drawPath(inner_path)
        painter.setClipping(False)

        # ===== 5. 双层半透明描边 =====
        outer_pen = QPen(QColor(255, 255, 255, 55))
        outer_pen.setWidthF(1.1)
        painter.setPen(outer_pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(dock_path)

        inner_pen = QPen(QColor(255, 255, 255, 42))
        inner_pen.setWidthF(0.6)
        painter.setPen(inner_pen)
        inner_border = QPainterPath()
        inner_border.addRoundedRect(dock_rect.adjusted(1.0, 1.0, -1.0, -1.0), r - 0.5, r - 0.5)
        painter.drawPath(inner_border)

        # ===== 6. 顶部 1.6px 白色高光线条 =====
        edge_pen = QPen(QColor(255, 255, 255, 145))
        edge_pen.setWidthF(1.6)
        painter.setPen(edge_pen)
        top_line = QPainterPath()
        ty = dock_rect.top() + 3.0
        top_line.moveTo(dock_rect.left() + r * 0.7, ty)
        top_line.lineTo(dock_rect.right() - r * 0.7, ty)
        painter.drawPath(top_line)

        # ===== 7. 发光分隔符（3处） =====
        # 这里用列表标注每个分隔符的 x 坐标（根据布局推算）
        sep_x_list = [
            90,   # 开始按钮后
            252,  # 系统功能后
            722,  # 右侧工具前
        ]
        sep_top = dock_rect.top() + 16
        sep_bot = dock_rect.bottom() - 16
        for cx in sep_x_list:
            path = QPainterPath()
            path.addRoundedRect(QRectF(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
            sg = QLinearGradient(0, sep_top, 0, sep_bot)
            sg.setColorAt(0.0, QColor(255, 255, 255, 0))
            sg.setColorAt(0.5, QColor(255, 255, 255, 55))
            sg.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(sg))
            painter.drawPath(path)

        painter.end()


# ======================================================================
# 目录树弹出面板 DirectoryTreePopup
# ======================================================================
class DirectoryTreePopup(QWidget):
    """Liquid Glass 风格目录树弹出面板"""

    def __init__(self):
        super().__init__(None)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(380, 440)
        self._anchor_x = 190  # 底部箭头位置 x
        self._build_content()

    def _build_content(self):
        outer = QVBoxLayout(self)
        outer.setContentsMargins(16, 16, 16, 26)  # 底部留 10px 给箭头
        outer.setSpacing(0)

        # 标题
        title_row = QHBoxLayout()
        title_row.setContentsMargins(4, 0, 4, 10)
        title = QLabel("🖼️  图片 分类（共 234 个文件）")
        tf = QFont("Segoe UI")
        tf.setPointSizeF(10.5)
        tf.setBold(True)
        title.setFont(tf)
        title.setStyleSheet("color: rgba(255,255,255,240); background: transparent;")
        title_row.addWidget(title)
        title_row.addStretch(1)
        hint = QLabel("双击打开")
        hf = QFont("Segoe UI")
        hf.setPointSizeF(8.5)
        hint.setFont(hf)
        hint.setStyleSheet("color: rgba(255,255,255,110); background: transparent;")
        title_row.addWidget(hint)
        outer.addLayout(title_row)

        # 分组目录树
        tree_widget = QListWidget()
        tree_widget.setStyleSheet("""
            QListWidget {
                background: transparent;
                border: none;
                outline: none;
                color: white;
                padding: 0 2px;
            }
            QListWidget::item {
                background: transparent;
                padding: 0;
                margin: 2px 0;
                border-radius: 8px;
            }
        """)

        groups = [
            ("📂 桌面 (48)", ["风景照.jpg", "家庭合照.png", "截图_20260807.png", "头像.png", "屏幕录制.mp4", "…还有 43 个更多…"]),
            ("📂 下载 (127)", ["wallpaper_4k.jpg", "IMG_0098.HEIC", "设计稿_v3.psd", "海报_最终版.png", "Photo_2026.png", "…还有 122 个更多…"]),
            ("📂 我的图片 (59)", ["旅行照片1.jpg", "旅行照片2.jpg", "猫咪.jpg", "狗狗.png", "风景壁纸.png", "…还有 54 个更多…"]),
        ]
        for group_name, items in groups:
            # group header
            h = QListWidgetItem(group_name)
            hf2 = QFont("Segoe UI")
            hf2.setBold(True)
            hf2.setPointSizeF(9.5)
            h.setFont(hf2)
            h.setForeground(QColor(170, 200, 255))
            h.setSizeHint(QSize(0, 28))
            tree_widget.addItem(h)
            for it in items:
                li = QListWidgetItem("      " + it)
                fl = QFont("Segoe UI")
                fl.setPointSize(9)
                li.setFont(fl)
                is_ellipsis = "还有" in it
                li.setForeground(QColor(255, 255, 255, 125 if is_ellipsis else 230))
                li.setSizeHint(QSize(0, 24))
                tree_widget.addItem(li)

        outer.addWidget(tree_widget, 1)

        # 底部状态栏
        status = QLabel("📍 共 3 个目录 · 点击「查看全部」展开完整列表")
        sf = QFont("Segoe UI")
        sf.setPointSizeF(8.5)
        status.setFont(sf)
        status.setStyleSheet("color: rgba(255,255,255,105); background: transparent; padding: 6px 2px 0 2px;")
        outer.addWidget(status)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform | QPainter.HighQualityAntialiasing)
        W, H = self.width(), self.height()

        # ===== 1. 外发光底托 =====
        glow_r = W * 0.6
        glow = QRadialGradient(QPointF(W / 2, H / 2), glow_r)
        glow.setColorAt(0.0, QColor(0, 0, 0, 55))
        glow.setColorAt(0.6, QColor(0, 0, 0, 22))
        glow.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(glow))
        painter.drawRoundedRect(QRectF(W / 2 - glow_r, H / 2 - glow_r, glow_r * 2, glow_r * 2), 40, 40)

        # ===== 2. 主体面板（底部留箭头空间） =====
        arrow_h = 14
        panel_rect = QRectF(6, 6, W - 12, H - 12 - arrow_h)
        r = 18
        # 主体 path
        panel_path = QPainterPath()
        panel_path.addRoundedRect(panel_rect, r, r)
        # 底部三角箭头
        ax, ay = self._anchor_x, panel_rect.bottom()
        aw, ah = 16, arrow_h
        panel_path.moveTo(ax - aw / 2, ay)
        panel_path.lineTo(ax, ay + ah)
        panel_path.lineTo(ax + aw / 2, ay)
        panel_path.closeSubpath()

        # 三段式渐变
        body_grad = QLinearGradient(0, panel_rect.top(), 0, panel_rect.bottom())
        body_grad.setColorAt(0.0,  QColor(60, 66, 96, 218))
        body_grad.setColorAt(0.35, QColor(44, 48, 72, 228))
        body_grad.setColorAt(0.72, QColor(34, 38, 60, 238))
        body_grad.setColorAt(1.0,  QColor(20, 22, 38, 248))
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(body_grad))
        painter.drawPath(panel_path)

        # ===== 3. 顶部镜面高光 =====
        mirror_h = panel_rect.height() * 0.45
        mirror_rect = QRectF(panel_rect.left() + 2, panel_rect.top() + 1.5,
                             panel_rect.width() - 4, mirror_h)
        mirror_grad = QLinearGradient(0, mirror_rect.top(), 0, mirror_rect.bottom())
        mirror_grad.setColorAt(0.0, QColor(255, 255, 255, 85))
        mirror_grad.setColorAt(0.35, QColor(255, 255, 255, 40))
        mirror_grad.setColorAt(0.75, QColor(255, 255, 255, 14))
        mirror_grad.setColorAt(1.0, QColor(255, 255, 255, 0))
        painter.setBrush(QBrush(mirror_grad))
        painter.setClipRect(mirror_rect)
        mp = QPainterPath()
        mp.addRoundedRect(mirror_rect, r * 0.9, r * 0.9)
        painter.drawPath(mp)
        painter.setClipping(False)

        # ===== 4. 底部内阴影 =====
        inner_h = 10
        inner_rect = QRectF(panel_rect.left(), panel_rect.bottom() - inner_h,
                            panel_rect.width(), inner_h)
        inner_grad = QLinearGradient(0, inner_rect.top(), 0, inner_rect.bottom())
        inner_grad.setColorAt(0.0, QColor(0, 0, 0, 0))
        inner_grad.setColorAt(1.0, QColor(0, 0, 0, 70))
        painter.setBrush(QBrush(inner_grad))
        painter.setClipRect(inner_rect)
        ip = QPainterPath()
        ip.addRoundedRect(QRectF(inner_rect.left(), inner_rect.top() - inner_h * 0.5,
                                 inner_rect.width(), inner_h * 1.5), r * 0.6, r * 0.6)
        painter.drawPath(ip)
        painter.setClipping(False)

        # ===== 5. 双层描边 =====
        outer_pen = QPen(QColor(255, 255, 255, 60))
        outer_pen.setWidthF(1.1)
        painter.setPen(outer_pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(panel_path)

        inner_pen = QPen(QColor(255, 255, 255, 40))
        inner_pen.setWidthF(0.6)
        painter.setPen(inner_pen)
        ib = QPainterPath()
        ib.addRoundedRect(panel_rect.adjusted(1.0, 1.0, -1.0, -1.0), r - 0.5, r - 0.5)
        painter.drawPath(ib)

        # ===== 6. 顶部反光细线 =====
        edge_pen = QPen(QColor(255, 255, 255, 145))
        edge_pen.setWidthF(1.5)
        painter.setPen(edge_pen)
        ty = panel_rect.top() + 3.0
        tl = QPainterPath()
        tl.moveTo(panel_rect.left() + r * 0.7, ty)
        tl.lineTo(panel_rect.right() - r * 0.7, ty)
        painter.drawPath(tl)

        painter.end()


# ======================================================================
# 文件夹图标三种状态对比网格
# ======================================================================
class FolderIconGrid(QWidget):
    """对比网格：每个文件夹 三种状态 × 8 个分类"""

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        cols = 8  # 分类数
        rows = 4  # 标题行 + 3 行状态
        cell_w, cell_h = 120, 120
        self.resize(cols * cell_w + 60, rows * cell_h + 80)

        root = QVBoxLayout(self)
        root.setContentsMargins(30, 30, 30, 30)
        root.setSpacing(16)

        states = [("normal", " 默认"), ("hover", "悬停"), ("pressed", "按下")]

        # 标题栏
        header_row = QHBoxLayout()
        header_row.setSpacing(0)
        header_row.addSpacing(80)
        for zone_name in ZONE_CONFIG.keys():
            hl = QLabel(f"{ZONE_CONFIG[zone_name]['icon']} {zone_name}")
            hf = QFont("Segoe UI")
            hf.setPointSize(10)
            hf.setBold(True)
            hl.setFont(hf)
            hl.setStyleSheet("color: rgba(255,255,255,230); background: transparent;")
            hl.setAlignment(Qt.AlignCenter)
            hl.setFixedWidth(cell_w)
            header_row.addWidget(hl)
        root.addLayout(header_row)

        # 三个状态行
        for state_key, state_label in states:
            row = QHBoxLayout()
            row.setSpacing(0)
            sl = QLabel(state_label)
            sf = QFont("Segoe UI")
            sf.setPointSize(10)
            sf.setBold(True)
            sl.setFont(sf)
            sl.setStyleSheet("color: rgba(180, 210, 255, 230); background: transparent;")
            sl.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            sl.setFixedWidth(75)
            row.addWidget(sl)
            counts = [234, 56, 1278, 89, 12, 45, 672, 8]
            for i, zone_name in enumerate(ZONE_CONFIG.keys()):
                cell = ZoneFolderButton(zone_name, counts[i], state_key)
                cell.setFixedSize(70, 70)
                wrap = QWidget()
                wrap.setFixedSize(cell_w, cell_h)
                wrap_l = QHBoxLayout(wrap)
                wrap_l.setContentsMargins(0, 0, 0, 0)
                wrap_l.setAlignment(Qt.AlignCenter)
                wrap_l.addWidget(cell)
                row.addWidget(wrap)
            root.addLayout(row)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        W, H = self.width(), self.height()
        # 深色半透明背景
        bg = QLinearGradient(0, 0, 0, H)
        bg.setColorAt(0.0, QColor(25, 28, 48, 245))
        bg.setColorAt(1.0, QColor(12, 14, 28, 250))
        painter.fillRect(self.rect(), QBrush(bg))
        painter.end()


# ======================================================================
# 主渲染函数
# ======================================================================
def render_all(out_dir="screenshots"):
    os.makedirs(out_dir, exist_ok=True)
    print(f"输出目录: {os.path.abspath(out_dir)}")

    # 1. Dock 栏整体预览
    print("[1/3] 渲染 Dock 栏预览...")
    dock = MiniDock()
    out = os.path.join(out_dir, "preview_dock.png")
    render_widget_to_png(dock, out, with_shadow_bg=False,
                         bg_color=QColor(35, 38, 58, 255))
    print(f"  ✅ {out} ({os.path.getsize(out)} bytes)")

    # 2. 目录树弹出面板
    print("[2/3] 渲染目录树弹出面板...")
    popup = DirectoryTreePopup()
    out = os.path.join(out_dir, "preview_directory_tree.png")
    render_widget_to_png(popup, out, with_shadow_bg=False,
                         bg_color=QColor(35, 38, 58, 255))
    print(f"  ✅ {out} ({os.path.getsize(out)} bytes)")

    # 3. 文件夹图标三种状态对比网格
    print("[3/3] 渲染文件夹图标三种状态对比网格...")
    grid = FolderIconGrid()
    out = os.path.join(out_dir, "preview_folder_icons.png")
    render_widget_to_png(grid, out)
    print(f"  ✅ {out} ({os.path.getsize(out)} bytes)")

    print("\n🎉 全部预览图生成完成！")
    for f in sorted(os.listdir(out_dir)):
        if f.endswith(".png"):
            fp = os.path.join(out_dir, f)
            print(f"   - {f}  ({os.path.getsize(fp) // 1024} KB)")


def main():
    # AA_EnableHighDpiScaling 必须在 QCoreApplication 创建前设置
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication.instance() or QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 9))
    render_all("screenshots")
    print("\nDONE.")


if __name__ == "__main__":
    main()
