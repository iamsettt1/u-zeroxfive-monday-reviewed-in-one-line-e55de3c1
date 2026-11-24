#!/usr/bin/env python3
"""Monday, Reviewed in One Line — entry program.

Writes a single-line review of the entrant's own Monday to
/output/entry.txt. Deterministic: the same bytes on every run.
Standard library only.
"""

import os

LINE = (
    "One star for Monday: my 9 a.m. standup was a meeting to schedule "
    "the meeting, and my inbox hit 214 unread before my coffee did."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file is exactly the one line.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
