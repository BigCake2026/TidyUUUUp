"""
生成 TidyUUUUp 程序图标
生成 .ico 格式（包含多种尺寸：16, 32, 48, 64, 128, 256）
"""
from PIL import Image, ImageDraw, ImageFont
import os


def generate_icon(output_path, size=512):
    """生成 TidyUUUUp 风格的图标"""
    # 创建正方形画布
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 圆角半径（20% 的圆角，类似 iOS 图标）
    radius = int(size * 0.22)

    # 绘制圆角矩形背景（白色）
    draw.rounded_rectangle(
        [(0, 0), (size, size)],
        radius=radius,
        fill=(255, 255, 255, 255)
    )

    # 绘制文字 "Tidy"（深蓝色）
    try:
        # 尝试加载系统字体
        font_large = ImageFont.truetype("arialbd.ttf", int(size * 0.22))
        font_small = ImageFont.truetype("arialbd.ttf", int(size * 0.22))
    except Exception:
        try:
            font_large = ImageFont.truetype("DejaVuSans-Bold.ttf", int(size * 0.22))
            font_small = ImageFont.truetype("DejaVuSans-Bold.ttf", int(size * 0.22))
        except Exception:
            font_large = ImageFont.load_default()
            font_small = ImageFont.load_default()

    # 颜色定义
    dark_blue = (26, 35, 59, 255)  # #1a233b 深蓝色（Tidy的颜色）
    bright_blue = (41, 98, 255, 255)  # #2962ff 亮蓝色（UUUp的颜色）

    # 计算文字位置（居中偏上）
    tidy_text = "Tidy"
    uuup_text = "UUUp"

    # 获取文字尺寸
    try:
        tidy_bbox = draw.textbbox((0, 0), tidy_text, font=font_large)
        tidy_width = tidy_bbox[2] - tidy_bbox[0]
        tidy_height = tidy_bbox[3] - tidy_bbox[1]

        uuup_bbox = draw.textbbox((0, 0), uuup_text, font=font_small)
        uuup_width = uuup_bbox[2] - uuup_bbox[0]
        uuup_height = uuup_bbox[3] - uuup_bbox[1]
    except Exception:
        tidy_width = size * 0.5
        tidy_height = size * 0.18
        uuup_width = size * 0.5
        uuup_height = size * 0.18

    # 两行文字的总高度
    total_height = tidy_height + uuup_height + size * 0.05

    # 起始Y位置（垂直居中）
    start_y = (size - total_height) / 2

    # 绘制 "Tidy"
    tidy_x = (size - tidy_width) / 2
    tidy_y = start_y
    draw.text((tidy_x, tidy_y), tidy_text, fill=dark_blue, font=font_large)

    # 绘制 "UUUp"
    uuup_x = (size - uuup_width) / 2
    uuup_y = start_y + tidy_height + size * 0.05
    draw.text((uuup_x, uuup_y), uuup_text, fill=bright_blue, font=font_small)

    return img


def save_as_ico(img, output_path):
    """保存为 .ico 格式（包含多种尺寸）"""
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    icons = []
    for s in sizes:
        resized = img.resize(s, Image.LANCZOS)
        icons.append(resized)
    icons[0].save(output_path, format='ICO', sizes=sizes)


if __name__ == '__main__':
    # 生成输出目录
    output_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(output_dir, exist_ok=True)

    # 生成 512x512 图标
    icon = generate_icon(output_dir, 512)

    # 保存为 PNG（用于预览）
    png_path = os.path.join(output_dir, 'app_icon.png')
    icon.save(png_path, 'PNG')
    print(f"PNG 图标已保存: {png_path}")

    # 保存为 ICO
    ico_path = os.path.join(output_dir, 'app_icon.ico')
    save_as_ico(icon, ico_path)
    print(f"ICO 图标已保存: {ico_path}")

    print("完成！")
