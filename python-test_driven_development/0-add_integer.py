#!/usr/bin/python3
"""
This module contains one function for adding 2 integers together
"""

def add_integer(a, b=98):
    """
    Sums up the arguments passed in.

    Args:
        a (int) : first one
        b (int) : second one (default value 98)

    Returns:
        int: sum of a and b
    """

    one = a
    two = b

    if isinstance(one, float) is True:
        one = int(one)

    if isinstance(two, float) is True:
        two = int(two)

    if isinstance(one, int) is not True:
        raise TypeError("a must be an integer")

    if isinstance(two, int) is not True:
        raise TypeError("b must be an integer")

    return one + two
