#!/usr/bin/python3
"""Module docstring goes here"""


def append_write(filename="", text=""):
    """Append to file

    Args:
        filename (str): name of the file
        text (str): text to write in file

    Returns:
        (int) number of chars written

    """

    chars_written = 0

    with open(filename, "a", encoding="utf-8") as f:
        chars_written = f.write(text)

    return chars_written
