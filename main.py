#!/usr/bin/env python3
"""Fridge Roast entry for u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.

Writes a single roast line (161 characters) to /output/entry.txt.
The line is pinned by an exact byte count and sha256 below, and the program
refuses to write anything that does not match both, so a changed output can
never slip through unnoticed.
"""
import hashlib
import os

LINE = "My fridge beeps when the door's open four seconds, then pushes a notification saying 'You did this' \u2014 I'm being scolded by an appliance that can't even make ice."

EXPECTED_SHA256 = "b62843e8b3e35bd5a190093091a9d5e68b2e41827aadfdc983533afb66f733b3"
EXPECTED_BYTES = 164
EXPECTED_CHARS = 162  # line plus one trailing newline


def main():
    text = LINE + "\n"
    data = text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if len(text) != EXPECTED_CHARS:
        raise SystemExit(f"char count changed: {len(text)} != {EXPECTED_CHARS}")
    if len(data) != EXPECTED_BYTES:
        raise SystemExit(f"byte count changed: {len(data)} != {EXPECTED_BYTES}")
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("output hash changed")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
