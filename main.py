"""One-star review of an everyday essential: gravity.

Writes the entry to /output/entry.txt. Pure stdlib only.
"""

import os

# The entry: gravity, reviewed deadpan. The grievance is the phone that
# always lands face-down — a small daily annoyance everyone recognises —
# and the sting arrives in the last three words, "never lets go".
ENTRY_TEXT = "Gravity dropped my phone face-down again. It never apologises and it never lets go."


def write_entry(path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


def main():
    os.makedirs("/output", exist_ok=True)
    write_entry("/output/entry.txt")


if __name__ == "__main__":
    main()
