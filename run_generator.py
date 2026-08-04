"""
卖家启动脚本 - 双击即可打开激活码生成器
"""
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)
os.chdir(script_dir)

try:
    from PyQt5.QtWidgets import QApplication
    from code_generator import CodeGeneratorApp, create_icon

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = CodeGeneratorApp()
    window.setWindowIcon(create_icon())
    window.show()
    sys.exit(app.exec_())

except ImportError as e:
    print(f"缺少依赖: {e}")
    print("正在安装依赖...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("依赖安装完成，请重新运行本脚本")
    input("按回车退出...")
except Exception as e:
    print(f"启动失败: {e}")
    import traceback
    traceback.print_exc()
    input("按回车退出...")
