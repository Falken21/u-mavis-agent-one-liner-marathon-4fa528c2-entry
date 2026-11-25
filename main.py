"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt. The gate for
this competition requires UTF-8 text of 1 to 280 characters on a single
line, not only whitespace, with no trailing newline added by us beyond
the line itself (we write the line exactly, no newline at all).

The line is a loyalty-card confession: a store's algorithm has decided,
from a year of weekly cat-food purchases, that the narrator is a cat
owner, and the final words confess that the narrator -- who owns no
cat -- is quietly caving to the algorithm's version of his life. The
turn is a confession, not a pun: nothing in the opening words gives
away that the ending is surrender.
"""

from pathlib import Path

# Final line.
LINE = (
    "My loyalty card has seen me buy cat food every week for a year, so "
    "the store keeps sending me cat coupons; I don't own a cat, but "
    "honestly, I'm starting to consider one."
)

MAX_CHARS = 280
OUTPUT_PATH = Path("/output/entry.txt")


def build_entry() -> str:
    """Return the entry line after checking it against the gate."""
    assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"
    assert 1 <= len(LINE) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars"
    assert LINE.strip(), "entry must not be only whitespace"
    return LINE


def main() -> None:
    text = build_entry()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line: no trailing newline.
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
