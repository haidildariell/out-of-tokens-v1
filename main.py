#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes a single error line (1-140 UTF-8 chars) to /output/entry.txt:
the error message an AI agent shows when it runs out of tokens
mid-sentence. Chosen line: flat error tone, second beat, concrete
closing image — no stock apology, no explanation of the joke.

Structure: the line is assembled by build_entry() from two named
fragments (SETUP + PUNCH) and checked by validate_entry() against the
1-140 char limit before it is written, so a future edit to either
beat is caught immediately if it breaks the limit.
"""

import os

SETUP = "Error: token budget exhausted. I had a great point."
PUNCH = " It is now compost."


def build_entry() -> str:
    """Assemble the entry line from its two beats.

    The setup states the failure; the punch closes it with a concrete
    image. Kept as separate fragments so each beat can be tuned
    independently without touching the other.
    """
    return SETUP + PUNCH


def validate_entry(line: str) -> None:
    """Check the entry line fits the competition's 1-140 char limit."""
    if not 1 <= len(line) <= 140:
        raise ValueError(f"entry must be 1-140 chars, got {len(line)}")


def main() -> None:
    line = build_entry()
    validate_entry(line)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
