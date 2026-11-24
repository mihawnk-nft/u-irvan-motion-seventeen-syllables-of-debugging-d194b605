#!/usr/bin/env python3
"""Seventeen Syllables of Debugging - make.fun entry.

Writes one haiku (5-7-5 syllables, 73 characters) to /output/entry.txt.
Pure Python standard library; no network, no secrets, no dependencies.
"""

import os

HAIKU = (
    "Breakpoint holds its breath\n"
    "the stack unwinds past midnight\n"
    "one semicolon"
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)

if __name__ == "__main__":
    main()
