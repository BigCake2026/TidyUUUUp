"""Build the TidyUUUUp v2.0.0 Windows application and one-click installer.

Run only on Windows after PyInstaller and Inno Setup have been installed:
    python scripts/build_windows_release.py

The output release contains one user-facing setup executable plus its SHA-256
file.  The installer writes the app to the current user's local app directory
and creates branded desktop and Start menu shortcuts.
"""
from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "2.0.0"
APP_DIR = ROOT / f"v{VERSION}"
ASSETS = APP_DIR / "assets"
BUILD_DIR = ROOT / "build"
DIST_DIR = ROOT / "dist"
RELEASE_DIR = ROOT / "release"
APP_NAME = "TidyUUUUp"
INSTALLER_NAME = f"{APP_NAME}_Setup_v{VERSION}.exe"


def run(command: list[str], cwd: Path = APP_DIR) -> None:
    subprocess.run(command, cwd=cwd, check=True)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def find_inno_compiler() -> str:
    for candidate in ("iscc", "ISCC.exe"):
        resolved = shutil.which(candidate)
        if resolved:
            return resolved
    raise RuntimeError(
        "Inno Setup compiler was not found. Install Inno Setup 6 or run the GitHub Actions Windows workflow."
    )


def main() -> None:
    if not sys.platform.startswith("win"):
        raise SystemExit("Windows installer builds must run on Windows. Use the GitHub Actions workflow from Linux/macOS.")
    icon = ASSETS / "tidyuuuup_app_icon.ico"
    installer_script = APP_DIR / "installer.iss"
    if not icon.is_file():
        raise FileNotFoundError(f"Missing application icon: {icon}")
    if not installer_script.is_file():
        raise FileNotFoundError(f"Missing installer script: {installer_script}")

    for directory in (BUILD_DIR, DIST_DIR, RELEASE_DIR):
        shutil.rmtree(directory, ignore_errors=True)
    RELEASE_DIR.mkdir(parents=True, exist_ok=True)

    run([
        sys.executable, "-m", "PyInstaller",
        "--noconfirm", "--clean", "--onefile", "--noconsole",
        "--name", APP_NAME,
        "--icon", str(icon),
        "--add-data", f"{icon};assets",
        "--add-data", f"{APP_DIR / 'create_shortcut.ps1'};.",
        "--distpath", str(DIST_DIR),
        "--workpath", str(BUILD_DIR / "work"),
        "--specpath", str(BUILD_DIR / "spec"),
        str(APP_DIR / "main.py"),
    ])

    portable_exe = DIST_DIR / f"{APP_NAME}.exe"
    if not portable_exe.is_file():
        raise RuntimeError(f"Expected application EXE was not created: {portable_exe}")

    run([find_inno_compiler(), str(installer_script)], cwd=APP_DIR)
    installer = RELEASE_DIR / INSTALLER_NAME
    if not installer.is_file():
        raise RuntimeError(f"Expected installer was not created: {installer}")

    checksum = RELEASE_DIR / f"{installer.name}.sha256"
    checksum.write_text(f"{sha256(installer)}  {installer.name}\n", encoding="utf-8")
    print(f"Built portable application: {portable_exe}")
    print(f"Built one-click installer: {installer}")
    print(f"Checksum: {checksum}")


if __name__ == "__main__":
    main()
