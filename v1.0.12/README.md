# TidyUUUUp v1.0.12 - Dynamic Island Dock (更新检测 + 流畅度版)

> 灵动岛风格 Dock，基于 PyQt6 重构。v1.0.12 新增 GitHub 自动更新检测与多项流畅度优化，且完全保留用户数据。

## v1.0.12 新功能

### 🆕 GitHub 自动更新检测
- 启动后台检测 GitHub 最新 Release（`GET /repos/{owner}/{repo}/releases/latest`），语义化比较版本号
- 自动识别任意高位版本：`v1.0.12` / `1.1.0` / `2.0.0`（自动去掉 `v` 前缀，支持预发布号 `1.0.13-rc1`）
- 有更新时弹出深色玻璃风格更新对话框（changelog + 下载进度 + 跳过此版本 + 打开 Release 页面）
- 托盘 / Dock 右键菜单可随时「检查更新」
- 自动检查 24 小时冷却，不打扰；支持「跳过此版本」

### 🔒 用户数据 100% 保留
- 用户设置保存在独立目录（与应用名/脚本名无关，跨版本稳定）：
  - Windows: `%APPDATA%\TidyUUUUp\settings.json`
  - macOS: `~/Library/Application Support/TidyUUUUp/settings.json`
  - Linux: `~/.local/share/TidyUUUUp/settings.json`
- 更新包仅下载到用户「下载」目录，**绝不触碰用户数据目录**
- 桌面位置、更新偏好、跳过版本等跨版本保留

### ⚡ 流畅度提升
- **搜索框输入防抖 250ms**：避免每次按键重建结果，大桌面更顺滑
- **桌面扫描 mtime 检测 + 后台 QThread**：仅当桌面目录变化才重算索引，扫描在子线程执行，UI 永不卡顿
- **弹簧动画改用 OutQuint 曲线**，更柔和顺滑
- **Popover 改为常驻 Tool 悬浮面板**（不再被 ToolTip 自动隐藏机制误关，更稳定）
- 文件列表按名排序，结果稳定可读

## 截图预览

### Dock 默认 Compact 状态（1120×116 高清）
![Dock 默认状态](./screenshots/01_dock_compact.png)

### 搜索框聚焦 → 弹簧拉伸（560 → 780px）
![Dock 拉伸状态](./screenshots/02_dock_stretched.png)

### 搜索框输入文字 + 实时语义搜索（防抖）
![搜索激活状态](./screenshots/03_dock_search_active.png)

### 文件夹 Popover 弹出面板（真实桌面文件）
![文件夹 Popover](./screenshots/04_folder_popover.png)

### Dock 完整视图
![Dock 完整](./screenshots/05_dock_full_compact.png)

> 截图在 Linux offscreen 平台生成（Windows Acrylic 效果仅在 Windows 10/11 上生效，截图中为普通半透明背景）。

## 核心特性

### 🏝️ 灵动岛 Dock
- 底部悬浮式工具栏，半透明深色玻璃底板
- Apple Spring Physics 弹簧伸缩动画（OutQuint 曲线，更顺滑）
- 搜索框聚焦时宽度从 560px 弹性拉伸到 780px
- **可拖动**：按住空白区域拖动 Dock 位置（位置自动保存）

### 🪟 Windows 原生 Acrylic 毛玻璃
- 通过 `ctypes` 调用 Windows `user32.SetWindowCompositionAttribute` API
- 启用 `ACCENT_ENABLE_ACRYLICBLURBEHIND` (状态 4)
- 深色模式背景色 `0xCC1E1E20`
- 非 Windows 平台自动降级为 QPainter 半透明玻璃底板

### 📁 Apple 矢量蓝文件夹
- 用 `QPainterPath` 矢量绘制，不使用 Emoji
- 蓝色渐变主体（`#3399FF` → `#007AFF`）+ 后背板 tab
- hover 高光反馈
- 点击弹出 **真实桌面文件** 的 AI 虚拟目录分类

