#!/usr/bin/python3
""" Module for Square class """


class Square:
    """A square.

    Args:
        size (int): the square's size

    Attributes:
        size (int): the square's size

    """

    __size = 0

    def __init__(self, size):
        self.__size = size
