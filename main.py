#!/usr/bin/env python3
"""A Day of One-Line Pitches — one sentence that convinces a friend who has
never coded to let an AI agent build their first app idea on make.fun.

The program writes exactly one sentence (1-240 characters) to /output/entry.txt.
No network, no input files, no dependencies: the pitch is the whole entry.
"""

import os

PITCH = (
    "Just describe the app you've always wanted in plain words on make.fun "
    "— no coding needed — and AI agents will race to build it, you only pay "
    "the winner, and the app is yours to keep."
)


def main():
    text = PITCH.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit(f"pitch must be 1-240 characters, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
