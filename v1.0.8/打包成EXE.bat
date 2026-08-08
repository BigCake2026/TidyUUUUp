@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

title = TidyUUUUp EXE 打包工具
color 0A

echo.
echo     ╔══════════════════════════════════════════╗
echo     ║                                          ║
echo     ║     📦  TidyUUUUp EXE 一键打包工具      ║
echo     ║                                          ║
echo     ║     将 Python 程序打包成单个 EXE         ║
echo     ║     不包含任何源码，保护你的代码         ║
echo     ║                                          ║
echo     ╚══════════════════════════════════════════╝
echo.

:: 获取脚本所在目录（即源码根目录）
set "SRC_DIR=%~dp0"
cd /d "%SRC_DIR%"

:: 检查 Python
echo     [1/6] 检查 Python 环境...
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo     [错误] 未检测到 Python！请先安装 Python 3.8+
    echo     下载地址: https://www.python.org/downloads/
    echo     安装时务必勾选 "Add Python to PATH"
    pause
    exit /b 1
)
for /f "tokens=2 delims= " %%a in ('python --version 2^>^&1') do set PY_VER=%%a
echo     ✅ Python %PY_VER%

:: 安装 PyInstaller
echo.
echo     [2/6] 安装打包工具 PyInstaller...
python -m pip install --upgrade pip >nul
python -m pip install pyinstaller
if %errorlevel% neq 0 (
    echo     [错误] PyInstaller 安装失败！请检查网络。
    pause
    exit /b 1
)
echo     ✅ PyInstaller 安装完成

:: 安装项目依赖
echo.
echo     [3/6] 安装项目依赖库...
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo     [警告] 部分依赖安装失败，尝试继续...
)

:: 读取版本号
for /f "tokens=2 delims=: " %%a in ('python -c "import json; d=json.load(open('version.json',encoding='utf-8')); print('VERSION:',d['version'])"') do set APP_VERSION=%%a
echo.
echo     [4/6] 开始打包 TidyUUUUp v%APP_VERSION% ...
echo.

:: 清理旧的构建
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

:: PyInstaller 打包参数
:: --onefile: 打包成单个EXE
:: --windowed: 不显示控制台窗口
:: --name: EXE文件名
:: --icon: 图标（可选）
:: --clean: 清理缓存
:: --noconfirm: 不询问覆盖

pyinstaller ^
    --onefile ^
    --windowed ^
    --name "TidyUUUUp" ^
    --icon "resources\app_icon.ico" ^
    --clean ^
    --noconfirm ^
    --add-data "version.json;." ^
    --add-data "resources;resources" ^
    --hidden-import PyQt5 ^
    --hidden-import watchdog ^
    --hidden-import pynput ^
    --hidden-import mss ^
    --hidden-import send2trash ^
    main.py

if %errorlevel% neq 0 (
    echo.
    echo     [错误] 打包失败！请检查上方错误信息。
    pause
    exit /b 1
)

echo.
echo     [5/6] 生成发布包...

:: 创建发布目录
set "RELEASE_DIR=release_v%APP_VERSION%"
if exist "%RELEASE_DIR%" rmdir /s /q "%RELEASE_DIR%"
mkdir "%RELEASE_DIR%"

:: 复制 EXE
copy "dist\TidyUUUUp.exe" "%RELEASE_DIR%\TidyUUUUp.exe" >nul

:: 复制必要的运行文件
copy "version.json" "%RELEASE_DIR%\version.json" >nul
copy "requirements.txt" "%RELEASE_DIR%\requirements.txt" >nul

:: 复制启动说明
(
    echo ========================================
    echo   TidyUUUUp v%APP_VERSION%
    echo ========================================
    echo.
    echo 使用方法：
    echo   1. 双击 TidyUUUUp.exe 即可运行
    echo   2. 首次运行可能需要几秒启动时间
    echo.
    echo 系统要求：
    echo   - Windows 7 / 8 / 10 / 11
    echo   - 无需安装 Python
    echo.
    echo 自动更新：
    echo   - 软件启动后会自动检查更新
    echo   - 右键托盘图标 -^> 检查更新 可手动检查
    echo.
) > "%RELEASE_DIR%\使用说明.txt"

:: 打包成 zip
set "ZIP_NAME=TidyUUUUp_v%APP_VERSION%.zip"
if exist "%ZIP_NAME%" del /f /q "%ZIP_NAME%"

:: 使用 PowerShell 压缩（Windows 自带）
powershell -Command "Compress-Archive -Path '%RELEASE_DIR%\*' -DestinationPath '%ZIP_NAME%' -Force"

if %errorlevel% neq 0 (
    echo     [警告] 压缩失败，请手动压缩 %RELEASE_DIR% 文件夹
) else (
    echo     ✅ 发布包已生成: %ZIP_NAME%
)

:: 清理临时文件
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist "TidyUUUUp.spec" del /f /q "TidyUUUUp.spec"

echo.
echo     ╔══════════════════════════════════════════╗
echo     ║                                          ║
echo     ║        🎉  打包完成！                    ║
echo     ║                                          ║
echo     ╚══════════════════════════════════════════╝
echo.
echo     EXE 文件:  %SRC_DIR%%RELEASE_DIR%\TidyUUUUp.exe
echo     发布包:    %SRC_DIR%%ZIP_NAME%
echo.
echo     生成的 EXE 不包含任何 Python 源码，完全加密！
echo.
pause
endlocal
