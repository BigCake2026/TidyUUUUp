@echo off
chcp 65001 >nul

:: 便携模式启动（无需安装，直接运行）
echo.
echo     ✨  TidyUUUUp 便携版启动中...
echo.

cd /d "%~dp0TidyUUUUp"

where python >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [错误] 未检测到 Python！
    echo.
    echo 请先安装 Python 3.8 或更高版本：
    echo   1. 访问 https://www.python.org/downloads/
    echo   2. 下载并安装最新版 Python
    echo   3. 安装时务必勾选 "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

python -c "import PyQt5" >nul 2>&1
if %errorlevel% neq 0 (
    echo [提示] 首次运行，正在安装依赖库...
    python -m pip install --upgrade pip >nul
    python -m pip install -r requirements.txt
)

python main.py
