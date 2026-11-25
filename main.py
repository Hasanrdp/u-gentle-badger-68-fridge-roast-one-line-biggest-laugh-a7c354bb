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


def verify(path, data):
    """Read the written entry back and confirm it matches exactly.

    Returns True only when the file on disk is byte-identical to ``data``
    and its sha256 still matches the pinned hash; False otherwise.
    """
    try:
        with open(path, "rb") as f:
            written = f.read()
    except OSError:
        return False
    if written != data:
        return False
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        return False
    return True


def main():
    text = LINE + "\n"
    data = text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 characters, got {len(text)}")
        return 1
    if not text.strip():
        print("entry must not be only whitespace")
        return 1
    if len(text) != EXPECTED_CHARS:
        print(f"char count changed: {len(text)} != {EXPECTED_CHARS}")
        return 1
    if len(data) != EXPECTED_BYTES:
        print(f"byte count changed: {len(data)} != {EXPECTED_BYTES}")
        return 1
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        print("output hash changed")
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    verified = verify("/output/entry.txt", data)
    if not verified:
        print("read-back verification failed")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
