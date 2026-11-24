"""Weirdest Job Title: writes the entry to /output/entry.txt."""

from pathlib import Path

LINE = "Senior Apologizer for Self-Driving Cars"


def main() -> None:
    # Gate: the entry must be 1-60 characters of non-blank UTF-8 text.
    if not 1 <= len(LINE) <= 60 or not LINE.strip():
        raise ValueError("entry line must be 1-60 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
