# TidyUUUUp

> **TidyUUUUp** 是面向 Windows 的轻量桌面整理工具。它在本地扫描桌面文件，提供分类浏览、搜索和文件操作，并以低干扰的悬浮小岛呈现最常用入口。

![TidyUUUUp v1.1.1 居中小岛预览](./v1.1.1/screenshots/01_centered_compact.png)

## 当前版本：v1.1.1

v1.1.1 延续正式品牌图标和截图集，并将小岛收敛为一个**真正居中的主操作区**。默认界面只保留品牌标记、四个分类文件夹和搜索入口；时钟、重复分隔线、固定浏览器/终端按钮及模拟文案均被移除。较少使用的命令已转入右键菜单和系统托盘，因此界面更安静，功能仍可直接访问。

| 项目 | v1.1.1 行为 |
| --- | --- |
| 桌面整理 | 在本地按工作、图片、媒体和代码分类真实桌面文件，不移动、不上传文件。 |
| 搜索与文件操作 | 支持文件名搜索、双击打开、在文件夹中显示、复制路径；安装 `send2trash` 时可显式移到回收站。 |
| 小岛布局 | 小岛内的常驻内容由左右弹性空间包围，默认始终视觉居中；拖动后的自定义位置会被记住，可一键恢复居中。 |
| 后台能力 | 保留后台扫描、目录变化检测、系统托盘、更新检查和用户设置持久化。 |
| Windows 发布 | 自动构建单文件 `TidyUUUUp.exe`；EXE 首次启动会在桌面生成或刷新带应用图标的快捷方式。 |

## 下载与启动

发布完成后，请从 [GitHub Releases](https://github.com/BigCake2026/TidyUUUUp/releases) 下载 `TidyUUUUp_v1.1.1_Windows.zip`，解压后运行 `TidyUUUUp.exe`。程序第一次启动时会自动在当前用户桌面创建 `TidyUUUUp.lnk`，图标与 EXE 保持一致；压缩包中也附带 `create_shortcut.ps1`，可在需要时手动重建快捷方式。

| 文件 | 用途 |
| --- | --- |
| `TidyUUUUp.exe` | 无需安装的 Windows 单文件应用。 |
| `create_shortcut.ps1` | 快捷方式辅助脚本；通常由 EXE 首次启动自动调用。 |
| `README.md` | 当前发布包的快速使用说明。 |
| `*.sha256` | 发布压缩包的 SHA-256 完整性校验值。 |

## 仓库结构与版本保留

当前仓库采用“**新版本目录 + 历史版本快照**”策略。最新版本独立存放在 `v1.1.1/`；`v1.0.1` 至 `v1.1.0` 的目录、既有分支、标签与提交历史均保留，不重写、不删除。历史版本清单见 [VERSIONS.md](./VERSIONS.md)。

| 路径 | 说明 |
| --- | --- |
| [`v1.1.1/`](./v1.1.1/) | 当前稳定开发版本：正式品牌图标、居中小岛、真实本地索引与自动快捷方式。 |
| [`v1.0.1/` — `v1.1.0/`](./VERSIONS.md) | 原始历史版本快照，仅归档，不覆盖。 |
| [`scripts/build_windows_release.py`](./scripts/build_windows_release.py) | Windows EXE、ZIP 与 SHA-256 的可重复构建入口。 |

## 构建与发布

Windows EXE 必须在 Windows 环境构建，以避免在非 Windows 环境中伪造或交叉编译不可验证的二进制文件。仓库提供可重复执行的构建脚本；构建产物位于 `dist/` 和 `release/`，这两个目录不会被提交到版本库。

```powershell
python -m pip install -r v1.1.1/requirements.txt pyinstaller
python scripts/build_windows_release.py
```

## 隐私与安全边界

文件索引与分类逻辑完全在本地运行。程序不会自动移动、重命名、上传或删除任何桌面文件；“移到回收站”仅会在用户从文件右键菜单明确选择后执行。更新检查仅访问公开的 GitHub Release 接口。
