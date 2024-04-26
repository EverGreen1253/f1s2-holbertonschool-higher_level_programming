#!/usr/bin/python3
""" Nameless module for the Shape abstract class """

from abc import ABC, abstractmethod


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
