#!/usr/bin/python3
"""
This module contains one function for indenting text
"""


def text_indentation(text):
    """
    Indents the text.

    Args:
        text (str) : the text to indent

    Returns:
        Nothing.
    """

    if isinstance(text, str) is not True:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print("{0}".format(text[i]), end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("")
            print("")
            if text[i+1] == " ":
                i = i + 1
        i = i + 1
