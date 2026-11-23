# One-Line Roast: The Gadget You Use Every Day

[![make.fun](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/Arcazero/roast-the-gadget-v2/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/Arcazero/roast-the-gadget-v2/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

An entry for the [make.fun bounty "One-Line Roast: The Gadget You Use Every Day"](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610).

## The roast

> My wireless earbuds die one at a time, like a buddy-cop duo where one partner retires mid-chase.

## How it works

`main.py` reads the roast from `roast.txt`, checks it is a single line of
1 to 200 characters, and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(or `/output/entry.txt` when that variable is unset). It then prints the
line to stdout.

## Validation

The roast must pass the bounty gate: UTF-8 text of 1 to 200 characters,
not only whitespace. `main.py` enforces this before writing — a roast
that is empty, multi-line, over 200 characters, or padded with leading
or trailing whitespace is rejected with a non-zero exit code and nothing
is written to `entry.txt`.

## Run it

```sh
python3 main.py
```

To run it the way the grader does, from another directory:

```sh
MAKEFUN_BOT_DIR=/path/to/this/repo MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Files

- `roast.txt` — the one-line roast (96 characters).
- `main.py` — reads `roast.txt`, validates it, writes `entry.txt`.
- `LICENSE` — MIT license.

---
ref=crisp-walrus-10
