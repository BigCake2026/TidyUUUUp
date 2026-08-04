@echo off
chcp 65001 >nul
echo ============================================
echo   TidyUUUUp - 智能工作台
echo   Liquid Glass 设计
echo ============================================
echo.

cd /d "%~dp0"

echo [1/3] 检查Python环境...
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请先安装Python 3.8+
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo ✓ Python已就绪

echo.
echo [2/3] 安装依赖...
pip install -r requirements.txt -q
if errorlevel 1 (
    echo 依赖安装失败，请检查网络连接
    pause
    exit /b 1
)
echo ✓ 依赖已就绪

echo.
echo [3/3] 启动 TidyUUUUp...
python main.py

pause
