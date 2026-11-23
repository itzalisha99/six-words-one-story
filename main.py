"""Six Words, One Story — make.fun bounty entry.

Writes one complete story in exactly six words to /output/entry.txt.
Python 3, standard library only, no network, fully deterministic.
"""

import os

STORY = "The letter arrived after the funeral."


def main():
    words = STORY.split()
    assert len(words) == 6, f"story must be exactly six words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, "story must be 1-60 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
