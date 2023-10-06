#!/usr/bin/python3
"""
This module contains one function for printing a square with #
"""


def print_square(size):
    """
    Prints out the square.

    Args:
        size (int) : the size of one side

    Returns:
        Nothing.
    """

    if (isinstance(size, int) is not True or
            (isinstance(size, float) is True and size < 0)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end="")
        print("")
