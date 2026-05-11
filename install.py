#!/usr/bin/env python3

import os
import shutil
import stat
from pathlib import Path

HOME = Path.home()
INSTALL_DIR = HOME / ".arslang"
BIN_DIR = HOME / ".local" / "bin"
TARGET = BIN_DIR / "ars"

PROJECT_ROOT = Path(__file__).parent.resolve()
PACKAGE_SRC = PROJECT_ROOT / "arslang"

LAUNCHER = f"""#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".arslang"))

from arslang.cli import main

if __name__ == "__main__":
    main()
"""

def main():
    if not PACKAGE_SRC.exists():
        print("Error: arslang package folder not found.")
        return

    BIN_DIR.mkdir(parents=True, exist_ok=True)
    INSTALL_DIR.mkdir(parents=True, exist_ok=True)

    package_target = INSTALL_DIR / "arslang"

    if package_target.exists():
        shutil.rmtree(package_target)

    shutil.copytree(PACKAGE_SRC, package_target)

    with open(TARGET, "w") as f:
        f.write(LAUNCHER)

    st = os.stat(TARGET)
    os.chmod(TARGET, st.st_mode | stat.S_IEXEC)

    bashrc = HOME / ".bashrc"
    export_line = 'export PATH="$HOME/.local/bin:$PATH"'

    if bashrc.exists():
        content = bashrc.read_text()
        if export_line not in content:
            with open(bashrc, "a") as f:
                f.write(f"\n{export_line}\n")

    print("ARSLang installed successfully!")
    print("Run:")
    print("source ~/.bashrc")
    print("ars version")

if __name__ == "__main__":
    main()
