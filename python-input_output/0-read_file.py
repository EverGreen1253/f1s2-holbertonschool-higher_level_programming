#!/usr/bin/python3
"""Module docstring goes here"""


def read_file(filename=""):
    """Function docstring goes here"""

    with open('my_file_0.txt', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
    print("")
