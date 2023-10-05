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
    __position = (0, 0)
    __msg = "position must be a tuple of 2 positive integers"

    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int) is not True:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

        try:
            if (isinstance(position, tuple) is not True
                    or isinstance(position[0], int) is not True
                    or isinstance(position[1], int) is not True
                    or position[0] < 0
                    or position[1] < 0):
                raise TypeError(self.__msg)
        except IndexError:
            raise TypeError(self.__msg)

        self.__position = position

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
            if self.position[1] > 0:
                for i in range(self.__position[1]):
                    print("")

            for y in range(self.__size):
                if self.position[0] > 0:
                    for j in range(self.__position[0]):
                        print(" ", end="")

                for x in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def position(self):
        """Gets position of square.

            Returns:
                tuple: position of square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """Sets position of square.

            Returns:
                Nothing
        """

        try:
            if (isinstance(value, tuple) is not True
                    or isinstance(value[0], int) is not True
                    or isinstance(value[1], int) is not True
                    or value[0] < 0
                    or value[1] < 0):
                raise TypeError(self.__msg)
        except IndexError:
            raise TypeError(self.__msg)

        self.__position = value
