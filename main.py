#!/usr/bin/env python3
"""One-Line Roast: write the roast line to the output file.

Reads roast.txt from the entry directory (MAKEFUN_BOT_DIR when set,
otherwise the directory holding this file), checks it is a single
line of 1 to 200 characters, and writes it to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset).
"""

import os
import sys
from pathlib import Path


def entry_dir() -> Path:
    bot_dir = os.environ.get("MAKEFUN_BOT_DIR")
    if bot_dir:
        return Path(bot_dir)
    return Path(__file__).resolve().parent


def load_roast() -> str:
    source = entry_dir() / "roast.txt"
    if not source.is_file():
        raise ValueError(f"roast.txt not found in {entry_dir()}")
    text = source.read_text(encoding="utf-8")
    if not text.endswith("\n") or text.count("\n") != 1:
        raise ValueError("roast.txt must hold exactly one line ending in a newline")
    line = text[:-1]
    if not line:
        raise ValueError("roast.txt is empty")
    if line != line.strip():
        raise ValueError("roast must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be exactly one line")
    if len(line) > 200:
        raise ValueError(f"roast is {len(line)} characters, over the 200 limit")
    return line


def main() -> int:
    try:
        line = load_roast()
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "entry.txt"
    out_file.write_text(line + "\n", encoding="utf-8")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
