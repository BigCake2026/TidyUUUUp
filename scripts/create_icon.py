"""Create the multi-resolution Windows icon used by TidyUUUUp builds.

Run from the repository root:
    python scripts/create_icon.py
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "v1.1.1" / "assets" / "tidyuuuup_app_icon.png"
DESTINATION = ROOT / "v1.1.1" / "assets" / "tidyuuuup_app_icon.ico"
SIZES = (16, 20, 24, 32, 40, 48, 64, 128, 256)


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Missing source icon: {SOURCE}")
    image = Image.open(SOURCE).convert("RGBA")
    image.save(DESTINATION, format="ICO", sizes=[(size, size) for size in SIZES])
    print(f"Created {DESTINATION} with sizes: {', '.join(map(str, SIZES))}")


if __name__ == "__main__":
    main()
