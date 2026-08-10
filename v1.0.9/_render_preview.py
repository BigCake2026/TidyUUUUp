#!/usr/bin/env python3#!/usr/bin/env python3
"""
离线预览渲染脚本 - 无需显示环境即可生成 PNG 截图
渲染内容#!/usr/bin/env python3
"""
离线预览渲染脚本 - 无需显示环境即可生成 PNG 截图
渲染内容：
  1. Liquid Glass Dock 栏 (含 3D ZoneFolderButton#!/usr/bin/env python3
"""
离线预览渲染脚本 - 无需显示环境即可生成 PNG 截图
渲染内容：
  1. Liquid Glass Dock 栏 (含 3D ZoneFolderButton 文件夹图标)
  2. 目录树弹出面板 DirectoryTreePopup
使用 QT_Q#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'off#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPain#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    ##!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.S#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 8#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28,#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 6#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220,#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0,#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x,#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PN#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬',#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#0#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindow#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880,#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().set#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_e#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmap#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path =#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2,#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0,#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.set#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect =#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 2#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0,#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92,#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.set#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setCli#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() -#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinear#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.5#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(2#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() -#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 1#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0,#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0,#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 25#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.set#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 5#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width()#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top =#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
                sg = QLinearGradient(0#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
                sg = QLinearGradient(0, sep_top, 0, sep_bot)
                sg.setColorAt(0.0, QColor(255,#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
                sg = QLinearGradient(0, sep_top, 0, sep_bot)
                sg.setColorAt(0.0, QColor(255, 255, 255, 0))
                sg.setColorAt(0#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
                sg = QLinearGradient(0, sep_top, 0, sep_bot)
                sg.setColorAt(0.0, QColor(255, 255, 255, 0))
                sg.setColorAt(0.5, QColor(255, 255, 255,#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
                sg = QLinearGradient(0, sep_top, 0, sep_bot)
                sg.setColorAt(0.0, QColor(255, 255, 255, 0))
                sg.setColorAt(0.5, QColor(255, 255, 255, 55))
                sg.setColorAt(1.0, QColor(255, 255, 25#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
                sg = QLinearGradient(0, sep_top, 0, sep_bot)
                sg.setColorAt(0.0, QColor(255, 255, 255, 0))
                sg.setColorAt(0.5, QColor(255, 255, 255, 55))
                sg.setColorAt(1.0, QColor(255, 255, 255, 0))
                painter.setBrush(QBrush(sg))
                painter.drawPath#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
                sg = QLinearGradient(0, sep_top, 0, sep_bot)
                sg.setColorAt(0.0, QColor(255, 255, 255, 0))
                sg.setColorAt(0.5, QColor(255, 255, 255, 55))
                sg.setColorAt(1.0, QColor(255, 255, 255, 0))
                painter.setBrush(QBrush(sg))
                painter.drawPath(path)

    dock = MiniDock()
    out = os.path.join(out_dir,#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
                sg = QLinearGradient(0, sep_top, 0, sep_bot)
                sg.setColorAt(0.0, QColor(255, 255, 255, 0))
                sg.setColorAt(0.5, QColor(255, 255, 255, 55))
                sg.setColorAt(1.0, QColor(255, 255, 255, 0))
                painter.setBrush(QBrush(sg))
                painter.drawPath(path)

    dock = MiniDock()
    out = os.path.join(out_dir, 'preview_dock.png')
    render_widget_to_png(dock, out, with_sh#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
                sg = QLinearGradient(0, sep_top, 0, sep_bot)
                sg.setColorAt(0.0, QColor(255, 255, 255, 0))
                sg.setColorAt(0.5, QColor(255, 255, 255, 55))
                sg.setColorAt(1.0, QColor(255, 255, 255, 0))
                painter.setBrush(QBrush(sg))
                painter.drawPath(path)

    dock = MiniDock()
    out = os.path.join(out_dir, 'preview_dock.png')
    render_widget_to_png(dock, out, with_shadow_bg=True)
    print(f'[OK] 生成: {out}')
    return out


def render_folder_icons_grid#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
                sg = QLinearGradient(0, sep_top, 0, sep_bot)
                sg.setColorAt(0.0, QColor(255, 255, 255, 0))
                sg.setColorAt(0.5, QColor(255, 255, 255, 55))
                sg.setColorAt(1.0, QColor(255, 255, 255, 0))
                painter.setBrush(QBrush(sg))
                painter.drawPath(path)

    dock = MiniDock()
    out = os.path.join(out_dir, 'preview_dock.png')
    render_widget_to_png(dock, out, with_shadow_bg=True)
    print(f'[OK] 生成: {out}')
    return out


def render_folder_icons_grid(out_dir):
    """单独渲染所有文件夹#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
                sg = QLinearGradient(0, sep_top, 0, sep_bot)
                sg.setColorAt(0.0, QColor(255, 255, 255, 0))
                sg.setColorAt(0.5, QColor(255, 255, 255, 55))
                sg.setColorAt(1.0, QColor(255, 255, 255, 0))
                painter.setBrush(QBrush(sg))
                painter.drawPath(path)

    dock = MiniDock()
    out = os.path.join(out_dir, 'preview_dock.png')
    render_widget_to_png(dock, out, with_shadow_bg=True)
    print(f'[OK] 生成: {out}')
    return out


def render_folder_icons_grid(out_dir):
    """单独渲染所有文件夹图标（默认/悬停/按下 三种状态对比）"""
    from PyQt5#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
                sg = QLinearGradient(0, sep_top, 0, sep_bot)
                sg.setColorAt(0.0, QColor(255, 255, 255, 0))
                sg.setColorAt(0.5, QColor(255, 255, 255, 55))
                sg.setColorAt(1.0, QColor(255, 255, 255, 0))
                painter.setBrush(QBrush(sg))
                painter.drawPath(path)

    dock = MiniDock()
    out = os.path.join(out_dir, 'preview_dock.png')
    render_widget_to_png(dock, out, with_shadow_bg=True)
    print(f'[OK] 生成: {out}')
    return out


def render_folder_icons_grid(out_dir):
    """单独渲染所有文件夹图标（默认/悬停/按下 三种状态对比）"""
    from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout

    class#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
                sg = QLinearGradient(0, sep_top, 0, sep_bot)
                sg.setColorAt(0.0, QColor(255, 255, 255, 0))
                sg.setColorAt(0.5, QColor(255, 255, 255, 55))
                sg.setColorAt(1.0, QColor(255, 255, 255, 0))
                painter.setBrush(QBrush(sg))
                painter.drawPath(path)

    dock = MiniDock()
    out = os.path.join(out_dir, 'preview_dock.png')
    render_widget_to_png(dock, out, with_shadow_bg=True)
    print(f'[OK] 生成: {out}')
    return out


def render_folder_icons_grid(out_dir):
    """单独渲染所有文件夹图标（默认/悬停/按下 三种状态对比）"""
    from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout

    class Grid(QWidget):
        def __init__(self):
            super().__init__()
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
                sg = QLinearGradient(0, sep_top, 0, sep_bot)
                sg.setColorAt(0.0, QColor(255, 255, 255, 0))
                sg.setColorAt(0.5, QColor(255, 255, 255, 55))
                sg.setColorAt(1.0, QColor(255, 255, 255, 0))
                painter.setBrush(QBrush(sg))
                painter.drawPath(path)

    dock = MiniDock()
    out = os.path.join(out_dir, 'preview_dock.png')
    render_widget_to_png(dock, out, with_shadow_bg=True)
    print(f'[OK] 生成: {out}')
    return out


def render_folder_icons_grid(out_dir):
    """单独渲染所有文件夹图标（默认/悬停/按下 三种状态对比）"""
    from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout

    class Grid(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
                sg = QLinearGradient(0, sep_top, 0, sep_bot)
                sg.setColorAt(0.0, QColor(255, 255, 255, 0))
                sg.setColorAt(0.5, QColor(255, 255, 255, 55))
                sg.setColorAt(1.0, QColor(255, 255, 255, 0))
                painter.setBrush(QBrush(sg))
                painter.drawPath(path)

    dock = MiniDock()
    out = os.path.join(out_dir, 'preview_dock.png')
    render_widget_to_png(dock, out, with_shadow_bg=True)
    print(f'[OK] 生成: {out}')
    return out


def render_folder_icons_grid(out_dir):
    """单独渲染所有文件夹图标（默认/悬停/按下 三种状态对比）"""
    from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout

    class Grid(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(900, 360)

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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
                sg = QLinearGradient(0, sep_top, 0, sep_bot)
                sg.setColorAt(0.0, QColor(255, 255, 255, 0))
                sg.setColorAt(0.5, QColor(255, 255, 255, 55))
                sg.setColorAt(1.0, QColor(255, 255, 255, 0))
                painter.setBrush(QBrush(sg))
                painter.drawPath(path)

    dock = MiniDock()
    out = os.path.join(out_dir, 'preview_dock.png')
    render_widget_to_png(dock, out, with_shadow_bg=True)
    print(f'[OK] 生成: {out}')
    return out


def render_folder_icons_grid(out_dir):
    """单独渲染所有文件夹图标（默认/悬停/按下 三种状态对比）"""
    from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout

    class Grid(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(900, 360)

            root = QVBoxLayout(self)
            root.setContentsMargins(20,#!/usr/bin/env python3
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

# 强制使用 offscreen 平台，避免 DISPLAY 报错
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QTimer
from PyQt5.QtGui import (
    QPainter, QColor, QPixmap, QImage, QPainterPath,
    QLinearGradient, QRadialGradient, QBrush
)
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 注册组件
from ui.zone_panel import ZoneFolderButton, DirectoryTreePopup


def render_widget_to_png(widget, out_path, size=None, with_shadow_bg=True):
    """把 QWidget 渲染成 PNG，可选灰色渐变背景"""
    if size is None:
        widget.adjustSize()
        size = widget.size()
    else:
        widget.resize(size)

    # 确保 layout/子控件就位
    QApplication.processEvents()

    w, h = widget.width(), widget.height()
    # 画一个大一点的画布（加 padding）
    pad_x = 40
    pad_y_top = 60
    pad_y_bot = 60
    total_w = w + pad_x * 2
    total_h = h + pad_y_top + pad_y_bot

    img = QImage(total_w, total_h, QImage.Format_ARGB32)
    img.fill(Qt.transparent)

    painter = QPainter(img)
    painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

    # 背景：浅色桌面渐变，让 Dock 有底托
    bg_rect = img.rect()
    if with_shadow_bg:
        bg = QLinearGradient(0, 0, 0, bg_rect.height())
        bg.setColorAt(0.0, QColor(40, 52, 82))
        bg.setColorAt(0.5, QColor(28, 34, 56))
        bg.setColorAt(1.0, QColor(18, 20, 32))
        painter.fillRect(bg_rect, QBrush(bg))
        # 中间画一点虚化光晕（模拟桌面壁纸光）
        halo = QRadialGradient(
            bg_rect.center().x(),
            bg_rect.center().y() - bg_rect.height() * 0.1,
            bg_rect.width() * 0.6
        )
        halo.setColorAt(0.0, QColor(120, 90, 220, 60))
        halo.setColorAt(0.5, QColor(80, 120, 220, 30))
        halo.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.fillRect(bg_rect, QBrush(halo))

    # 先让 widget 自绘到临时 pixmap
    tmp = QPixmap(widget.size())
    tmp.fill(Qt.transparent)
    widget.render(tmp, QPoint(0, 0))
    painter.drawPixmap(pad_x, pad_y_top, tmp)

    painter.end()
    img.save(out_path, "PNG")
    return out_path


def build_mock_zone_configs():
    return {
        '图片':   {'color': '#FF5A8F', 'icon': '🖼️', 'patterns': []},
        '视频':   {'color': '#7A5CFF', 'icon': '🎬', 'patterns': []},
        '文档':   {'color': '#4A9DFF', 'icon': '📄', 'patterns': []},
        '下载':   {'color': '#22C55E', 'icon': '⬇️', 'patterns': []},
        '工作':   {'color': '#F59E0B', 'icon': '💼', 'patterns': []},
        '学习':   {'color': '#06B6D4', 'icon': '📚', 'patterns': []},
    }


def render_dock_preview(out_dir):
    """渲染一整条 Dock，包含 6 个 ZoneFolderButton 文件夹图标"""
    from PyQt5.QtWidgets import QHBoxLayout

    # 直接用 DockBar 会依赖很多信号和 tray，我们用一个简易 QWidget 重绘 paintEvent
    class MiniDock(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(880, 82)
            self.setLayout(QHBoxLayout(self))
            self.layout().setContentsMargins(14, 9, 14, 9)
            self.layout().setSpacing(5)

            # 伪造 6 个 ZoneFolderButton
            self._buttons = []
            configs = build_mock_zone_configs()
            for name, cfg in configs.items():
                btn = ZoneFolderButton(name, cfg)
                # 设置文件数量徽标
                import random
                btn.set_file_count(random.randint(3, 256))
                self.layout().addWidget(btn)
                self._buttons.append(btn)

            # 模拟 hover 第一个按钮（让它显示缩放+光晕）
            first = self._buttons[1]  # '视频' 用紫色好看
            first._hovered = True
            first._hover_progress = 0.85
            first._update_effect()
            # 让一个按钮按压
            third = self._buttons[3]
            third._pressed = True
            third._press_progress = 0.6
            third._update_effect()

        def paintEvent(self, event):
            """拷贝自 DockBar 的 Liquid Glass 背景画法"""
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
            rect = self.rect()

            # 外发光
            glow_path = QPainterPath()
            glow_rect = QRect(rect.x() + 2, rect.y() + 5, rect.width() - 4, rect.height() + 2)
            glow_path.addRoundedRect(glow_rect, 26, 26)
            shadow = QRadialGradient(
                glow_rect.center().x(),
                glow_rect.bottom() - 2,
                glow_rect.width() * 0.55
            )
            shadow.setColorAt(0.0, QColor(0, 0, 0, 90))
            shadow.setColorAt(0.55, QColor(0, 0, 0, 28))
            shadow.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QBrush(shadow))
            painter.drawPath(glow_path)

            # 主体渐变
            body_path = QPainterPath()
            body_rect = QRect(rect).adjusted(1.5, 1.5, -1.5, -1.5)
            body_path.addRoundedRect(body_rect, 24, 24)
            bg = QLinearGradient(0, 0, 0, rect.height())
            bg.setColorAt(0.0, QColor(58, 64, 92, 200))
            bg.setColorAt(0.35, QColor(38, 42, 62, 210))
            bg.setColorAt(1.0, QColor(22, 24, 38, 230))
            painter.fillPath(body_path, QBrush(bg))

            # 顶部高光
            painter.setClipping(True)
            painter.setClipRect(2, 2, rect.width() - 4, int(rect.height() * 0.55))
            hl = QLinearGradient(0, 2, 0, int(rect.height() * 0.55 + 2))
            hl.setColorAt(0.0, QColor(255, 255, 255, 78))
            hl.setColorAt(0.6, QColor(255, 255, 255, 24))
            hl.setColorAt(1.0, QColor(255, 255, 255, 0))
            painter.fillPath(body_path, QBrush(hl))
            painter.setClipping(False)

            # 底部内阴影
            painter.setClipping(True)
            painter.setClipRect(2, rect.height() - 10, rect.width() - 4, 10)
            bs = QLinearGradient(0, rect.height() - 10, 0, rect.height())
            bs.setColorAt(0.0, QColor(0, 0, 0, 0))
            bs.setColorAt(1.0, QColor(0, 0, 0, 60))
            painter.fillPath(body_path, QBrush(bs))
            painter.setClipping(False)

            # 外边框
            from PyQt5.QtGui import QPen
            painter.setPen(QPen(QColor(255, 255, 255, 55), 1.1))
            painter.setBrush(Qt.NoBrush)
            painter.drawPath(body_path)

            # 内部高光边框
            inner = QRect(body_rect.x() + 1.5, body_rect.y() + 1.5,
                          body_rect.width() - 3, body_rect.height() - 3)
            inner_path = QPainterPath()
            inner_path.addRoundedRect(inner, 22, 22)
            painter.setPen(QPen(QColor(255, 255, 255, 42), 0.6))
            painter.drawPath(inner_path)

            # 顶部反光细线
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 50))
            painter.drawRoundedRect(QRect(5, 3, rect.width() - 10, 1), 1, 1)

            # 分隔符
            for x_ratio in [0.08, 0.92]:
                cx = int(rect.x() + rect.width() * x_ratio)
                sep_top = rect.top() + 10
                sep_bot = rect.bottom() - 10
                path = QPainterPath()
                path.addRoundedRect(QRect(cx - 0.6, sep_top, 1.2, sep_bot - sep_top), 0.6, 0.6)
                sg = QLinearGradient(0, sep_top, 0, sep_bot)
                sg.setColorAt(0.0, QColor(255, 255, 255, 0))
                sg.setColorAt(0.5, QColor(255, 255, 255, 55))
                sg.setColorAt(1.0, QColor(255, 255, 255, 0))
                painter.setBrush(QBrush(sg))
                painter.drawPath(path)

    dock = MiniDock()
    out = os.path.join(out_dir, 'preview_dock.png')
    render_widget_to_png(dock, out, with_shadow_bg=True)
    print(f'[OK] 生成: {out}')
    return out


def render_folder_icons_grid(out_dir):
    """单独渲染所有文件夹图标（默认/悬停/按下 三种状态对比）"""
    from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout

    class Grid(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.resize(900, 360)

            root = QVBoxLayout(self)
            root.setContentsMargins(20, 20, 20, 20)
            root.setSpacing(18