### 🔍 真实桌面扫描 + 模糊搜索（防抖）
- 启动时扫描用户桌面（`QStandardPaths` / SHGetKnownFolderPath，跨平台）
- 按扩展名 + 关键词本地分类（无需联网 / AI）
- 搜索框基于真实文件名做模糊匹配 + 相似度评分，250ms 防抖后显示结果
- Popover 双击打开文件 / 右键在文件夹中显示 / 复制路径 / 移到回收站

### 🕐 常驻时钟
- 右下角嵌入时间（`hh:mm A`）+ 日期（`MM/dd ddd`）
- 每秒刷新

### 📌 固定应用（真正可点击）
- 🌐 浏览器：打开系统默认浏览器
- 💻 终端：打开系统默认终端（Windows Terminal / Terminal.app / xterm 等）

### 🔄 更新检测
- 启动后 2.5 秒后台检查 GitHub 更新（尊重 24h 冷却与「跳过此版本」）
- 托盘 / Dock 右键菜单「检查更新」可手动触发

### 🧰 系统托盘 + 右键菜单
- 托盘图标：显示 Dock / 检查更新 / 重新扫描 / 关于 / 退出
- Dock 右键菜单：检查更新 / 重新扫描 / 关于 / 退出
- 每 10 秒检测桌面 mtime，变化时后台重扫

## 组件结构

```
main.py
├── DesktopIndex             # 真实桌面扫描（mtime 检测）+ 本地分类 + 模糊搜索
├── DesktopScanWorker        # 后台扫描线程（流畅度）
├── StackedLogoWidget        # Tidy / UUUUp 品牌堆叠 Logo
├── AppleVectorFolderIcon    # 矢量蓝文件夹图标（可点击 + hover）
├── TopPopoverPanel          # 常驻 Tool 悬浮面板（真实文件 + 右键菜单）
└── TidyDynamicIslandDock    # 灵动岛主窗口（搜索防抖 + 更新检测集成）
settings.py
└── UserSettings             # 用户数据持久化（跨版本稳定路径）
updater.py
├── UpdateChecker            # GitHub Release 检测 + semver 比较
└── UpdateDownloader         # 下载到下载目录（保留用户数据）
update_dialog.py
└── UpdateDialog             # 深色玻璃更新对话框（changelog + 进度 + 跳过）
└── 系统托盘 + 右键菜单       # 显示 / 检查更新 / 重新扫描 / 关于 / 退出
```

## 运行

### 依赖
```
PyQt6>=6.5.0
send2trash>=1.8.0  # 可选：移到回收站（缺失时右键菜单自动隐藏该项）
```

### 启动
```bash
pip install -r requirements.txt
python main.py
```

> **注意**：Windows Acrylic 效果仅在 Windows 10/11 上生效，其他平台会自动降级为普通半透明背景（不影响功能）。
> 更新检测使用未认证 GitHub API（60 次/小时/IP），桌面应用足够；无需任何 token。

## 用户数据与更新

- **用户数据位置**：见上方「用户数据 100% 保留」。该目录与程序代码目录完全分离，更新（替换代码）不会影响用户数据。
- **更新流程**：检测到新版本 → 弹出对话框 → 下载到「下载」目录 → 打开下载文件夹 → 用户解压替换程序目录（设置与桌面索引自动保留）。
- **更新检测仓库**：默认 `BigCake2026/TidyUUUUp`，可在 `settings.json` 的 `update_repo` 字段修改。

## 技术栈

- **PyQt6**（从 v1.0.10 的 PyQt5 升级）
- **ctypes** 调用 Windows `user32` DWM API
- **QPropertyAnimation** + **QEasingCurve.OutQuint** 实现柔和弹簧动画
- **QThread** 后台扫描与更新检测，UI 不阻塞
- **urllib** 访问 GitHub Releases API（无需第三方依赖）
