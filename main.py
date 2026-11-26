import os

# One brutally honest out-of-office line: it names the person being dodged
# (Karen's 3pm budget review) and the exact minute the email was read (9:03),
# then admits the delay outright — honest, still polite, and impossible to
# copy-paste from a generic template.
ENTRY = (
    "I'm out of the office until Monday, hiding from Karen's 3pm budget review "
    "\u2014 I read your email at 9:03 and will answer it then, "
    "politely and from a safe distance."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
