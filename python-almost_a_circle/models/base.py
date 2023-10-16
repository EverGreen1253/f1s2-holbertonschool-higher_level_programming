#!/usr/bin/python3
""" Nameless module for Base class """


class Base:
    """A Base class.

    Args:
        None

    Returns:
        Nothing

    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def __str__(self):
        return self.id
