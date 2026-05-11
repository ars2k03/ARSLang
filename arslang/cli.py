#!/usr/bin/env python3

import re
import sys


VERSION = "ARSLang v0.1.0"


def show_usage():
    print("Usage:")
    print("  ars new filename.ars")
    print("  ars check filename.ars")
    print("  ars run filename.ars")
    print("  ars version")
    print("  ars help")


def show_help():
    print("ARSLang Help")
    print("")
    print("Commands:")
    print("  ars new filename.ars")
    print("  ars check filename.ars")
    print("  ars run filename.ars")
    print("  ars version")
    print("  ars help")
    print("")
    print("Syntax:")
    print('  void ars.prime(){')
    print('      ars.out("text")')
    print('  }')
    print("")
    print("Escape Support:")
    print(r'  \n  = new line')
    print(r'  \"  = double quote')
    print(r"  \'  = single quote")
    print(r'  \\  = backslash')
    print("")
    print("Comments:")
    print("  ## single line comment")
    print("  **")
    print("  multiline comment")
    print("  **")


def create_ars_file(filename):
    if not filename.endswith(".ars"):
        print("Error: File must end with .ars")
        return

    try:
        with open(filename, "x", encoding="utf-8") as file:
            file.write('void ars.prime(){\n')
            file.write('    ars.out("Hello ARSLang")\n')
            file.write('}\n')

        print(f"Created: {filename}")

    except FileExistsError:
        print(f"Error: File already exists: {filename}")


def decode_string(text):
    try:
        return bytes(text, "utf-8").decode("unicode_escape")
    except UnicodeDecodeError:
        return None


def parse_ars_file(filename):
    if not filename.endswith(".ars"):
        return False, "Error: Only .ars files are allowed", []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            code = file.read()

    except FileNotFoundError:
        return False, f"Error: File not found: {filename}", []

    main_match = re.fullmatch(
        r'\s*void\s+ars\.prime\s*\(\)\s*\{\s*([\s\S]*?)\s*\}\s*',
        code
    )

    if not main_match:
        return False, "Syntax Error: Invalid program structure", []

    main_body = main_match.group(1)
    lines = main_body.strip().splitlines()
    outputs = []
    in_comment = False

    for index, line in enumerate(lines, start=2):
        line = line.strip()

        if line == "":
            continue

        if line == "**":
            in_comment = not in_comment
            continue

        if in_comment:
            continue

        if line.startswith("##"):
            continue

        match = re.fullmatch(r'ars\.out\s*\(\s*"((?:\\.|[^"\\])*)"\s*\)', line)

        if match:
            raw_text = match.group(1)
            decoded_text = decode_string(raw_text)

            if decoded_text is None:
                return False, f"Syntax Error at line {index}: Invalid escape sequence", []

            outputs.append(decoded_text)
        else:
            return False, f"Syntax Error at line {index}: {line}", []

    if in_comment:
        return False, "Syntax Error: Multiline comment not closed", []

    return True, "Syntax OK", outputs


def check_ars_file(filename):
    is_valid, message, _ = parse_ars_file(filename)
    print(message)


def run_ars_file(filename):
    is_valid, message, outputs = parse_ars_file(filename)

    if not is_valid:
        print(message)
        return

    for output in outputs:
        print(output)


def main():
    if len(sys.argv) < 2:
        show_usage()
        return

    command = sys.argv[1]

    if command == "version":
        print(VERSION)

    elif command == "help":
        show_help()

    elif command == "new":
        if len(sys.argv) < 3:
            print("Usage: ars new filename.ars")
        else:
            create_ars_file(sys.argv[2])

    elif command == "check":
        if len(sys.argv) < 3:
            print("Usage: ars check filename.ars")
        else:
            check_ars_file(sys.argv[2])

    elif command == "run":
        if len(sys.argv) < 3:
            print("Usage: ars run filename.ars")
        else:
            run_ars_file(sys.argv[2])

    else:
        print("Error: Unknown command")
        show_usage()


if __name__ == "__main__":
    main()