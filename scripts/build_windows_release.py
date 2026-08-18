"""Build the TidyUUUUp Windows release.

Run this on Windows after installing the dependencies:
    python scripts/build_windows_release.py

The script packages v1.1.0 into a single EXE, copies the shortcut helper and
release notes, then creates a ZIP plus a SHA-256 checksum.  It never modifies
historical version directories.
"""
from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.1.0"
APP_DIR = ROOT / f"v{VERSION}"
ASSETS = APP_DIR / "assets"
BUILD_DIR = ROOT / "build"
DIST_DIR = ROOT / "dist"
RELEASE_DIR = ROOT / "release"
APP_NAME = "TidyUUUUp"


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=APP_DIR, check=True)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    if not sys.platform.startswith("win"):
        raise SystemExit("Windows EXE builds must run on Windows. Use the GitHub Actions workflow from Linux/macOS.")
    icon = ASSETS / "tidyuuuup_app_icon.ico"
    if not icon.is_file():
        raise FileNotFoundError(f"Missing application icon: {icon}")

    for directory in (BUILD_DIR, DIST_DIR, RELEASE_DIR):
        shutil.rmtree(directory, ignore_errors=True)

    separator = ";"
    run([
        sys.executable, "-m", "PyInstaller",
        "--noconfirm", "--clean", "--onefile", "--noconsole",
        "--name", APP_NAME,
        "--icon", str(icon),
        "--add-data", f"{icon}{separator}assets",
        "--add-data", f"{APP_DIR / 'create_shortcut.ps1'}{separator}.",
        "--distpath", str(DIST_DIR),
        "--workpath", str(BUILD_DIR / "work"),
        "--specpath", str(BUILD_DIR / "spec"),
        str(APP_DIR / "main.py"),
    ])

    executable = DIST_DIR / f"{APP_NAME}.exe"
    if not executable.is_file():
        raise RuntimeError(f"Expected EXE was not created: {executable}")

    package = RELEASE_DIR / f"{APP_NAME}_v{VERSION}"
    package.mkdir(parents=True, exist_ok=True)
    shutil.copy2(executable, package / executable.name)
    shutil.copy2(APP_DIR / "create_shortcut.ps1", package / "create_shortcut.ps1")
    shutil.copy2(APP_DIR / "README.md", package / "README.md")

    archive = RELEASE_DIR / f"{APP_NAME}_v{VERSION}_Windows.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
        for file in sorted(package.rglob("*")):
            if file.is_file():
                bundle.write(file, file.relative_to(RELEASE_DIR))

    checksum = RELEASE_DIR / f"{archive.name}.sha256"
    checksum.write_text(f"{sha256(archive)}  {archive.name}\n", encoding="utf-8")
    print(f"Built: {executable}")
    print(f"Release package: {archive}")
    print(f"Checksum: {checksum}")


if __name__ == "__main__":
    main()
