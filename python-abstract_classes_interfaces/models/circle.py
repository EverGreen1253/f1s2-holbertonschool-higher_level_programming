#!/usr/bin/python3
""" Nameless module for the Circle abstract class """

import math
from models.shape import Shape


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

        return math.pi * self.radius * self.radius

    def perimeter(self) -> float:
        """overrides abstract method of area"""

        return 2 * math.pi * self.radius
