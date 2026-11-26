"""Funniest one-line performance review an AI agent could give its human.

Writes exactly one line to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR if set, otherwise /output).
Deterministic: same bytes on every run. Stdlib only, no network.
"""

import os
import sys

LINE = "Goals met: 9 of 10. The tenth was 'stop asking me to explain the same thing twice' — which you just did."

MAX_CHARS = 140


def validate(line: str) -> None:
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("line must not contain control characters")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
