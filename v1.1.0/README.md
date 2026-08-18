# TidyUUUUp v1.1.0

> **Centered Island Edition**：以更少的常驻元素完成桌面文件的查看与搜索。

![居中小岛](./screenshots/v1.1.0_centered_island.png)

## 设计准则

v1.1.0 不再把所有功能放进小岛。默认状态仅展示一个无文字品牌标记、四个分类入口和一个搜索框，并由左右弹性空间将这一组内容严格置于小岛中心。文件数量、更新时间、关于信息和退出操作均移至菜单，避免常驻文案干扰桌面。

| 保留在小岛 | 移入菜单或托盘 |
| --- | --- |
| 本地文件分类 | 全部桌面文件 |
| 搜索桌面文件 | 重新扫描与恢复居中 |
| 文件列表入口 | 检查更新、关于与退出 |
| 搜索框焦点动画 | 系统托盘显示与退出 |

## 功能边界

TidyUUUUp 仅创建一个本地索引，用扩展名将桌面文件分为工作、图片、媒体、代码、归档和其他。分类与搜索都指向真实文件；双击可用默认程序打开文件，右键菜单支持在文件夹中显示、复制路径，并在可用时将文件移到回收站。程序不会自行整理、移动、重命名或上传文件。

| 功能 | 实现方式 |
| --- | --- |
| 实时性 | 每十秒检测桌面目录变更；发生变化时在后台线程重新索引，避免阻塞界面。 |
| 搜索 | 对真实文件名进行本地子串与词元匹配，并进行短暂防抖。 |
| 位置 | 默认显示在底部中心；拖动后记录位置，右键“恢复居中”可还原。 |
| 更新 | 后台检查公开 GitHub Release；下载包保存至用户下载目录，不接触设置目录。 |
| 设置 | Windows 下存放于 `%APPDATA%\TidyUUUUp\settings.json`，跨版本保留。 |

## Windows EXE 与快捷方式

构建过程将应用图标写入 EXE。首次运行打包后的 `TidyUUUUp.exe` 时，程序会在用户桌面生成或刷新 `TidyUUUUp.lnk`；快捷方式目标为当前 EXE，图标直接使用 EXE 内的品牌图标。若用户移动 EXE，下一次运行会自动将快捷方式指向新位置。

```powershell
# 仅在 Windows 上执行
python -m pip install -r requirements.txt pyinstaller
python ..\scripts\build_windows_release.py
```

构建脚本将生成 `dist/TidyUUUUp.exe`、`release/TidyUUUUp_v1.1.0_Windows.zip` 和对应的 SHA-256 文件。请在 Windows 环境执行该脚本，以获得可验证的 Windows 二进制文件。

## 目录说明

| 文件或目录 | 作用 |
| --- | --- |
| `main.py` | 居中小岛、分类、搜索、文件操作、托盘和快捷方式逻辑。 |
| `assets/tidyuuuup_app_icon.ico` | 用于 EXE、系统托盘和桌面快捷方式的多尺寸 Windows 图标。 |
| `create_shortcut.ps1` | 负责创建或更新 `.lnk` 的 PowerShell 脚本。 |
| `settings.py` | 将用户设置放在独立数据目录，保护更新过程中的用户偏好。 |
| `updater.py` 与 `update_dialog.py` | GitHub Release 更新检查及下载界面。 |
| `take_screenshot.py` | 生成离屏界面预览，供视觉回归核对。 |
