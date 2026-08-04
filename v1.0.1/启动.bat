@echo off
chcp 65001 >nul
title TidyUUUUp v1.0.1
cd /d "%~dp0"
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo 请先安装 Python 3.8+
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)
python -c "import PyQt5" >nul 2>&1
if %errorlevel% neq 0 (
    echo 首次运行，正在安装依赖...
    python -m pip install -r requirements.txt
)
python main.py
