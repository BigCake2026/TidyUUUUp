"""
系统集成模块：桌面快捷方式、开机自启
适用于 Windows 系统
"""

import os
import sys
import platform


def is_windows():
    """判断是否为 Windows 系统"""
    return platform.system() == 'Windows'


def get_app_path():
    """获取当前程序的路径"""
    if getattr(sys, 'frozen', False):
        # PyInstaller 打包后的 exe
        return sys.executable
    else:
        # 开发模式
        return os.path.abspath(sys.argv[0])


def get_app_dir():
    """获取程序所在目录"""
    return os.path.dirname(get_app_path())


def get_desktop_path():
    """获取桌面路径"""
    if is_windows():
        try:
            import winreg
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
            )
            desktop, _ = winreg.QueryValueEx(key, "Desktop")
            winreg.CloseKey(key)
            return os.path.expandvars(desktop)
        except Exception:
            pass
    return os.path.join(os.path.expanduser('~'), 'Desktop')


def get_startup_folder_path():
    """获取 Windows 启动文件夹路径"""
    if is_windows():
        try:
            import winreg
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
            )
            startup, _ = winreg.QueryValueEx(key, "Startup")
            winreg.CloseKey(key)
            return os.path.expandvars(startup)
        except Exception:
            pass
    return os.path.join(
        os.path.expanduser('~'),
        'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup'
    )


def create_shortcut(target_path, shortcut_path, working_dir=None, icon_path=None, description=""):
    """
    创建 Windows 快捷方式 (.lnk)
    
    Args:
        target_path: 目标程序路径
        shortcut_path: 快捷方式保存路径 (.lnk)
        working_dir: 工作目录
        icon_path: 图标路径 (.ico)
        description: 描述
    
    Returns:
        bool: 是否成功
    """
    if not is_windows():
        print("非 Windows 系统，跳过快捷方式创建")
        return False

    try:
        import pythoncom
        from win32com.shell import shell, shellcon

        shortcut = pythoncom.CoCreateInstance(
            shell.CLSID_ShellLink,
            None,
            pythoncom.CLSCTX_INPROC_SERVER,
            shell.IID_IShellLink
        )

        shortcut.SetPath(target_path)

        if working_dir:
            shortcut.SetWorkingDirectory(working_dir)

        if icon_path:
            shortcut.SetIconLocation(icon_path, 0)

        if description:
            shortcut.SetDescription(description)

        # 保存为 .lnk
        persist_file = shortcut.QueryInterface(pythoncom.IID_IPersistFile)
        persist_file.Save(shortcut_path, 0)

        print(f"快捷方式已创建: {shortcut_path}")
        return True

    except ImportError:
        # 如果没有 pywin32，使用 PowerShell
        return _create_shortcut_powershell(target_path, shortcut_path, working_dir, icon_path, description)
    except Exception as e:
        print(f"创建快捷方式失败 (COM): {e}")
        return _create_shortcut_powershell(target_path, shortcut_path, working_dir, icon_path, description)


def _create_shortcut_powershell(target_path, shortcut_path, working_dir=None, icon_path=None, description=""):
    """使用 PowerShell 创建快捷方式"""
    try:
        import subprocess

        ps_script = f"""
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("{shortcut_path}")
$Shortcut.TargetPath = "{target_path}"
"""
        if working_dir:
            ps_script += f'$Shortcut.WorkingDirectory = "{working_dir}"\n'

        if icon_path:
            ps_script += f'$Shortcut.IconLocation = "{icon_path},0"\n'

        if description:
            ps_script += f'$Shortcut.Description = "{description}"\n'

        ps_script += "$Shortcut.Save()\n"

        result = subprocess.run(
            ['powershell', '-Command', ps_script],
            capture_output=True, text=True
        )

        if result.returncode == 0:
            print(f"快捷方式已创建 (PowerShell): {shortcut_path}")
            return True
        else:
            print(f"PowerShell 创建快捷方式失败: {result.stderr}")
            return False

    except Exception as e:
        print(f"PowerShell 创建快捷方式异常: {e}")
        return False


def create_desktop_shortcut(icon_path=None):
    """在桌面创建 TidyUUUUp 快捷方式"""
    app_path = get_app_path()
    desktop = get_desktop_path()
    shortcut_path = os.path.join(desktop, "TidyUUUUp.lnk")
    working_dir = get_app_dir()

    if icon_path is None:
        # 尝试在程序目录下找图标
        default_icon = os.path.join(get_app_dir(), 'resources', 'app_icon.ico')
        if os.path.exists(default_icon):
            icon_path = default_icon

    return create_shortcut(
        target_path=app_path,
        shortcut_path=shortcut_path,
        working_dir=working_dir,
        icon_path=icon_path,
        description="TidyUUUUp - 智能桌面整理工具"
    )


def is_desktop_shortcut_exists():
    """检查桌面快捷方式是否已存在"""
    shortcut_path = os.path.join(get_desktop_path(), "TidyUUUUp.lnk")
    return os.path.exists(shortcut_path)


def remove_desktop_shortcut():
    """删除桌面快捷方式"""
    shortcut_path = os.path.join(get_desktop_path(), "TidyUUUUp.lnk")
    if os.path.exists(shortcut_path):
        os.remove(shortcut_path)
        print(f"桌面快捷方式已删除")
        return True
    return False


def enable_autostart(icon_path=None):
    """
    启用开机自启
    
    方法：在启动文件夹创建快捷方式
    """
    app_path = get_app_path()
    startup_folder = get_startup_folder_path()
    shortcut_path = os.path.join(startup_folder, "TidyUUUUp.lnk")
    working_dir = get_app_dir()

    if icon_path is None:
        default_icon = os.path.join(get_app_dir(), 'resources', 'app_icon.ico')
        if os.path.exists(default_icon):
            icon_path = default_icon

    os.makedirs(startup_folder, exist_ok=True)

    return create_shortcut(
        target_path=app_path,
        shortcut_path=shortcut_path,
        working_dir=working_dir,
        icon_path=icon_path,
        description="TidyUUUUp - 开机自启"
    )


def disable_autostart():
    """禁用开机自启"""
    startup_folder = get_startup_folder_path()
    shortcut_path = os.path.join(startup_folder, "TidyUUUUp.lnk")
    if os.path.exists(shortcut_path):
        os.remove(shortcut_path)
        print(f"开机自启已禁用")
        return True
    return False


def is_autostart_enabled():
    """检查是否已启用开机自启"""
    startup_folder = get_startup_folder_path()
    shortcut_path = os.path.join(startup_folder, "TidyUUUUp.lnk")
    return os.path.exists(shortcut_path)


def run_first_time_setup():
    """首次运行安装：创建桌面快捷方式 + 询问是否开机自启"""
    print("正在执行首次安装设置...")

    # 创建桌面快捷方式
    desktop_ok = create_desktop_shortcut()
    if desktop_ok:
        print("✓ 桌面快捷方式已创建")
    else:
        print("⚠ 桌面快捷方式创建失败（非 Windows 或权限不足）")

    return desktop_ok
