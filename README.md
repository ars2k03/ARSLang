<div align="center">

# 🔷 ARSLang

**A beginner-friendly, custom interpreted programming language — built with Python.**

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://github.com/ars2k03/ARSLang)
[![Language](https://img.shields.io/badge/built%20with-Python-3776AB?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![VS Code Extension](https://img.shields.io/badge/VS%20Code-Extension-blue?logo=visualstudiocode&logoColor=white)](https://marketplace.visualstudio.com/items?itemName=ars2k03.arslang)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)](CONTRIBUTING.md)

<br/>

> ARSLang is a lightweight, expressive programming language with its own syntax, CLI tool, interpreter, Windows installer, Linux/macOS installer, and VS Code ecosystem — all powered by Python.

</div>

---

## 📚 Table of Contents

- [What is ARSLang?](#-what-is-arslang)
- [Features](#-features)
- [Requirements](#-requirements)
- [Beginner Setup Guide](#-beginner-setup-guide)
  - [Windows Setup](#-windows-setup)
  - [Linux Setup](#-linux-setup)
  - [macOS Setup](#-macos-setup)
- [Windows PATH Fix](#️-windows-path-fix-if-ars-is-not-recognized)
- [VS Code Extension](#-vs-code-extension)
- [Getting Started](#-getting-started)
- [Syntax Guide](#-syntax-guide)
- [CLI Commands](#️-cli-commands)
- [Example Programs](#-example-programs)
- [Project Structure](#️-project-structure)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

# 🔷 What is ARSLang?

ARSLang is a custom interpreted programming language written from scratch in Python.

It is designed to be simple, readable, beginner-friendly, and easy to extend.

ARSLang includes:

- Custom `.ars` file format
- Dedicated `ars` command-line tool
- Built-in interpreter
- Linux/macOS installer
- Native Windows installer
- VS Code extension
- Syntax highlighting
- Smart autocomplete
- Error diagnostics
- Auto formatter
- Run button inside VS Code

Example:

```ars
void ars.prime(){
    ars.out("Hello, World!")
}
```

---

# ✨ Features

- ✅ Custom `.ars` file format
- ✅ Beginner-friendly syntax
- ✅ `ars.out()` output system
- ✅ Escape sequence support
- ✅ Single-line comments
- ✅ Multi-line comments
- ✅ Syntax validation
- ✅ Dedicated CLI tool
- ✅ Native Windows installer
- ✅ Linux/macOS installer
- ✅ VS Code extension
- ✅ Smart autocomplete
- ✅ Error diagnostics
- ✅ Auto formatting
- ✅ Run ARSLang button inside VS Code
- ✅ Lightweight architecture
- ✅ Zero external runtime dependencies

---

# 📋 Requirements

ARSLang needs:

- Python `3.6` or higher
- Git, if you want to clone the repository
- Windows, Linux, or macOS

Check Python version:

```bash
python --version
```

On some Linux/macOS systems:

```bash
python3 --version
```

Check Git version:

```bash
git --version
```

If Git is not installed, follow the setup guide below for your operating system.

---

# 🚀 Beginner Setup Guide

This section is for beginners who are installing ARSLang from zero.

---

## 🪟 Windows Setup

### Step 1 — Install Python

1. Go to the official Python website:

   👉 https://www.python.org/downloads/

2. Download Python for Windows.
3. During installation, make sure you check:

```txt
Add Python to PATH
```

4. Finish the installation.

Verify Python:

```powershell
python --version
```

Expected example:

```txt
Python 3.12.x
```

---

### Step 2 — Install Git

If this command does not work:

```powershell
git --version
```

Install Git from:

👉 https://git-scm.com/download/win

During installation, keep the default options. Make sure this option is selected:

```txt
Git from the command line and also from 3rd-party software
```

After installation, close PowerShell and open it again.

Verify Git:

```powershell
git --version
```

---

### Step 3 — Clone ARSLang

```powershell
git clone https://github.com/ars2k03/ARSLang.git
cd ARSLang
```

If Git is not installed and you do not want to install it, you can download the project manually:

1. Open the GitHub repository.
2. Click **Code**.
3. Click **Download ZIP**.
4. Extract the ZIP file.
5. Open the extracted folder in PowerShell.

---

### Step 4 — Install ARSLang on Windows

Inside the ARSLang folder, run:

```powershell
python install_windows.py
```

After installation, close PowerShell and open it again.

Verify:

```powershell
ars version
```

Expected output:

```txt
ARSLang v0.1.0
```

---


# ⚠️ Windows PATH Fix If `ars` Is Not Recognized

Sometimes Windows may install ARSLang successfully but fail to add it to PATH automatically.

You may see:

```txt
'ars' is not recognized as an internal or external command
```

or:

```txt
Failed to update PATH automatically
```

If this happens, manually add this folder to your Windows User PATH:

```txt
%USERPROFILE%\.arslang\bin
```

## Manual PATH Steps

1. Open Windows Search.
2. Search:

```txt
Environment Variables
```

3. Open:

```txt
Edit the system environment variables
```

4. Click:

```txt
Environment Variables
```

5. Under **User variables**, select:

```txt
Path
```

6. Click:

```txt
Edit
```

7. Click:

```txt
New
```

8. Add:

```txt
%USERPROFILE%\.arslang\bin
```

Example full path:

```txt
C:\Users\YourName\.arslang\bin
```

9. Click **OK** on all windows.
10. Restart PowerShell or Command Prompt.

Verify:

```powershell
ars version
```

---


## 🐧 Linux Setup

### Step 1 — Install Python and Git

For Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3 git -y
```

For Fedora:

```bash
sudo dnf install python3 git -y
```

For Arch Linux:

```bash
sudo pacman -S python git
```

Verify:

```bash
python3 --version
git --version
```

---

### Step 2 — Clone ARSLang

```bash
git clone https://github.com/ars2k03/ARSLang.git
cd ARSLang
```

---

### Step 3 — Install ARSLang on Linux

```bash
python3 install.py
source ~/.bashrc
```

If you use Zsh:

```bash
source ~/.zshrc
```

Verify:

```bash
ars version
```

Expected output:

```txt
ARSLang v0.1.0
```

---

## 🍎 macOS Setup

### Step 1 — Install Python and Git

macOS usually includes Git or asks you to install Command Line Tools automatically.

Check Git:

```bash
git --version
```

If Git is missing, install Apple Command Line Tools:

```bash
xcode-select --install
```

Check Python:

```bash
python3 --version
```

If Python is missing, install it from:

👉 https://www.python.org/downloads/macos/

Or install using Homebrew:

```bash
brew install python git
```

---

### Step 2 — Clone ARSLang

```bash
git clone https://github.com/ars2k03/ARSLang.git
cd ARSLang
```

---

### Step 3 — Install ARSLang on macOS

```bash
python3 install.py
source ~/.bashrc
```

If you use Zsh, which is the default shell on newer macOS versions:

```bash
source ~/.zshrc
```

Verify:

```bash
ars version
```

Expected output:

```txt
ARSLang v0.1.0
```

---

# 🧩 VS Code Extension

ARSLang has an official VS Code extension.

Install it from the Visual Studio Marketplace:

👉 [ARSLang VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ars2k03.arslang)

The extension includes:

- Syntax highlighting for `.ars` files
- Smart autocomplete
- Snippets
- Run ARSLang button
- Right-click Run ARSLang command
- Error diagnostics
- Format Document support

You can also search directly inside VS Code Extensions:

```txt
ARSLang
```

---

# 🏁 Getting Started

Create your first ARSLang program:

```bash
ars new hello.ars
```

Generated file:

```ars
void ars.prime(){
    ars.out("Hello ARSLang")
}
```

Run it:

```bash
ars run hello.ars
```

Output:

```txt
Hello ARSLang
```

---

# 📖 Syntax Guide

## Program Structure

Every ARSLang program must contain a `void ars.prime()` block.

```ars
void ars.prime(){

}
```

This is the entry point of the program.

---

## Output

Use `ars.out()` to print text to the terminal.

```ars
ars.out("Hello")
```

Example:

```ars
void ars.prime(){
    ars.out("Welcome to ARSLang")
}
```

Output:

```txt
Welcome to ARSLang
```

---

## Escape Sequences

ARSLang supports escape sequences inside strings.

| Sequence | Meaning |
|---|---|
| `\n` | New line |
| `\"` | Double quote |
| `\'` | Single quote |
| `\\` | Backslash |

Example:

```ars
void ars.prime(){
    ars.out("Line 1\nLine 2")
    ars.out("I'm \"Amit\"")
}
```

Output:

```txt
Line 1
Line 2
I'm "Amit"
```

---

## Comments

### Single-line comment

Use `##` for single-line comments.

```ars
## This is a comment
```

Example:

```ars
void ars.prime(){
    ## Print greeting
    ars.out("Hello")
}
```

---

### Multi-line comment

Use `**` to start and end a multi-line comment.

```ars
**
This is a
multi-line comment
**
```

Example:

```ars
void ars.prime(){
    **
    This line is ignored
    ars.out("This will not run")
    **

    ars.out("This will run")
}
```

---

# 🖥️ CLI Commands

| Command | Description |
|---|---|
| `ars new file.ars` | Create a new ARSLang file |
| `ars run file.ars` | Run an ARSLang program |
| `ars check file.ars` | Validate syntax without running |
| `ars version` | Show ARSLang version |
| `ars help` | Show help and syntax information |

Examples:

```bash
ars new myprogram.ars
ars check myprogram.ars
ars run myprogram.ars
ars version
ars help
```

---

# 💡 Example Programs

## Hello World

```ars
void ars.prime(){
    ars.out("Hello, World!")
}
```

---

## Multi-line Output

```ars
void ars.prime(){
    ars.out("Line 1\nLine 2\nLine 3")
}
```

---

## Quotes Inside Strings

```ars
void ars.prime(){
    ars.out("She said \"Hello!\"")
    ars.out("It\'s a beautiful day")
}
```

---

## Using Comments

```ars
void ars.prime(){

    ## Greeting
    ars.out("Good morning!")

    **
    Hidden code
    ars.out("This will not execute")
    **

    ars.out("Program finished")
}
```

---

# 🗂️ Project Structure

```txt
ARSLang/
├── arslang/
│   ├── __init__.py
│   └── cli.py
├── windows/
│   └── ars.bat
├── examples/
│   └── hello.ars
├── install.py
├── install_windows.py
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🛠️ Troubleshooting

## Problem: `git` is not recognized

You may see:

```txt
'git' is not recognized as an internal or external command
```

Fix:

1. Install Git from:

   👉 https://git-scm.com/download/win

2. Restart PowerShell or Command Prompt.
3. Run:

```powershell
git --version
```

---

## Problem: `python` is not recognized

You may see:

```txt
'python' is not recognized as an internal or external command
```

Fix:

1. Install Python from:

   👉 https://www.python.org/downloads/

2. During installation, enable:

```txt
Add Python to PATH
```

3. Restart PowerShell or Command Prompt.
4. Run:

```powershell
python --version
```

---

## Problem: `ars` is not recognized

Run:

```powershell
ars version
```

If it does not work, add this folder to your Windows User PATH:

```txt
%USERPROFILE%\.arslang\bin
```

Then restart PowerShell and try again:

```powershell
ars version
```

---

# 🤝 Contributing

Contributions are welcome.

Steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

Example:

```bash
git checkout -b feature/new-feature
git commit -m "Add new feature"
git push origin feature/new-feature
```

Found a bug?

Open an issue here:

👉 [ARSLang Issues](https://github.com/ars2k03/ARSLang/issues)

---

# 📄 License

This project is licensed under the MIT License.

```txt
Copyright (c) 2026 A R S

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction.
```

See the full license in the [LICENSE](LICENSE) file.

---

<div align="center">

Made with ❤️ by A R S

⭐ Star the repository if you find ARSLang interesting.

</div>
