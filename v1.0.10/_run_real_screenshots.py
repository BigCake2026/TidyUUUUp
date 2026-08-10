#!/usr/bin/env python3
"""
v1.0.8 真实 UI Mock 预览脚本（无桌面环境也能截图）
不执行实际的 DesktopWatcher / pynput / 托盘 / 系统 API
用假数据填充 file_index，完整渲染：
  - Dock 栏（含 3D 文件夹 + Liquid Glass + 发光分隔符）
  - 悬浮球 FloatingBall
  - 悬停在文件夹上弹出 DirectoryTreePopup 目录树
  - MainWindow 主界面（暗色主题）
"""
import os
import sys
import threading
import time
import random
import datetime

os.environ['QT_QPA_PLATFORM'] = 'xcb'

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtCore import (
    Qt, QTimer, QPoint, QRect, QRectF, QSize, QThread, pyqtSignal,
    QPropertyAnimation, QEasingCurve
)
from PyQt5.QtGui import (
    QIcon, QPixmap, QPainter, QColor, QFont, QLinearGradient, QPen, QBrush
)
from PyQt5.QtWidgets import QApplication, QSplashScreen

from ui.styles import apply_tidy_style
from ui.dock_bar import DockBar
from ui.main_window import MainWindow
from ui.floating_ball import FloatingBall
from ui.zone_panel import ZonePanel, ZoneFolderButton, DirectoryTreePopup
from ui.undo_panel import UndoPanel
from ui.quick_look import QuickLookPanel
from core.smart_engine import SmartRuleEngine
from core.updater import CURRENT_VERSION
from core.file_index import FileIndex


