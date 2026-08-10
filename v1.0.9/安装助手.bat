@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

title = TidyUUUUp 安装助手
color 0B

echo.
echo     ╔══════════════════════════════════════════╗
echo     ║                                          ║
echo     ║        ✨  TidyUUUUp  安装助手          ║
echo     ║                                          ║
echo     ║        Liquid Glass 智能工作台           ║
echo     ║                                          ║
echo     ╚══════════════════════════════════════════╝
echo.

:: 获取脚本所在目录
set "INSTALLER_DIR=%~dp0"
set "APP_DIR=%INSTALLER_DIR%TidyUUUUp"

:: 检查程序文件是否存在
if not exist "%APP_DIR%\main.py" (
    echo.
    echo     [错误] 找不到程序文件！请确保 TidyUUUUp 文件夹与此安装助手在同一目录。
    echo.
    pause
    exit /b 1
)

:: 选择安装目录
echo.
echo     请选择安装位置：
echo.
echo     [1] 当前目录（便携版，无需安装）
echo     [2] C:\Program Files\TidyUUUUp（推荐）
echo     [3] C:\Users\%username%\AppData\Local\TidyUUUUp
echo     [4] 自定义路径
echo.
set /p choice=     请输入选项 (1-4，默认2): 

if "%choice%"=="" set choice=2

if "%choice%"=="1" (
    set "TARGET_DIR=%INSTALLER_DIR:~0,-1%"
    goto :check_python
)

if "%choice%"=="2" (
    set "TARGET_DIR=C:\Program Files\TidyUUUUp"
    goto :check_python
)

if "%choice%"=="3" (
    set "TARGET_DIR=%LOCALAPPDATA%\TidyUUUUp"
    goto :check_python
)

if "%choice%"=="4" (
    echo.
    set /p TARGET_DIR=     请输入安装路径: 
    if "%TARGET_DIR%"=="" (
        echo     [错误] 路径不能为空！
        pause
        exit /b 1
    )
    goto :check_python
)

echo     [错误] 无效选项！
pause
exit /b 1

:check_python
echo.
echo     ────────────────────────────────────────────
echo.
echo     [1/5] 检查 Python 环境...
echo.

where python >nul 2>&1
if %errorlevel% neq 0 (
    echo     [警告] 未检测到 Python！
    echo.
    echo     TidyUUUUp 需要 Python 3.8 或更高版本才能运行。
    echo.
    echo     请先安装 Python：
    echo       1. 访问 https://www.python.org/downloads/
    echo       2. 下载并安装最新版 Python
    echo       3. 安装时务必勾选 "Add Python to PATH"
    echo       4. 安装完成后重新运行此安装助手
    echo.
    echo     是否现在打开 Python 下载页面？
    set /p open_py=     输入 y 打开，其他键跳过 (y/N): 
    if /i "%open_py%"=="y" (
        start https://www.python.org/downloads/
    )
    echo.
    pause
    exit /b 1
)

:: 检查Python版本
for /f "tokens=2 delims= " %%a in ('python --version 2^>^&1') do set PY_VER=%%a
echo     ✅ 检测到 Python %PY_VER%

:install_files
echo.
echo     [2/5] 复制程序文件到 "%TARGET_DIR%" ...
echo.

:: 创建目标目录
if exist "%TARGET_DIR%" (
    echo     目标目录已存在，将覆盖旧版本...
)

mkdir "%TARGET_DIR%" >nul 2>&1

:: 复制文件
xcopy "%APP_DIR%\*" "%TARGET_DIR%\" /E /I /Y /Q >nul

if %errorlevel% neq 0 (
    echo     [错误] 文件复制失败！请以管理员身份运行此安装助手。
    pause
    exit /b 1
)

echo     ✅ 文件复制完成

:install_deps
echo.
echo     [3/5] 安装依赖库（首次安装可能需要几分钟）...
echo.

cd /d "%TARGET_DIR%"
python -m pip install --upgrade pip >nul 2>&1
python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo     [警告] 部分依赖安装可能失败，请检查网络连接。
    echo     您也可以手动运行: pip install -r "%TARGET_DIR%\requirements.txt"
)

echo.
echo     ✅ 依赖安装完成

:create_shortcuts
echo.
echo     [4/5] 创建快捷方式...
echo.

:: 创建 VBS 脚本来生成快捷方式（避免依赖额外工具）
set "VBS_SCRIPT=%TEMP%\create_shortcuts.vbs"

