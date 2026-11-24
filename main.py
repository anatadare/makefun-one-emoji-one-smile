#!/usr/bin/env python3
"""One Emoji, One Smile.

Writes exactly one emoji to /output/entry.txt, nothing else:
no words, no caption, no explanation, no trailing newline.

The emoji is U+1F917 HUGGING FACE: open arms and a warm smile.
It is the warmest friendly gesture a stranger can send at first
glance, understood the same way at any age and in any background,
a deliberate pick rather than the first smiley that comes to mind,
and friendly without the hearts or affection that would read as
intimate or flirtatious coming from someone unknown. A hug also
carries the smile in the body, not just the face, so the warmth
lands even before the reader notices the grin.
"""

import os

EMOJI = "\U0001F917"  # 🤗 Hugging Face


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
