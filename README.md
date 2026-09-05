# TidyUUUUp
> **TidyUUUUp** 是面向 Windows 的轻量桌面整理工具。它在本地扫描桌面文件，提供分类浏览、搜索和文件操作，并以悬浮小岛呈现最常用入口。

![TidyUUUUp v2.0.0 Liquid Glass 小岛预览](./v2.0.0/screenshots/01_liquid_glass_dock.png)

## 当前版本：v2.0.0（Liquid Glass 系列首发）

v2.0.0 是 **Liquid Glass 系列**的第一个版本：UI 全面采用苹果 Liquid Glass 设计语言——半透明亚克力基底、垂直深度渐变、顶部镜面高光、折射边缘双层边框、底部内阴影，通透度对标苹果控制中心。所有功能与 v1.x 完全一致，仅重写 UI 绘制层。

| 项目 | v2.0.0 行为 |
| --- | --- |
| UI 风格 | 苹果 Liquid Glass 通透玻璃：alpha 119-152 半透明基底、顶部镜面高光、双层折射边缘、底部内阴影、玻璃质感图标与搜索框。 |
| 文件分类 | 在本地按工作、图片、媒体和代码分类真实桌面文件，不移动、不上传文件。 |
| 搜索与文件操作 | 支持文件名搜索、双击打开、在文件夹中显示、复制路径；安装 `send2trash` 时可显式移到回收站。 |
| 小岛布局 | 底部居中悬浮小岛，保留搜索聚焦时的弹性展开与拖动位置记忆。 |
| Windows 安装 | 发布一个 `TidyUUUUp_Setup_v2.0.0.exe`，双击即可安装，并自动创建带品牌图标的桌面与开始菜单快捷方式。 |
| 后台能力 | 保留后台扫描、目录变化检测、系统托盘、更新检查和用户设置持久化。 |

## 版本系列

| 系列 | 版本 | UI 风格 |
| --- | --- | --- |
| 经典系列 | v1.0.1 – v1.1.2 | Classic UI，经典小岛 |
| **Liquid Glass 系列** | **v2.0.0 起** | 苹果 Liquid Glass 通透玻璃 |

## 下载与安装

请从 [GitHub Releases](https://github.com/BigCake2026/TidyUUUUp/releases) 下载单个 `TidyUUUUp_Setup_v2.0.0.exe` 文件并双击。安装程序会将应用安装至当前用户的本地应用目录，自动创建 **桌面快捷方式** 和 **开始菜单入口**，安装完成后可直接启动应用。无需解压 ZIP 或执行 PowerShell。

随 Release 提供的 `*.sha256` 文件用于校验安装程序完整性。应用也保留首次启动时的快捷方式修复逻辑，以避免安装路径变化后出现失效入口。

## GitHub 更新检查与用户数据

更新检查始终启用，用户不能关闭自动检查或跳过某个新版本。应用每次启动都会在后台检查公开 GitHub Release；发现更高版本时优先下载单文件 Setup EXE，并在用户点击“安装更新”后执行。安装程序仅替换当前用户应用目录；`%APPDATA%/TidyUUUUp/settings.json`、桌面索引路径、小岛位置和快捷方式记录均保持不变，更新下载也仅写入用户下载目录。

## 仓库结构与版本保留

当前仓库采用“**新版本目录 + 历史版本快照**”策略。最新版本独立存放在 `v2.0.0/`；`v1.0.1` 至 `v1.2.0` 的目录、既有分支、标签与提交历史均保留，不重写、不删除。完整清单见 [VERSIONS.md](./VERSIONS.md)。

| 路径 | 说明 |
| --- | --- |
| [`v2.0.0/`](./v2.0.0/) | **当前 Liquid Glass 系列**：苹果玻璃 UI、正式图标、真实本地索引、自动快捷方式和单文件安装程序。 |
| [`v1.2.0/`](./v1.2.0/) | Liquid Glass Edition（系列过渡版，经典目录结构）。 |
| [`v1.0.1/` — `v1.1.2/`](./VERSIONS.md) | 历史版本快照，仅归档，不覆盖。 |
| [`scripts/build_windows_release.py`](./scripts/build_windows_release.py) | Windows 应用 EXE、单文件安装程序和 SHA-256 的可重复构建入口。 |

## 构建与发布

Windows 安装程序必须在 Windows 环境构建。仓库的自动构建流程会安装应用依赖和 Inno Setup，生成单个安装程序并发布到对应 GitHub Release。

```powershell
python -m pip install -r v2.0.0/requirements.txt pyinstaller
choco install innosetup --yes
python scripts/build_windows_release.py
```

## 隐私与安全边界

文件索引与分类逻辑完全在本地运行。程序不会自动移动、重命名、上传或删除任何桌面文件；“移到回收站”仅会在用户从文件右键菜单明确选择后执行。更新检查仅访问公开的 GitHub Release 接口。
