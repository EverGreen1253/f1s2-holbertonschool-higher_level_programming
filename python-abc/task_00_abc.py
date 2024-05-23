#!/usr/bin/python3
""" Nameless module for the Animal class """

from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal

    Args:
        ABC

    Returns:
        Nothing

    """

    @abstractmethod
    def sound(self) -> str:
        """defines sound made by animal.

            Returns:
                Nothing
        """

        return ""


class Dog(Animal):
    """Dog Class"""

    def sound(self) -> str:
        """overrides abstract method of Animal"""

        return "Bark"


class Cat(Animal):
    """Cat Class"""

    def sound(self) -> str:
        """overrides abstract method of Animal"""

        return "Meow"
