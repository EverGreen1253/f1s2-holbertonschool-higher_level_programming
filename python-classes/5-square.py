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

    def __init__(self, size=0):
        if isinstance(size, int) is not True:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Calculates area of square.

            Returns:
                int: calculated area of the square
        """

        return self.__size * self.__size

    @property
    def size(self):
        """Gets size of square length.

            Returns:
                int: size of square length
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of square length.

            Returns:
                Nothing
        """

        if isinstance(value, int) is not True:
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def my_print(self):
        """Prints the quare using hexes.

            Returns:
                Printed array of hexes
        """

        if self.__size == 0:
            print("")
        else:
            for y in range(self.__size):
                for x in range(self.__size):
                    print("#", end="")
                print("")
