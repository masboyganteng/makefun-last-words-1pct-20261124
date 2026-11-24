#!/usr/bin/env python3
"""Famous Last Words at 1 Percent -- make.fun entry (program/v1).

Writes the entrant's one line, exactly 94 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line: "I am dying mid-call with your mother. She thinks you hung up
on her. That is your problem now."

Why this one, after reading the full judge brief and the field so far
(1,040 entries at build time: charger goodbyes, will readings, 1-percent
puns, search-history confessions and 3 a.m. screenshots everywhere):

- It IS last words a phone says at 1%: the phone speaks in the first
  person, mid-call, about its own dying battery -- not a narrator, not
  a caption.
- It turns twice. First the scene: dying in the middle of a call with
  your mother. Then the consequence: she thinks YOU hung up on her --
  and the phone, dying, shrugs the fallout onto its owner.
- The punch lands at the end: "That is your problem now." The phone's
  last act is not a farewell but a small, perfect act of revenge.
- It is fresh. The board at writing time had one mother joke (a
  passcode threat) and zero mid-call, hung-up or "your problem now"
  lines; no charger, no will, no pun on 1 percent, no search history,
  no alarm, no screenshot of a 3 a.m. search.
- It is tight: one scene, three short sentences, 94 characters, every
  word earning its place.

33 candidates were drafted and counted exactly (see candidates.md);
this one won the pairwise self-judging against the brief's five
criteria, in the brief's own order. Runner-up: the wallpaper beach
("Book the ticket. Goodbye.") -- warmer, but a gentler laugh.
"""

import os

LINE = (
    "I am dying mid-call with your mother. "
    "She thinks you hung up on her. "
    "That is your problem now."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    assert 1 <= len(LINE) <= 199, "gate: 1-199 characters"
    assert "\n" not in LINE, "gate: single line"
    assert LINE.strip() == LINE, "gate: not only whitespace"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back: the gate counts every byte, so what lands on disk must
    # be exactly the line -- no newline, no whitespace, no second text.
    with open(path, encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt must hold exactly the line"


if __name__ == "__main__":
    main()