# ======================================================================
# Mock FileIndex：填充几千个假文件，让 Dock 的数量徽标、目录树真实显示
# ======================================================================
def mock_file_index():
    fi = FileIndex()
    fi._lock = threading.Lock()
    fi.index = {}

    fake_files = [
        # ===== 桌面 (100+) =====
        ("/home/user/Desktop/风景照.jpg",         "图片",  1200, "2026-08-01"),
        ("/home/user/Desktop/家庭合照.png",       "图片",  8600, "2026-08-05"),
        ("/home/user/Desktop/截图_20260807.png",   "图片",   540, "2026-08-07"),
        ("/home/user/Desktop/头像.png",           "图片",   180, "2026-07-20"),
        ("/home/user/Desktop/屏幕录制.mp4",        "视频", 95000, "2026-08-06"),
        ("/home/user/Desktop/旅行照片1.jpg",       "图片",  2400, "2026-07-25"),
        ("/home/user/Desktop/旅行照片2.jpg",       "图片",  2100, "2026-07-25"),
        ("/home/user/Desktop/猫咪.jpg",           "图片",  1100, "2026-07-15"),
        ("/home/user/Desktop/狗狗.png",           "图片",  1800, "2026-07-16"),
        ("/home/user/Desktop/毕业论文.docx",       "文档", 54000, "2026-08-02"),
        ("/home/user/Desktop/设计稿_v3.psd",       "设计",  87000, "2026-08-03"),
        ("/home/user/Desktop/source_code.zip",     "压缩包", 23000, "2026-08-06"),
        ("/home/user/Desktop/main.py",             "代码",    80, "2026-08-06"),
        ("/home/user/Desktop/ui_animations.py",    "代码",    56, "2026-08-05"),
        ("/home/user/Desktop/backup.7z",           "压缩包", 45000, "2026-07-28"),
        ("/home/user/Desktop/IMG_0098.HEIC",       "图片",  1800, "2026-08-01"),
        ("/home/user/Desktop/海报_最终版.png",      "图片",  3400, "2026-08-05"),
        ("/home/user/Desktop/会议记录.docx",       "文档",  1200, "2026-08-04"),
        ("/home/user/Desktop/财务报表.xlsx",       "文档",  2300, "2026-08-03"),
        ("/home/user/Desktop/TidyUUUUp_v1.0.8.zip","压缩包",   201, "2026-08-07"),
        ("/home/user/Desktop/song.flac",           "音频", 24000, "2026-07-30"),
        ("/home/user/Desktop/podcast.mp3",         "音频", 48000, "2026-07-28"),

        # ===== 下载 (200+) =====
        ("/home/user/Downloads/wallpaper_4k.jpg",    "图片",  3400, "2026-08-06"),
        ("/home/user/Downloads/wallpaper_mac.jpg",   "图片",  2100, "2026-08-06"),
        ("/home/user/Downloads/Photo_2026.png",      "图片",  1200, "2026-08-05"),
        ("/home/user/Downloads/iPhone备份.zip",      "压缩包", 89000, "2026-07-01"),
        ("/home/user/Downloads/Python-3.11.9.tgz",   "压缩包", 28000, "2026-08-01"),
        ("/home/user/Downloads/教材-算法导论.pdf",    "文档", 15000, "2026-07-15"),
        ("/home/user/Downloads/教材-机器学习.pdf",    "文档", 22000, "2026-07-18"),
        ("/home/user/Downloads/tensorflow.whl",      "代码", 640000, "2026-07-20"),
        ("/home/user/Downloads/VSCodeSetup.exe",     "可执行", 95000, "2026-08-02"),
        ("/home/user/Downloads/电影-沙丘2.mp4",      "视频", 1800000, "2026-08-01"),
        ("/home/user/Downloads/美剧-三体S02E01.mkv", "视频", 980000, "2026-08-07"),
        ("/home/user/Downloads/Train/01.jpg",        "图片",  3200, "2026-07-05"),
        ("/home/user/Downloads/Train/02.jpg",        "图片",  3100, "2026-07-05"),
        ("/home/user/Downloads/Train/03.jpg",        "图片",  2900, "2026-07-05"),
        ("/home/user/Downloads/music.m4a",           "音频", 32000, "2026-07-25"),
        ("/home/user/Downloads/project_final.zip",   "压缩包", 15000, "2026-08-04"),

        # ===== 文档 (500+) =====
        ("/home/user/Documents/工作/简历.docx",             "文档",  80, "2026-06-10"),
        ("/home/user/Documents/工作/合同范本.pdf",           "文档", 5200, "2026-07-12"),
        ("/home/user/Documents/工作/项目进度表.xlsx",        "文档",  420, "2026-08-05"),
        ("/home/user/Documents/工作/季度报告.pptx",          "文档", 12000, "2026-08-06"),
        ("/home/user/Documents/工作/代码规范.md",            "文档",   20, "2026-07-19"),
        ("/home/user/Documents/学习/数学笔记.txt",           "文档",   40, "2026-05-10"),
        ("/home/user/Documents/学习/Python基础.ipynb",       "代码",   80, "2026-06-18"),
        ("/home/user/Documents/学习/论文.tex",               "文档",  300, "2026-08-01"),
        ("/home/user/Documents/私人/日记.docx",              "文档",  200, "2026-07-10"),
        ("/home/user/Documents/私人/全家福.jpg",             "图片", 4500, "2026-02-15"),

        # ===== 图片 (60+) =====
        ("/home/user/Pictures/相册/2026春/a.jpg", "图片", 3400, "2026-03-15"),
        ("/home/user/Pictures/相册/2026春/b.jpg", "图片", 3200, "2026-03-15"),
        ("/home/user/Pictures/相册/2026夏/1.jpg", "图片", 4100, "2026-07-20"),
        ("/home/user/Pictures/相册/2026夏/2.jpg", "图片", 4300, "2026-07-20"),
        ("/home/user/Pictures/相册/2026夏/3.jpg", "图片", 3900, "2026-07-20"),
        ("/home/user/Pictures/相册/2026夏/4.jpg", "图片", 4000, "2026-07-20"),
        ("/home/user/Pictures/相册/2026夏/5.jpg", "图片", 3800, "2026-07-20"),
        ("/home/user/Pictures/Screenshots/shot1.png","图片",  800, "2026-08-06"),
        ("/home/user/Pictures/Screenshots/shot2.png","图片",  900, "2026-08-07"),
        ("/home/user/Pictures/Wallpapers/lake.heic","图片", 5200, "2026-05-03"),
        ("/home/user/Pictures/Wallpapers/space.jpg","图片", 6400, "2026-05-01"),
        ("/home/user/Pictures/Camera/photo.raw",    "图片", 32000, "2026-04-10"),

        # ===== 视频 (30+) =====
        ("/home/user/Videos/录制1.mp4",  "视频", 540000, "2026-07-01"),
        ("/home/user/Videos/录制2.mov",  "视频", 820000, "2026-07-10"),
        ("/home/user/Videos/电影.mp4",   "视频", 1800000, "2026-06-15"),
        ("/home/user/Videos/学习视频1.mp4","视频", 120000, "2026-05-12"),
        ("/home/user/Videos/学习视频2.mp4","视频", 140000, "2026-05-14"),

        # ===== 代码 (89+) =====
        ("/home/user/Projects/main.py",          "代码",  80, "2026-08-06"),
        ("/home/user/Projects/utils.py",         "代码",  30, "2026-08-05"),
        ("/home/user/Projects/requirements.txt", "代码",   1, "2026-08-04"),
        ("/home/user/Projects/index.js",         "代码",  40, "2026-08-02"),
        ("/home/user/Projects/App.tsx",          "代码",  60, "2026-07-28"),
        ("/home/user/Projects/Hello.cs",         "代码",  20, "2026-07-10"),
        ("/home/user/Projects/Program.java",     "代码",  35, "2026-06-30"),
        ("/home/user/Projects/README.md",        "文档",   5, "2026-08-01"),
        ("/home/user/Projects/lib.rs",           "代码",  45, "2026-07-25"),
        ("/home/user/Projects/game.go",          "代码",  30, "2026-07-22"),

        # ===== 音频 (45+) =====
        ("/home/user/Music/01.夜曲.mp3",      "音频", 4800, "2026-03-01"),
        ("/home/user/Music/02.稻香.flac",     "音频", 24000, "2026-03-02"),
        ("/home/user/Music/03.晴天.aac",      "音频", 3200, "2026-03-03"),
        ("/home/user/Music/playlist.m3u",     "文档",   1, "2026-04-01"),
        ("/home/user/Music/专辑/光盘映像.iso", "数据", 600000, "2026-05-01"),

        # ===== 压缩包 (12+) =====
        ("/home/user/Downloads/backup_full.tar.gz", "压缩包", 450000, "2026-07-01"),
        ("/home/user/Downloads/dataset.rar",        "压缩包", 230000, "2026-07-15"),
        ("/home/user/Documents/old_projects.zip",   "压缩包", 89000, "2026-01-10"),
        ("/home/user/Desktop/assets.tar",            "压缩包", 56000, "2026-07-05"),
    ]

    # 再加 600 条随机的小假文件，把总数撑到 ~1278
    categories = ["图片", "视频", "文档", "代码", "压缩包", "音频", "其他", "其他", "其他"]
    dirs = ["/home/user/Desktop/", "/home/user/Downloads/",
            "/home/user/Documents/", "/home/user/Pictures/",
            "/home/user/Music/", "/home/user/Videos/"]
    extensions = {"图片": [".jpg",".png",".heic"], "视频": [".mp4",".mkv",".mov"],
                  "文档": [".docx",".pdf",".xlsx"], "代码": [".py",".js",".ts",".rs"],
                  "压缩包": [".zip",".7z",".tar.gz"], "音频": [".mp3",".flac"],
                  "其他": [".tmp",".dat"]}
    for i in range(700):
        cat = random.choice(categories)
        ext = random.choice(extensions[cat])
        d = random.choice(dirs)
        name = f"random_file_{i:04d}{ext}"
        mod_ts = int(time.time()) - random.randint(1, 3600 * 24 * 60)
        mod_str = datetime.datetime.fromtimestamp(mod_ts).strftime("%Y-%m-%d")
        sz = random.randint(1, 5000)
        fake_files.append((d + name, cat, sz, mod_str))

    for (fp, zone, sz, md_str) in fake_files:
        try:
            md = time.mktime(datetime.datetime.strptime(md_str, "%Y-%m-%d").timetuple())
        except Exception:
            md = time.time()
        fi.index[fp] = {
            'name': os.path.basename(fp),
            'size': sz * 1024,
            'modified': md,
            'zone': zone,
        }

    print(f"[Mock] 填充假文件 {len(fi.index)} 条")
    return fi


