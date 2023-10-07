#!/usr/bin/python3
""" Nameless module for Rectangle class """


class Rectangle:
    """A rectangle.

    Args:
        None

    Returns:
        Nothing

    """

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for private prop width

            Returns:
                value of __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets value of width.

            Returns:
                Nothing
        """

        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter for private prop height

            Returns:
                value of __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets value of height.

            Returns:
                Nothing
        """

        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

            Returns:
                Calculated area
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

            Returns:
                Calculated perimeter
        """
        return 2 * (self.__width + self.__height)
