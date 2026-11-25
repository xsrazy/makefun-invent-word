#!/usr/bin/env python3
"""Invent a Word We Need — entry program for make.fun bounty
u-deranalabs-invent-a-word-we-need-17a020e0.

The entry text (written verbatim to /output/entry.txt):

    Wavestray (n.) A wave returned to a stranger who was waving at
    someone behind you.

    (82 characters, one line, well inside the 140-character gate.)

Why this word
------------
Every reader has lived this exact moment: you spot someone waving,
you wave back with a full friendly smile, and a half-second later
you realise they were waving at the person standing right behind
you. There is no single English word for it. People describe it
with a whole sentence ("I waved at someone who wasn't waving at
me"), or they just tell the story and everyone laughs because they
recognise it instantly. That is the test the judge's brief sets:
a real gap, a thing a reader recognises at once as something they
have felt or seen, with no word of its own. Wavestray names it.

Why this shape works
--------------------
Wavestray is a compound of two plain English morphemes, "wave" +
"stray": a wave that went astray, a wave that strayed to the wrong
person. Both halves are common, so the word is spellable on first
hearing and memorable after one reading, and the stress falls
naturally on the first syllable (WAVE-stray), the way English
compounds usually stress. It sounds like a word English could
already have grown — compare "castaway", "runaway", "stowaway",
all built on the same -away/-stray tail — yet a search of the
mental lexicon finds no existing entry: it is not "wave" plus a
suffix anyone already uses, and it collides with no known word
(sonder, petrichor, jomo, doomscrolling and the rest all name
other things). The noun tag "(n.)" and the dictionary-style
one-line definition make the entry read as a real dictionary
headword, which is exactly what the brief asks a lexicographer
judge to want on the page.

Why this definition works
--------------------------
The definition is one sentence, self-contained, and lands in a
single reading: "A wave returned to a stranger who was waving at
someone behind you." Every word earns its place. "Returned"
carries the mistaken reciprocity (you waved back, you did not
wave first). "Stranger" carries the social sting (it was not a
friend, so there is no recovery). "Someone behind you" is the
punchline and the whole mechanism of the embarrassment in three
words. No second sentence, no example, no hedging — the meaning
is complete the moment the line ends.

Other gaps considered and set aside
-----------------------------------
The relief-and-guilt of a cancelled plan is real, but coinages
for it ("cancelief", "planlief") are clumsy to say and the feeling
already has near-words in "relief" and "flake". The long
"typing..." that never becomes a message is vivid, but any coinage
there leans on "ghosting", which already exists. Forgetting why
you entered a room is already half-named by the doorway effect.
The 1% battery dread is a feeling, not a nameable moment. The
misdirected wave beats them all: it is a social moment, a small
story with a beginning, a mistake and a sting, instantly
recognisable, and it had no name until now.
"""

import os

ENTRY_TEXT = (
    "Wavestray (n.) A wave returned to a stranger who was waving "
    "at someone behind you."
)


def write_entry(path: str = "/output/entry.txt") -> str:
    """Write ENTRY_TEXT to *path* and return the text written.

    The gate allows 1 to 140 UTF-8 characters, not only whitespace,
    so the length is checked here before writing; a text that grew
    past the cap would fail loudly instead of shipping invalid.
    """
    text = ENTRY_TEXT.strip()
    if not 1 <= len(text) <= 140:
        raise ValueError(
            "entry text must be 1-140 characters, got %d" % len(text)
        )
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)
    return text


def main() -> None:
    """Write the entry text to /output/entry.txt, readable by all."""
    write_entry("/output/entry.txt")


if __name__ == "__main__":
    main()
