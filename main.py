#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single line about a useless superpower to /output/entry.txt.

The line: a power (stopping time) whose only window (while asleep)
cancels it completely, with the payoff landing on the last word.
"""
import os
from pathlib import Path

LINE = "I can stop time, but only while I'm asleep \u2014 so I wake up every morning exactly as late as I was going to be anyway."

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
