#!/usr/bin/env python3

import os
import shutil
import subprocess
from pathlib import Path

USER_HOME = Path.home()
INSTALL_DIR = USER_HOME / ".arslang"
BIN_DIR = INSTALL_DIR / "bin"

PROJECT_ROOT = Path(__file__).parent.resolve()
PACKAGE_SRC = PROJECT_ROOT / "arslang"
BAT_SRC = PROJECT_ROOT / "windows" / "ars.bat"

def add_to_user_path(path_to_add):
    current_path = os.environ.get("PATH", "")

    if str(path_to_add).lower() in current_path.lower():
        print("PATH already contains ARSLang bin directory.")
        return True

    try:
        subprocess.run(
            ["setx", "PATH", f"%PATH%;{path_to_add}"],
            check=True,
            shell=True
        )
        print("PATH updated.")
        print("Restart Command Prompt or PowerShell before using ars.")
        return True
    except Exception as error:
        print(f"Error: Failed to update PATH automatically: {error}")
        print("")
        print("Manual fix:")
        print(f"Add this folder to your Windows User PATH:")
        print(path_to_add)
        return False

def main():
    if os.name != "nt":
        print("Error: This installer must be run on Windows.")
        print("Use install.py for Linux/macOS.")
        return

    if not PACKAGE_SRC.exists():
        print("Error: arslang package folder not found.")
        return

    if not BAT_SRC.exists():
        print("Error: windows/ars.bat not found.")
        return

    package_target = INSTALL_DIR / "arslang"

    if package_target.exists():
        shutil.rmtree(package_target)

    INSTALL_DIR.mkdir(parents=True, exist_ok=True)
    BIN_DIR.mkdir(parents=True, exist_ok=True)

    shutil.copytree(PACKAGE_SRC, package_target)
    shutil.copy2(BAT_SRC, BIN_DIR / "ars.bat")

    path_ok = add_to_user_path(BIN_DIR)

    print("")
    print("ARSLang files installed successfully for Windows!")

    if path_ok:
        print("Restart Command Prompt or PowerShell, then test:")
        print("ars version")
    else:
        print("After adding PATH manually, restart terminal and run:")
        print("ars version")

if __name__ == "__main__":
    main()
