import os

# One Word, First Thought: the word is the whole entry.
#
# Final word: "psithurism" — the sound of wind moving through
# trees. It beats the first draft ("petrichor") on the judge's own
# criteria: it is more surprising (petrichor is a staple of every
# "most beautiful word" list, so the field will be full of it, and
# byte-identical entries share one rate), more vivid in a different
# sense (a sound you can almost hear, not just a smell), and it
# carries a spark of wit in its whispering "ps-" sound — the word
# sounds like what it means. Ten letters, one word, no filler.
# The gate requires 1 to 24 UTF-8 characters, not only whitespace,
# so the program writes the single word with no trailing newline
# and nothing else.
WORD = "psithurism"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    # Guard the gate: the entry is only valid if the file holds
    # exactly one word of 1-24 characters. Read it back and fail
    # loudly rather than ever submitting a blank or invalid file.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if len(written) < 1 or len(written) > 24 or written != WORD:
        raise ValueError("entry.txt must hold exactly one word, got %r" % written)


if __name__ == "__main__":
    main()
