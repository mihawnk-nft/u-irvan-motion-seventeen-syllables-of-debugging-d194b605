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

# Hand-verified syllable counts, one per line: 5-7-5.
SYLLABLES_PER_LINE = (5, 7, 5)

# Syllable count per word, verified by hand against a dictionary count.
SYLLABLES = {
    "breakpoint": 2, "holds": 1, "its": 1, "breath": 1,
    "the": 1, "stack": 1, "unwinds": 2, "past": 1, "midnight": 2,
    "one": 1, "semicolon": 4,
}


def validate(text: str) -> None:
    """Check the haiku the gate checks: 3 lines, 5-7-5, 1-200 chars."""
    lines = text.split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    for line, expected in zip(lines, SYLLABLES_PER_LINE):
        counted = sum(SYLLABLES[word.lower()] for word in line.split())
        assert counted == expected, f"{line!r}: {counted} syllables, expected {expected}"
    assert 1 <= len(text) <= 200, f"{len(text)} characters, must be 1-200"
    assert text.strip() == text, "leading/trailing whitespace"


def main() -> None:
    validate(HAIKU)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)

if __name__ == "__main__":
    main()
