#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

Writes the entry — one single-line error message a kitchen toaster shows
its owner when something goes wrong — to /output/entry.txt. Standard
library only, fully deterministic: the same line is written on every run.
"""

import os

ENTRY = "ERROR E07: Toast deceased. Survived by crumbs."


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.isascii(), "entry must be ASCII only"
    assert "\u2014" not in ENTRY, "entry must not contain an em dash"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
