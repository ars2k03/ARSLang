<div align="center">

# 🔷 ARSLang

**A beginner-friendly, custom interpreted programming language — built with Python.**

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://github.com/ars2k03/ARSLang)
[![Language](https://img.shields.io/badge/built%20with-Python-3776AB?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)](CONTRIBUTING.md)

<br/>

> ARSLang is a lightweight, expressive programming language with its own syntax, CLI tool, interpreter, and VS Code ecosystem — all powered by Python.

</div>

---

## 📚 Table of Contents

- [What is ARSLang?](#-what-is-arslang)
- [Features](#-features)
- [Requirements](#-requirements)
- [Windows Support](#️-windows-support)
- [Installation](#-installation)
- [VS Code Extension](#-vs-code-extension)
- [Getting Started](#-getting-started)
- [Syntax Guide](#-syntax-guide)
- [CLI Commands](#️-cli-commands)
- [Example Programs](#-example-programs)
- [Project Structure](#️-project-structure)
- [Roadmap](#️-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

# 🔷 What is ARSLang?

ARSLang is a custom interpreted programming language written from scratch in Python.

It includes:

- Custom `.ars` file format
- Dedicated `ars` CLI
- Built-in interpreter
- VS Code extension
- Syntax highlighting
- Diagnostics
- Formatter
- Autocomplete

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
- ✅ Comments support
- ✅ Syntax validation
- ✅ Dedicated CLI tool
- ✅ VS Code extension
- ✅ Smart autocomplete
- ✅ Error diagnostics
- ✅ Auto formatting
- ✅ Run button inside VS Code
- ✅ Native Windows installer
- ✅ Lightweight architecture

---

# 📋 Requirements

- Python `3.6` or higher
- Linux
- macOS
- Windows

Check Python version:

```bash
python --version
```

---

# ⚠️ Windows Support

ARSLang now includes a native Windows installer.

Windows users can install ARSLang with:

```bash
python install_windows.py
```

After installation, restart Command Prompt or PowerShell, then run:

```bash
ars version
```

If `ars` is not recognized, manually add this folder to your Windows User PATH:

```txt
%USERPROFILE%\.arslang\bin
```

---

# 🚀 Installation

## Step 1 — Clone the repository

```bash
git clone https://github.com/ars2k03/ARSLang.git
cd ARSLang
```

---

## Step 2 — Run the installer

### Linux/macOS

```bash
python3 install.py
source ~/.bashrc
```

### Windows

```bash
python install_windows.py
```

---

## Step 3 — Verify installation

```bash
ars version
```

Expected:

```txt
ARSLang v0.1.0
```

---

# 🧩 VS Code Extension

ARSLang has an official VS Code extension with:

- Syntax highlighting
- Smart autocomplete
- Run ARSLang button
- Error diagnostics
- Auto formatting

Install from VS Code Marketplace:

```txt
Search: ARSLang
```

---

# 🏁 Getting Started

Create your first program:

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

Every ARSLang program must contain:

```ars
void ars.prime(){
    
}
```

This is the entry point of the program.

---

## Output

Use:

```ars
ars.out("Hello")
```

Example:

```ars
void ars.prime(){
    ars.out("Welcome to ARSLang")
}
```

---

## Escape Sequences

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

---

## Comments

### Single-line comment

```ars
## This is a comment
```

### Multi-line comment

```ars
**
This is a
multi-line comment
**
```

---

# 🖥️ CLI Commands

| Command | Description |
|---|---|
| `ars new file.ars` | Create a new ARSLang file |
| `ars run file.ars` | Run program |
| `ars check file.ars` | Validate syntax |
| `ars version` | Show version |
| `ars help` | Show help |

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

## Using Comments

```ars
void ars.prime(){

    ## Greeting
    ars.out("Good morning!")

    **
    Hidden code
    ars.out("Not executed")
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

# 🗺️ Roadmap

Planned future features:

- [ ] Variables
- [ ] Numbers
- [ ] Arithmetic
- [ ] Conditions
- [ ] Loops
- [ ] Functions
- [ ] Import system
- [ ] Standard library
- [ ] AI integration
- [ ] Real parser & AST
- [ ] Bytecode VM
- [ ] Package manager

---

# 🤝 Contributing

Contributions are welcome.

Steps:

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push branch
5. Open Pull Request

---

# 📄 License

MIT License

```txt
Copyright (c) 2026 A R S

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction.
```

---

<div align="center">

Made with ❤️ by A R S

⭐ Star the repository if you find ARSLang interesting.

</div>