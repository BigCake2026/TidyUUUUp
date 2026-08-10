# GitHub Actions 自动打包说明

本项目已配置自动打包 Windows EXE 的 workflow。

## 触发方式

### 方式一：手动触发（推荐，会自动创建 Release）

1. 打开 GitHub 仓库: https://github.com/BigCake2026/TidyUUUUpCode
2. 点击 **Actions** 标签页
3. 在左侧选择 **Build Windows EXE** workflow
4. 点击右侧 **Run workflow** 按钮
5. 填写参数：
   - `release_tag`: 版本号（例如 `v1.0.9`）
   - `make_latest`: 是否设为最新 Release（默认 `true`）
6. 点击绿色 **Run workflow** 按钮

等待约 5-10 分钟，构建完成后会：
- 在 [Releases 页面](https://github.com/BigCake2026/TidyUUUUpCode/releases) 自动创建新 Release
- 上传 `TidyUUUUp.exe`（单文件可执行程序）
- 上传 `TidyUUUUp_v1.0.9.zip`（完整发布包）

### 方式二：推送代码自动触发（仅构建，不创建 Release）

当推送到 `main` 分支且修改了以下文件时，会自动触发构建：
- `ui/**` (UI 组件)
- `core/**` (核心逻辑)
- `main.py` (主程序)
- `version.json` (版本信息)
- `requirements.txt` (依赖列表)

构建产物会作为 Artifact 上传，可在 Action 运行页面下载（保留 30 天）。
**不会自动创建 Release**，避免每次推送都发版。

## 下载 EXE

构建完成后，从以下位置下载：

1. **Release 页面**: https://github.com/BigCake2026/TidyUUUUpCode/releases
   - 下载 `TidyUUUUp_v1.0.9.zip` 完整包
   - 或下载 `TidyUUUUp.exe` 单文件

2. **Action 运行页面**（仅手动/自动触发的构建）:
   - 打开 Actions → 选择对应运行 → 下拉到 Artifacts 区域
   - 下载 `TidyUUUUp-windows-exe` 压缩包

## 构建产物

| 文件 | 说明 | 大小 |
|---|---|---|
| `TidyUUUUp.exe` | 单文件可执行程序，双击即可运行 | ~35 MB |
| `TidyUUUUp_v1.0.9.zip` | 完整发布包（含使用说明、版本信息、依赖列表） | ~35 MB |

## 构建环境

- **操作系统**: `windows-latest` (Windows Server 2022)
- **Python**: 3.11
- **打包工具**: PyInstaller (onefile + windowed)
- **依赖**: 见 [requirements.txt](../requirements.txt)

## 手动本地打包（可选）

如果需要在本地 Windows 机器打包，双击运行：

```
打包成EXE.bat
```

会自动安装 PyInstaller、依赖，并生成 `release_v1.0.9\TidyUUUUp.exe`。
