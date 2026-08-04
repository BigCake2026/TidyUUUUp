@echo off
chcp 65001 >nul
title TidyUUUUp - 智能工作台

:: 获取脚本所在目录
cd /d "%~dp0"

:: 检查 Python
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

:: 检查依赖是否安装
python -c "import PyQt5" >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [提示] 首次运行，正在安装依赖库...
    echo.
    python -m pip install --upgrade pip >nul
    python -m pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo.
        echo [错误] 依赖安装失败！请检查网络连接。
        pause
        exit /b 1
    )
)

:: 启动程序
python main.py
