#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes a single error line (1-140 UTF-8 chars) to /output/entry.txt:
the error message an AI agent shows when it runs out of tokens
mid-sentence. Chosen line: flat error tone, second beat, concrete
closing image — no stock apology, no explanation of the joke.
"""

import os

LINE = "Error: token budget exhausted. I had a great point. It is now compost."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
