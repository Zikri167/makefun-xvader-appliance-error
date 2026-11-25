"""The Funniest Honest Appliance Error — make.fun entry.

Prints exactly one line: the most honest error message a vacuum cleaner
can display when its dust bag is full.
"""

LINE = "Dust bag full. Suction at 12%. I am now a very loud broom with a power cord."


def main() -> None:
    """Validate the error line, then print exactly that one line."""
    if not LINE.isascii():
        raise ValueError("line must be ASCII")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1-200 characters")
    print(LINE)


if __name__ == "__main__":
    main()
