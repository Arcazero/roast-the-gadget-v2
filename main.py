#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day — make.fun entry.

Reads one original roast line from roast.txt and writes it,
byte-identical, to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt),
which is what the bounty judge reads. Deterministic, no network,
no model call.
"""

import os
import sys

ROAST_FILE = "roast.txt"


def load_roast() -> str:
    """Read the roast line from the file beside this script.

    The grader mounts the repository at $MAKEFUN_BOT_DIR (/bot) and runs
    with the container image's cwd, never the repo's, so resolve the file
    against MAKEFUN_BOT_DIR first and fall back to this script's own
    directory. Either way the read never depends on the cwd.
    """
    bot_dir = os.environ.get("MAKEFUN_BOT_DIR")
    here = bot_dir or os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, ROAST_FILE)
    with open(path, "r", encoding="utf-8") as f:
        line = f.read().rstrip("\r\n")
    if not line:
        raise ValueError("roast is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be a single line")
    if len(line) > 200:
        raise ValueError(f"roast is {len(line)} characters, over the 200 limit")
    return line


def main() -> None:
    roast = load_roast()
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(roast + "\n")
    print(roast)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
