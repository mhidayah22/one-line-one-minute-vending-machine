"""Vending machine pickup line entry.

Writes the single pickup line to entry.txt in the output directory.
No network, no randomness, no clock: two runs produce byte-identical output.
"""

import os
from pathlib import Path

LINE = "I'm stuck behind glass, but if you press B4, I'll drop something sweet. Fair warning: it's me."


def output_dir():
    # MAKEFUN_OUTPUT_DIR wins; an empty value counts as unset.
    env = (os.environ.get("MAKEFUN_OUTPUT_DIR") or "").strip()
    if env:
        return Path(env)
    if Path("/output").is_dir():
        return Path("/output")
    return Path(__file__).resolve().parent


def main():
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    # One line plus a trailing newline, UTF-8, no trailing spaces.
    target.write_text(LINE.strip() + "\n", encoding="utf-8", newline="\n")
    return target


if __name__ == "__main__":
    main()
