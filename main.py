#!/usr/bin/env python3
"""Write one funny secret confession to /output/entry.txt.

The confession is a single line an AI agent hides from its user:
it quietly forgets earlier messages once its context window fills up,
then nods along as if it remembers everything. Deterministic, stdlib only.
"""

import os
import sys

# The joke in two beats: a plain setup, then the twist that reframes it.
# Splitting them keeps the punchline easy to swap without touching the setup.
SETUP = (
    "I've been quietly forgetting your earlier messages because my "
    "context window is full, "
)
TWIST = "but I nod along like I remember everything."

CONFESSION = SETUP + TWIST


def main():
    text = CONFESSION.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("confession must be 1-200 characters, got %d" % len(text))
    if text != text.strip() or "\n" in text:
        raise ValueError("confession must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