echo Set WshShell = CreateObject("WScript.Shell") > "%VBS_SCRIPT%"
echo Set fso = CreateObject("Scripting.FileSystemObject") >> "%VBS_SCRIPT%"
echo. >> "%VBS_SCRIPT%"

:: 桌面快捷方式
echo strDesktop = WshShell.SpecialFolders("Desktop") >> "%VBS_SCRIPT%"
echo Set oShellLink = WshShell.CreateShortcut(strDesktop ^& "\TidyUUUUp.lnk") >> "%VBS_SCRIPT%"
echo oShellLink.TargetPath = "%TARGET_DIR%\启动.bat" >> "%VBS_SCRIPT%"
echo oShellLink.WorkingDirectory = "%TARGET_DIR%" >> "%VBS_SCRIPT%"
echo oShellLink.Description = "TidyUUUUp - 智能工作台" >> "%VBS_SCRIPT%"
echo oShellLink.Save >> "%VBS_SCRIPT%"

:: 开始菜单快捷方式
echo strStartMenu = WshShell.SpecialFolders("StartMenu") >> "%VBS_SCRIPT%"
echo If Not fso.FolderExists(strStartMenu ^& "\TidyUUUUp") Then >> "%VBS_SCRIPT%"
echo     fso.CreateFolder(strStartMenu ^& "\TidyUUUUp") >> "%VBS_SCRIPT%"
echo End If >> "%VBS_SCRIPT%"
echo Set oShellLink2 = WshShell.CreateShortcut(strStartMenu ^& "\TidyUUUUp\TidyUUUUp.lnk") >> "%VBS_SCRIPT%"
echo oShellLink2.TargetPath = "%TARGET_DIR%\启动.bat" >> "%VBS_SCRIPT%"
echo oShellLink2.WorkingDirectory = "%TARGET_DIR%" >> "%VBS_SCRIPT%"
echo oShellLink2.Description = "TidyUUUUp - 智能工作台" >> "%VBS_SCRIPT%"
echo oShellLink2.Save >> "%VBS_SCRIPT%"

cscript //nologo "%VBS_SCRIPT%" >nul 2>&1
del "%VBS_SCRIPT%" >nul 2>&1

echo     ✅ 桌面快捷方式已创建
echo     ✅ 开始菜单快捷方式已创建

:startup_option
echo.
echo     [5/5] 可选：开机自动启动
echo.
echo     是否让 TidyUUUUp 开机自动启动？
set /p auto_start=     输入 y 开启，其他键跳过 (y/N): 

if /i "%auto_start%"=="y" (
    set "VBS_SCRIPT2=%TEMP%\create_startup.vbs"
    echo Set WshShell = CreateObject("WScript.Shell") > "%VBS_SCRIPT2%"
    echo strStartup = WshShell.SpecialFolders("Startup") >> "%VBS_SCRIPT2%"
    echo Set oShellLink = WshShell.CreateShortcut(strStartup ^& "\TidyUUUUp.lnk") >> "%VBS_SCRIPT2%"
    echo oShellLink.TargetPath = "%TARGET_DIR%\启动.bat" >> "%VBS_SCRIPT2%"
    echo oShellLink.WorkingDirectory = "%TARGET_DIR%" >> "%VBS_SCRIPT2%"
    echo oShellLink.WindowStyle = 7 >> "%VBS_SCRIPT2%"
    echo oShellLink.Save >> "%VBS_SCRIPT2%"
    cscript //nologo "%VBS_SCRIPT2%" >nul 2>&1
    del "%VBS_SCRIPT2%" >nul 2>&1
    echo     ✅ 已添加到开机启动
)

:done
echo.
echo     ╔══════════════════════════════════════════╗
echo     ║                                          ║
echo     ║        🎉  TidyUUUUp 安装完成！         ║
echo     ║                                          ║
echo     ╚══════════════════════════════════════════╝
echo.
echo     安装位置: %TARGET_DIR%
echo.
echo     启动方式:
echo       - 双击桌面 "TidyUUUUp" 快捷方式
echo       - 开始菜单 → TidyUUUUp → TidyUUUUp
echo       - 或直接运行: "%TARGET_DIR%\启动.bat"
echo.
echo     是否现在启动 TidyUUUUp？
set /p launch=     输入 y 启动，其他键退出 (y/N): 

if /i "%launch%"=="y" (
    start "" "%TARGET_DIR%\启动.bat"
)

endlocal
