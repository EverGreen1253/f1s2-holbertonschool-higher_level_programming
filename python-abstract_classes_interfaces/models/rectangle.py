#!/usr/bin/python3
""" Nameless module for the Rectangle abstract class """

from models.shape import Shape


class Rectangle(Shape):
    """Rectangle Class"""

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for private prop width

            Returns:
                value of __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets value of private prop width

            Returns:
                Nothing
        """
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
        """Sets value of private prop height

            Returns:
                Nothing
        """
        self.__height = value

    def area(self) -> float:
        """overrides abstract method of area"""

        return self.width * self.height

    def perimeter(self) -> float:
        """overrides abstract method of area"""

        return 2 * (self.width + self.height)
