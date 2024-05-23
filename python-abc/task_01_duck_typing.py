#!/usr/bin/python3
""" Nameless module for the Shape abstract class + its children """

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape

    Args:
        ABC

    Returns:
        Nothing

    """

    @abstractmethod
    def area(self) -> int:
        """defines area value of shape.

            Returns:
                Default 0
        """

        return 0

    @abstractmethod
    def perimeter(self) -> int:
        """defines perimeter value of shape.

            Returns:
                Default 0
        """

        return 0


class Circle(Shape):
    """Circle Class"""

    __radius = 0

    def __init__(self, radius=0):
        self.radius = radius

    @property
    def radius(self):
        """Getter for private prop radius

            Returns:
                value of __radius
        """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Sets value of private prop radius

            Returns:
                Nothing
        """
        self.__radius = value

    def area(self) -> float:
        """overrides abstract method of area"""

        area = round(math.pi * self.radius * self.radius, 2)
        print("Circle area is {:0.2f}".format(area))

        return area

    def perimeter(self) -> float:
        """overrides abstract method of area"""

        perimeter = round(2 * math.pi * self.radius, 2)
        print("Circle perimeter is {:0.2f}".format(perimeter))

        return perimeter


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

        area = round(self.width * self.height, 2)
        print("Rectangle area is {:0.2f}".format(area))

        return area

    def perimeter(self) -> float:
        """overrides abstract method of area"""

        perimeter = round(2 * (self.width + self.height), 2)
        print("Rectangle perimeter is {:0.2f}".format(perimeter))

        return perimeter


def shape_info(shape :Shape):
    """general function"""

    area :float = shape.area()
    perimeter :float = shape.perimeter()

    return {'area': area, 'perimeter': perimeter }
