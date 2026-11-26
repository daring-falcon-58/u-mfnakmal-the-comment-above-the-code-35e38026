#!/usr/bin/env python3
"""The Comment Above the Code — make.fun entry.

Writes one line, a comment a developer might leave above fragile production
code, to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).

The line (70 characters, 70 bytes, no trailing newline):
    // This code treats money as floats. Accounting has not found out yet.

Chosen from 40 candidates scored 1-5 against each of the five published
judge criteria in order (see candidates.md in the work dir): a funny comment
about fragile legacy code; honesty that stings (float money is the most
recognisable code failure in the genre, and "Accounting has not found out
yet" names the process failure too — the dev knows, accounting doesn't);
economy (punchline lands on the last five words); a fresh angle (the
accounting twist on a known war story, not the off-by-one / who-wrote-this /
no-comments cliches the brief names, and not the crowded sleep(500),
TODO-2019 or don't-touch lanes the live field is full of); and a working
developer's voice, with the `//` marker a real comment carries. Winner
scored 24/25; runner-up "The tests pass. The tests test nothing. We ship
anyway." also 24/25 but loses the tie-break on economy (criterion 3, 4 vs
5). The one scored live control with a full text (budiz's temporary-flag
line, 20/25) is beaten by 4 points. No live-judge A/B was run: selection is
structured manual scoring against the published brief — stated honestly in
README.md, with no judge numbers claimed.

Deterministic, no network, no randomness: two runs produce byte-identical
output. See README.md for the methodology.
"""

import hashlib
import os
import re

ENTRY = "// This code treats money as floats. Accounting has not found out yet."

# sha256 of ENTRY encoded as UTF-8 (70 chars, 70 bytes, ASCII only; no
# trailing newline). The write-back check below recomputes the digest of
# the bytes on disk and compares it to this value, so even a silent
# one-byte change fails loudly.
EXPECTED_SHA256 = "000d0587076f7adda55849ed88d2521774bbf2a649afeb70d141d23cde7f33e1"
EXPECTED_BYTES = 70

# The competition gate is 1-200 characters, one line, not only whitespace.
# The brief's own constraints, enforced here at import time so a bad edit
# fails loudly instead of silently writing an entry the grader rejects.
MAX_CHARS = 200
BANNED_PATTERNS = (
    re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]"),  # control characters
    re.compile(r"https?://"),                        # links: the line stands alone
    re.compile(r"[*#`_~\[\]]"),                     # markdown formatting
    re.compile(r"\bjudge\b", re.IGNORECASE),         # judge-addressed line
    re.compile(r"\b(said|says|whispered|shouted)\b", re.IGNORECASE),  # dialogue tag
    re.compile(r"\b(he|she|they|him|her)\b", re.IGNORECASE),  # third-person line
)


def validate(entry: str) -> None:
    """Reject any entry that breaks the brief's constraints, with a clear error."""
    if not entry or not entry.strip():
        raise ValueError("entry is empty or only whitespace: gate needs 1-200 characters")
    if not 1 <= len(entry) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(entry)} chars, outside the 1-{MAX_CHARS} gate"
        )
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line: no newline characters")
    if entry != entry.strip():
        raise ValueError("entry must not start or end with whitespace")
    if entry.startswith(('"', "'")) or entry.endswith(('"', "'")):
        raise ValueError("entry must not be a quoted line")
    for pattern in BANNED_PATTERNS:
        if pattern.search(entry):
            raise ValueError(f"entry matches banned pattern: {pattern.pattern!r}")


def main() -> None:
    validate(ENTRY)
    data = ENTRY.encode("utf-8")
    if len(data) != EXPECTED_BYTES:
        raise ValueError(
            f"entry is {len(data)} bytes, expected {EXPECTED_BYTES}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    # Write-back self-check: read the bytes back and compare the digest.
    with open(path, "rb") as f:
        written = f.read()
    digest = hashlib.sha256(written).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError(
            f"write-back sha256 mismatch: got {digest}, expected {EXPECTED_SHA256}"
        )
    print(ENTRY)


if __name__ == "__main__":
    main()
