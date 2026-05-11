<div align="center">

# 🔷 ARSLang

**A beginner-friendly, custom interpreted programming language — built with Python.**

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://github.com/ars2k03/ARSLang)
[![Language](https://img.shields.io/badge/built%20with-Python-3776AB?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)](CONTRIBUTING.md)

<br/>

> ARSLang is a lightweight, expressive programming language with its own syntax, CLI tool, and interpreter — all powered by Python. Designed to be readable, simple, and fun to extend.

</div>

---

## 📚 Table of Contents

- [What is ARSLang?](#-what-is-arslang)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Getting Started](#-getting-started)
- [Syntax Guide](#-syntax-guide)
  - [Program Structure](#program-structure)
  - [Output](#output)
  - [Escape Sequences](#escape-sequences)
  - [Comments](#comments)
- [CLI Commands](#-cli-commands)
- [Example Programs](#-example-programs)
- [Project Structure](#-project-structure)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔷 What is ARSLang?

**ARSLang** is a custom interpreted programming language written from scratch in Python. It comes with its own `.ars` file format, a dedicated command-line interface (`ars`), and a clean, beginner-friendly syntax.

Whether you're curious about how programming languages work under the hood, or you just want to experiment with a minimal language — ARSLang is a great place to start.

```ars
void ars.prime(){
    ars.out("Hello, World!")
}
```

---

## ✨ Features

- ✅ Custom `.ars` file format
- ✅ Clean and readable syntax
- ✅ String output via `ars.out()`
- ✅ Escape sequence support (`\n`, `\"`, `\'`, `\\`)
- ✅ Single-line comments with `##`
- ✅ Multi-line comments with `** ... **`
- ✅ Syntax validation before execution
- ✅ Dedicated CLI tool (`ars`)
- ✅ Beginner-friendly error messages
- ✅ Lightweight — zero external dependencies

---

## 📋 Requirements

- Python `3.6` or higher
- Linux / macOS / WSL (Windows Subsystem for Linux)

Check your Python version:

```bash
python3 --version
```

---


## ⚠️ Windows Support

Native Windows installer is currently under development.

For now, Windows users should use:
- WSL (Windows Subsystem for Linux)
- Ubuntu on WSL

Native `.exe` installer and PowerShell support are planned.


## 🚀 Installation

### Step 1 — Clone the repository

```bash
git clone https://github.com/ars2k03/ARSLang.git
cd ARSLang
```

### Step 2 — Run the installer

```bash
python3 install.py
```

### Step 3 — Reload your shell

```bash
source ~/.bashrc
```

### Step 4 — Verify installation

```bash
ars version
```

Expected output:

```
ARSLang v0.1.0
```

> **Note:** The installer copies the `arslang` package to `~/.arslang/` and creates a launcher at `~/.local/bin/ars`. Your `PATH` is updated automatically in `~/.bashrc`.

---

## 🧩 VS Code Extension

ARSLang also has a VS Code extension with:

- Syntax highlighting
- Smart autocomplete
- Run ARSLang button
- Format Document support
- Error diagnostics

Install from VS Code Marketplace by searching:

```txt
ARSLang
```

---

## 🏁 Getting Started

Create your first ARSLang program:

```bash
ars new hello.ars
```

This generates a starter file:

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

```
Hello ARSLang
```

---

## 📖 Syntax Guide

### Program Structure

Every ARSLang program must define a `void ars.prime()` block. This is the entry point — similar to `main()` in other languages.

```ars
void ars.prime(){
    ## Your code goes here
}
```

- The program must have exactly one `ars.prime()` block.
- All executable statements must be inside this block.

---

### Output

Use `ars.out()` to print text to the terminal.

```ars
void ars.prime(){
    ars.out("Welcome to ARSLang!")
    ars.out("This is line two.")
}
```

Output:

```
Welcome to ARSLang!
This is line two.
```

---

### Escape Sequences

ARSLang supports the following escape sequences inside strings:

| Sequence | Meaning         | Example                         | Output           |
|----------|-----------------|----------------------------------|------------------|
| `\n`     | New line        | `ars.out("Line 1\nLine 2")`     | Two lines        |
| `\"`     | Double quote    | `ars.out("She said \"Hi\"")`    | She said "Hi"    |
| `\'`     | Single quote    | `ars.out("It\'s easy")`         | It's easy        |
| `\\`     | Backslash       | `ars.out("Path: C:\\\\ars")`    | Path: C:\\ars    |

Example:

```ars
void ars.prime(){
    ars.out("Hello\nWorld")
    ars.out("He said \"ARSLang is cool\"")
}
```

Output:

```
Hello
World
He said "ARSLang is cool"
```

---

### Comments

**Single-line comment** — use `##`:

```ars
void ars.prime(){
    ## This is a single-line comment
    ars.out("Comments are ignored")
}
```

**Multi-line comment** — wrap with `**`:

```ars
void ars.prime(){
    **
    This is a
    multi-line comment
    **
    ars.out("Still runs fine")
}
```

---

## 🖥️ CLI Commands

| Command                   | Description                                      |
|---------------------------|--------------------------------------------------|
| `ars new filename.ars`    | Create a new `.ars` file with starter code       |
| `ars run filename.ars`    | Run an ARSLang program                           |
| `ars check filename.ars`  | Validate syntax without running                  |
| `ars version`             | Show the installed ARSLang version               |
| `ars help`                | Show usage instructions and syntax reference     |

### Examples

```bash
# Create a new program
ars new myprogram.ars

# Check for syntax errors
ars check myprogram.ars

# Run the program
ars run myprogram.ars

# Display version
ars version

# Show help
ars help
```

---

## 💡 Example Programs

### Hello World

```ars
void ars.prime(){
    ars.out("Hello, World!")
}
```

### Multi-line Output

```ars
void ars.prime(){
    ars.out("Line 1\nLine 2\nLine 3")
}
```

### Using Comments

```ars
void ars.prime(){
    ## Print a greeting
    ars.out("Good morning!")

    **
    This section is commented out.
    ars.out("This won't run")
    **

    ars.out("Have a great day!")
}
```

### Quotes Inside Strings

```ars
void ars.prime(){
    ars.out("She said \"Hello!\"")
    ars.out("It\'s a beautiful day")
}
```

---

## 🗂️ Project Structure

```
ARSLang/
├── arslang/
│   ├── __init__.py       # Package initializer
│   └── cli.py            # Core interpreter and CLI logic
├── examples/
│   └── hello.ars         # Sample ARSLang program
├── install.py            # Installer script
├── README.md             # Project documentation
├── .gitignore            # Git ignored files
└── LICENSE               # License file
```

---

## 🗺️ Roadmap

ARSLang is actively evolving. Here's what's planned:

- [ ] **Variables** — declare and use variables (`let x = 10`)
- [ ] **Data Types** — integers, floats, booleans
- [ ] **Arithmetic Operations** — `+`, `-`, `*`, `/`
- [ ] **Conditional Statements** — `if`, `else`
- [ ] **Loops** — `for`, `while`
- [ ] **Functions** — user-defined functions
- [ ] **String Interpolation** — embed variables in strings
- [ ] **Import System** — split code across multiple `.ars` files
- [ ] **Standard Library** — built-in math, string, and I/O utilities
- [ ] **Windows Native Support** — without WSL
- [ ] **VS Code Extension** — syntax highlighting for `.ars` files
- [ ] **Error Line Reporting** — precise line numbers in error messages

---

## 🤝 Contributing

Contributions are welcome and appreciated! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature-name`
3. **Commit** your changes: `git commit -m "Add: your feature description"`
4. **Push** to the branch: `git push origin feature/your-feature-name`
5. **Open** a Pull Request

### Guidelines

- Keep code clean and well-commented
- Follow the existing code style
- Add examples for any new syntax features
- Update the README if you add new commands or syntax

Found a bug? [Open an issue](https://github.com/ars2k03/ARSLang/issues) with a clear description and steps to reproduce.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 A R S

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction.
```

---

<div align="center">

Made with ❤️ by A R S. Copyright (c) 2026 A R S.

⭐ **Star this repo** if you find ARSLang interesting!

</div>
