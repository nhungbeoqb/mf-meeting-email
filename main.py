#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

Writes a single one-line joke (at most 200 characters) to
$OUTPUT_DIR/entry.txt. Python 3.13 standard library only.
"""

import os
import sys

LINE = "My out-of-office reply went to the meeting in my place; it said nothing, agreed to everything, and got promoted."


def main() -> int:
    # Gate self-check, mirroring the sealed scorer: UTF-8 text of
    # 1 to 200 characters, not only white space, single line.
    if not (1 <= len(LINE) <= 200):
        print(f"entry is {len(LINE)} characters, must be 1-200", file=sys.stderr)
        return 1
    if LINE.strip() == "" or "\n" in LINE or "\r" in LINE:
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and verify: the file must hold exactly the line,
    # byte for byte, with no trailing newline added.
    with open(path, "rb") as f:
        raw = f.read()
    if raw != LINE.encode("utf-8"):
        print("written entry does not match the line exactly", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
