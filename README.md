<div align="center">

# 🔷 ARSLang

**A beginner-friendly custom interpreted programming language — built with Python.**

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
- Windows installer
- Linux/macOS installer
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
- ✅ Windows installer
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

ARSLang needs only these tools:

- Python `3.6` or higher
- Git, optional but recommended
- VS Code, optional but recommended

Check Python:

```bash
python --version
```

If that does not work, try:

```bash
python3 --version
```

Check Git:

```bash
git --version
```

If Git is not installed, follow the setup guide below for your operating system.

---

# 🚀 Beginner Setup Guide

This section starts from zero. Follow the guide for your operating system.

---

## 🪟 Windows Setup

### Step 1 — Install Python

1. Go to the official Python website: https://www.python.org/downloads/
2. Download Python for Windows.
3. Run the installer.
4. Important: select this checkbox before installing:

```txt
Add Python to PATH
```

5. Finish installation.
6. Close and reopen Command Prompt or PowerShell.

Verify Python:

```powershell
python --version
```

Expected example:

```txt
Python 3.12.x
```

If `python` is not recognized, reinstall Python and make sure `Add Python to PATH` is selected.

---

### Step 2 — Install Git

Git is required if you want to use `git clone`.

1. Go to: https://git-scm.com/download/win
2. Download Git for Windows.
3. Run the installer.
4. During installation, choose this option:

```txt
Git from the command line and also from 3rd-party software
```

5. Finish installation.
6. Close and reopen PowerShell.

Verify Git:

```powershell
git --version
```

Expected example:

```txt
git version 2.x.x
```

---

### Step 3 — Download ARSLang

Recommended method:

```powershell
git clone https://github.com/ars2k03/ARSLang.git
cd ARSLang
```

If Git is not installed, use ZIP download instead:

1. Open the repository: https://github.com/ars2k03/ARSLang
2. Click **Code**.
3. Click **Download ZIP**.
4. Extract the ZIP file.
5. Open the extracted `ARSLang` folder.
6. Open PowerShell inside that folder.

---

### Step 4 — Install ARSLang on Windows

Run:

```powershell
python install_windows.py
```

After installation, close and reopen PowerShell.

Verify:

```powershell
ars version
```

Expected output:

```txt
ARSLang v0.1.0
```

---

### Step 5 — Run your first ARSLang file

Create a new file:

```powershell
ars new hello.ars
```

Run it:

```powershell
ars run hello.ars
```

---

## 🐧 Linux Setup

### Step 1 — Install Python and Git

For Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3 python3-pip git -y
```

For Fedora:

```bash
sudo dnf install python3 python3-pip git -y
```

For Arch Linux:

```bash
sudo pacman -S python python-pip git
```

Verify:

```bash
python3 --version
git --version
```

---

### Step 2 — Download ARSLang

```bash
git clone https://github.com/ars2k03/ARSLang.git
cd ARSLang
```

If Git is not installed, download the ZIP from GitHub and extract it.

---

### Step 3 — Install ARSLang on Linux

```bash
python3 install.py
```

Reload your terminal configuration:

```bash
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

### Step 4 — Run your first ARSLang file

```bash
ars new hello.ars
ars run hello.ars
```

---

## 🍎 macOS Setup

### Step 1 — Install Homebrew, if needed

Check if Homebrew exists:

```bash
brew --version
```

If it is not installed, install it from:

```txt
https://brew.sh
```

---

### Step 2 — Install Python and Git

```bash
brew install python git
```

Verify:

```bash
python3 --version
git --version
```

---

### Step 3 — Download ARSLang

```bash
git clone https://github.com/ars2k03/ARSLang.git
cd ARSLang
```

If Git is not installed, download the ZIP from GitHub and extract it.

---

### Step 4 — Install ARSLang on macOS

```bash
python3 install.py
```

Reload your terminal configuration:

```bash
source ~/.zshrc
```

If you use Bash:

```bash
source ~/.bashrc
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

### Step 5 — Run your first ARSLang file

```bash
ars new hello.ars
ars run hello.ars
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

# 🛠 Troubleshooting

## `git` is not recognized on Windows

Problem:

```txt
git is not recognized as a name of a cmdlet, function, script file, or executable program
```

Fix:

1. Install Git from: https://git-scm.com/download/win
2. During setup, choose:

```txt
Git from the command line and also from 3rd-party software
```

3. Close and reopen PowerShell.
4. Run:

```powershell
git --version
```

---

## `python` is not recognized on Windows

Fix:

1. Reinstall Python from: https://www.python.org/downloads/
2. Select:

```txt
Add Python to PATH
```

3. Close and reopen PowerShell.
4. Run:

```powershell
python --version
```

---

## `ars` is not recognized after installation

### Windows fix

Manually add this folder to your Windows User PATH:

```txt
%USERPROFILE%\.arslang\bin
```

Then close and reopen PowerShell.

Verify:

```powershell
ars version
```

### Linux/macOS fix

Reload your shell:

```bash
source ~/.bashrc
```

Or:

```bash
source ~/.zshrc
```

Then verify:

```bash
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
git add .
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
