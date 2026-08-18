# TidyUUUUp v1.0.11 - Dynamic Island Dock

> 灵动岛风格 Dock，基于 PyQt6 重构

## 截图预览

### Dock 默认 Compact 状态（1120×116 高清）
![Dock 默认状态](./screenshots/01_dock_compact.png)

### 搜索框聚焦 → 弹簧拉伸（560 → 780px）
![Dock 拉伸状态](./screenshots/02_dock_stretched.png)

### 搜索框输入文字 + 实时语义搜索
![搜索激活状态](./screenshots/03_dock_search_active.png)

### 文件夹 Popover 弹出面板（AI 虚拟目录内容）
![文件夹 Popover](./screenshots/04_folder_popover.png)

### 完整桌面合成视图
![完整桌面](./screenshots/05_full_desktop.png)

### Dock + Popover 组合视图
![Dock + Popover](./screenshots/06_dock_with_popover.png)

> 截图在 Linux offscreen 平台生成（Windows Acrylic 效果仅在 Windows 10/11 上生效，截图中为普通半透明背景）。

## 核心特性

### 🏝️ 灵动岛 Dock
- 底部悬浮式工具栏，半透明深色玻璃底板
- Apple Spring Physics 弹簧伸缩动画
- 搜索框聚焦时宽度从 560px 弹性拉伸到 780px

### 🪟 Windows 原生 Acrylic 毛玻璃
- 通过 `ctypes` 调用 Windows `user32.SetWindowCompositionAttribute` API
- 启用 `ACCENT_ENABLE_ACRYLICBLURBEHIND` (状态 4)
- 深色模式背景色 `0xCC1E1E20`

### 📁 Apple 矢量蓝文件夹
- 用 `QPainterPath` 矢量绘制，不使用 Emoji
- 蓝色渐变主体（`#3399FF` → `#007AFF`）+ 后背板 tab
- 点击弹出 AI 虚拟目录内容

### 🔍 AI 虚拟目录 + 语义搜索
- 物理桌面文件不移动，仅做语义分类映射
- 搜索框实时显示匹配结果（带相似度百分比）
- Popover 悬浮面板展示文件列表

### 🕐 常驻时钟
- 右下角嵌入时间（`hh:mm A`）+ 日期（`MM/dd ddd`）
- 每秒刷新

## 组件结构

```
main.py
├── StackedLogoWidget        # Tidy / UUUUp 品牌堆叠 Logo
├── AppleVectorFolderIcon    # 矢量蓝文件夹图标（可点击）
├── TopPopoverPanel          # 悬浮毛玻璃弹出面板
└── TidyDynamicIslandDock    # 灵动岛主窗口
    ├── Pinned Apps          # 固定应用（浏览器、终端）
    ├── AI Virtual Folders   # 3 个虚拟目录文件夹
    ├── Search Pill          # 药丸型搜索框
    └── Clock                # 时钟日期
```

## 运行

### 依赖
```
PyQt6>=6.5.0
```

### 启动
```bash
pip install -r requirements.txt
python main.py
```

> **注意**：Windows Acrylic 效果仅在 Windows 10/11 上生效，其他平台会自动降级为普通半透明背景（不影响功能）。

## Bug 修正记录

### 1. `pyqtProperty` 未导入（已修正）
**问题**：原代码在 `TidyDynamicIslandDock` 类中使用了 `pyqtProperty(int, get_dock_width, set_dock_width)` 来定义 `dockWidth` 属性（供 `QPropertyAnimation` 动画使用），但未从 `PyQt6.QtCore` 导入 `pyqtProperty`，导致运行时 `NameError`。

**修正**：在导入列表中添加 `pyqtProperty`：
```python
from PyQt6.QtCore import (..., pyqtSignal, pyqtProperty)
```

## 技术栈

- **PyQt6**（从 v1.0.10 的 PyQt5 升级）
- **ctypes** 调用 Windows `user32` DWM API
- **QPropertyAnimation** + **QEasingCurve.OutBack** 实现弹簧回弹动画
