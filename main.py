#!/usr/bin/env python3
"""Funniest Autocorrect Fail — writes one line to /output/entry.txt.

Stdlib only. Honours OUTPUT_DIR env override for local runs.
"""
import os

LINE = "Happy birthday! Hope your day is full of cake and peasants"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
