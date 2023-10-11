#!/usr/bin/python3
""" Nameless module containing Rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry Class.
    """

    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calculates area of the Rectangle

            Returns:
                Area
        """

        return self.__width * self.__height

    def __str__(self):
        """Stringify the graphical representation of the rect.

            Returns:
                String describing rectangle's dimensions
        """

        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