# ======================================================================
# 主流程
# ======================================================================
def create_app_icon():
    pixmap = QPixmap(64, 64)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    gradient = QLinearGradient(0, 0, 64, 64)
    gradient.setColorAt(0, QColor(100, 150, 255))
    gradient.setColorAt(1, QColor(180, 100, 255))
    painter.setBrush(gradient)
    painter.setPen(Qt.NoPen)
    painter.drawRoundedRect(4, 4, 56, 56, 16, 16)
    painter.setPen(QColor(255, 255, 255, 230))
    font = QFont()
    font.setBold(True)
    font.setPointSize(28)
    painter.setFont(font)
    painter.drawText(pixmap.rect(), Qt.AlignCenter, "◇")
    painter.end()
    return QIcon(pixmap)


OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots_real")
os.makedirs(OUT_DIR, exist_ok=True)


def shot(name):
    """截取整个虚拟显示为 PNG"""
    import subprocess
    time.sleep(0.1)
    out = os.path.join(OUT_DIR, name)
    subprocess.run(["scrot", "-z", out], check=False)
    print(f"[截图] {out}")
    # 也用 Qt 的方式再保存每个 widget
    return out


def main():
    # 启动属性要在 QApplication 之前
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    app.setApplicationName("TidyUUUUp")
    app.setFont(QFont("Noto Sans CJK SC", 10))

    apply_tidy_style(app)
    icon = create_app_icon()
    app.setWindowIcon(icon)

    # ---- 屏幕几何（虚拟显示器 1280x800）----
    screen = app.primaryScreen().geometry()
    screen = QRect(0, 0, 1440, 900) if screen.width() < 100 else screen
    print(f"[屏幕] {screen.width()}x{screen.height()}")

    # ---- Mock 数据 ----
    smart_engine = SmartRuleEngine()
    file_index = mock_file_index()

    # ---- 组件 ----
    main_window = MainWindow()
    main_window.file_index = file_index  # 替换为 mock 索引

    dock = DockBar(screen)
    # Dock 需要几个假应用按钮
    default_apps = [
        ("文件",  "explorer"),
        ("浏览器", "chrome"),
        ("聊天",  "wechat"),
    ]
    for n, p in default_apps:
        dock.add_app(n, p)

    floating_ball = FloatingBall()
    undo_panel = UndoPanel.__new__(UndoPanel)  # 不初始化，避免依赖

    quick_look = QuickLookPanel()

    # ---- 智能分类文件夹按钮（真实 ZoneFolderButton）----
    zones = smart_engine.get_all_zones()
    tree_popup = DirectoryTreePopup()
    _zone_btns = []
    for zone_name, zone_config in zones.items():
        btn = ZoneFolderButton(zone_name, zone_config)
        _zone_btns.append(btn)
        dock.apps_layout.addWidget(btn)
        dock._all_items.append(btn)
    if hasattr(dock, '_magnify'):
        dock._magnify.items = dock._all_items

    # ---- 更新每个 Zone 的文件数量徽标 ----
    counts = {zn: 0 for zn in zones}
    for fp, info in file_index.index.items():
        z, _ = smart_engine.classify(fp)
        if z in counts:
            counts[z] += 1
    for b in _zone_btns:
        b.set_file_count(counts.get(b.zone_name, 0))
        print(f"  [Zone] {b.zone_name} → {counts.get(b.zone_name, 0)} 个文件")

    # ---- 显示所有主要窗口 ----
    # 把 Dock / 悬浮球 / MainWindow 都显示出来
    main_window.resize(960, 600)
    mw_x = (screen.width() - main_window.width()) // 2
    mw_y = 60
    main_window.move(mw_x, mw_y)
    main_window.setWindowOpacity(0.0)  # 先透明避免瞬间闪烁
    main_window.show()

    dock.move(screen.width() // 2 - dock.width() // 2,
              screen.height() - dock.height() - 20)
    dock.setWindowOpacity(0.0)
    dock.show()

    floating_ball.move(100, screen.height() // 2)
    floating_ball.setWindowOpacity(0.0)
    floating_ball.show()

    # 给 200ms 让所有 widget 布局，再淡入
    def step1_show():
        print("\n[阶段1] 淡入所有窗口，等 UI 稳定")
        dock.setWindowOpacity(1.0)
        floating_ball.setWindowOpacity(1.0)
        main_window.setWindowOpacity(0.98)
        # 让搜索框和分类计数显示一下
        try:
            main_window.toast.show_toast(f"✨ v{CURRENT_VERSION} 已加载 · 共整理 {len(file_index.index)} 个文件", 2800)
        except Exception:
            pass

    def step2_screenshot_main():
        print("\n[阶段2] 截图1：主界面 + Dock + 悬浮球整体")
        shot("01_main_window_with_dock.png")

    def step3_screenshot_dock():
        # 只把 Dock 栏放大展示在屏幕中央，然后截图
        print("\n[阶段3] 截图2：Dock 栏特写（居中）")
        # 隐藏主窗口、悬浮球
        main_window.hide()
        floating_ball.hide()
        dock.move(screen.width() // 2 - dock.width() // 2,
                  screen.height() // 2 - dock.height() // 2 - 80)
        QTimer.singleShot(400, lambda: shot("02_dock_closeup.png"))

    def step4_screenshot_tree():
        print("\n[阶段4] 截图3：悬停到『图片区域』文件夹，弹出 DirectoryTreePopup")
        try:
            # Zone 真实名是 "图片区域" 不是 "图片"
            img_btn = next((b for b in _zone_btns if b.zone_name == "图片区域"), None)
            if img_btn is None:
                # 找第一个 Zone 按钮兜底
                img_btn = _zone_btns[0] if _zone_btns else None
            if not img_btn:
                print("  ⚠️ 没找到图片区域按钮，跳过")
                QTimer.singleShot(200, step5_folder_states)
                return

            zone_name = img_btn.zone_name
            zone_config = zones.get(zone_name, {})
            print(f"  [Zone] 选中: {zone_name}")

            # 模拟"悬停" - 直接修改内部状态 + update()
            img_btn._hovered = True
            img_btn._pressed = False
            img_btn.update()

            # 收集该分类下的文件
            files = []
            for fp, info in file_index.index.items():
                classified_zone, _ = smart_engine.classify(fp)
                if classified_zone == zone_name:
                    files.append(dict(info, path=fp, name=os.path.basename(fp)))
            files.sort(key=lambda x: x.get('modified', 0), reverse=True)
            files = files[:80]
            print(f"  [Tree] {len(files)} 条文件 → populate")
            tree_popup.populate_from_files(files, zone_name,
                                            zone_config.get('icon', '🖼️'),
                                            zone_config.get('color', '#56B6FF'))

            # 锚点定位到 Dock 上按钮正上方
            img_btn.raise_()
            dock.raise_()
            anchor_global = dock.mapToGlobal(QPoint(img_btn.x() + img_btn.width() // 2, img_btn.y() + 5))
            tree_popup.show_above(anchor_global, offset_x=0)
            print(f"  [Tree] popup at {tree_popup.pos()}, size={tree_popup.size()}")

            # 等 popup 显示 + 淡入完成 600ms
            QTimer.singleShot(700, lambda: shot("03_dock_with_directory_tree.png"))
            QTimer.singleShot(1000, step5_folder_states)
        except Exception as e:
            import traceback
            print(f"  ❌ step4 异常: {e}")
            traceback.print_exc()
            QTimer.singleShot(300, step5_folder_states)

    def step5_folder_states():
        print("\n[阶段5] 截图4：文件夹图标三种状态 + 悬浮球")
        try:
            tree_popup.hide()
        except Exception:
            pass
        # 展示悬浮球特写
        floating_ball.show()
        floating_ball.move(screen.width() // 2 - floating_ball.width() // 2,
                           screen.height() // 2 - floating_ball.height() // 2 - 200)
        # 强制悬浮球进入 hover 状态（极简版：直接置 hover 标志 + 重绘）
        floating_ball._is_hovered = True
        floating_ball.update()
        time.sleep(0.02)

        # Dock 上依次展示 normal / hover / pressed；Zone 真实名带"区域"字样
        zone_real_names = [b.zone_name for b in _zone_btns[:3]] if _zone_btns else ["工作区域", "娱乐区域", "学习区域"]
        for zn, st in zip(zone_real_names, ["hover", "pressed", "normal"]):
            b = next((x for x in _zone_btns if x.zone_name == zn), None)
            if b:
                if st == "hover":
                    b._hovered = True; b._pressed = False
                elif st == "pressed":
                    b._hovered = False; b._pressed = True
                else:
                    b._hovered = False; b._pressed = False
                b.update()
        # 重新移动 Dock
        dock.move(screen.width() // 2 - dock.width() // 2,
                  screen.height() // 2 - dock.height() // 2 + 120)

        QTimer.singleShot(450, lambda: shot("04_floating_ball_and_folder_states.png"))
        QTimer.singleShot(800, step6_main)

    def step6_main():
        print("\n[阶段6] 截图5：主界面大图（Dock 放在正常位置）")
        floating_ball.hide()
        # 所有文件夹恢复正常
        for b in _zone_btns:
            b._hovered = False
            b._pressed = False
            b.update()
        # 主窗口显示
        main_window.resize(1120, 680)
        main_window.move((screen.width() - main_window.width()) // 2, 40)
        main_window.show()
        main_window.setWindowOpacity(1.0)
        main_window.raise_()
        main_window.activateWindow()
        dock.move(screen.width() // 2 - dock.width() // 2,
                  screen.height() - dock.height() - 30)
        dock.raise_()
        floating_ball.move(40, screen.height() // 2)
        floating_ball.show()
        floating_ball.setWindowOpacity(1.0)
        QTimer.singleShot(500, lambda: shot("05_full_app_desktop.png"))
        QTimer.singleShot(900, quit_app)

    def quit_app():
        print("\n[最终] 退出应用")
        app.quit()

    # 用 QTimer 串联所有步骤
    QTimer.singleShot(300, step1_show)
    QTimer.singleShot(1200, step2_screenshot_main)
    QTimer.singleShot(2400, step3_screenshot_dock)
    QTimer.singleShot(3800, step4_screenshot_tree)

    app.exec_()
    print(f"\n✅ 所有截图保存在: {OUT_DIR}")
    for f in sorted(os.listdir(OUT_DIR)):
        if f.endswith('.png'):
            sz = os.path.getsize(os.path.join(OUT_DIR, f))
            print(f"   📸 {f}  ({sz // 1024} KB)")


if __name__ == "__main__":
    main()
