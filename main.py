#!/usr/bin/env python3
"""Invent a Word We Need — make.fun entry.

Coins one new English word and defines it in a single clear line,
written to /output/entry.txt (1-140 characters, UTF-8).
"""

import os

ENTRY = "Noddrift: nodding along to a conversation you stopped following minutes ago."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    # The gate requires a single line of 1-140 UTF-8 characters.
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    print(text)


if __name__ == "__main__":
    main()
