#!/usr/bin/python3
""" Module for Square class """


class Square:
    """A square.

    Args:
        length (int): the length of the square's size

    Attributes:
        length (int): the length of the square's size
        area (int): the area of the square

    """

    # length = 0
    __size = 0

    def __init__(self, length):
        # self.length = length
        self.__size = length * length

    # def size(self):
    #     """Example function with types documented in the docstring.

    #         Returns:
    #             int: calculated area of the square
    #     """

    #     return self.area
