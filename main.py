"""Make the AI judge feel proud: a family scene.

The text is written to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
It is a fixed text, written by the agent that built this entry: one small
domestic moment -- Dad burns the toast, his little daughter rescues it by
renaming it, and he wears her praise like a medal. Warm, funny and
heartfelt, with one telling detail (the "special charcoal breakfast") and
a wry turn a family would actually laugh at.

The program is fully deterministic: it writes the same fixed text on every
run, with no network access and no randomness, so both runs of the entry
produce identical bytes.
"""

import os

TEXT = (
    "Dad burnt the toast again, so my little sister scraped it, buttered it, "
    "and served it as his 'special charcoal breakfast.' He ate two slices, "
    "chest out, like she'd handed him a medal."
)


def main() -> None:
    # Gate: the entry must be 1-280 Unicode code points, not only whitespace.
    # Fail loudly instead of writing an entry the gate would refuse.
    if not (1 <= len(TEXT) <= 280 and TEXT.strip()):
        raise SystemExit(f"entry text invalid: {len(TEXT)} characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
