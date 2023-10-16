#!/usr/bin/python3
""" Nameless module for Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class.

    Args:
        size (int): the size
        x (int): the x offset
        y (int): the y offset
        id (int): the id

    Returns:
        Nothing
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints textual representation of shape dimensions.

            Returns:
                nothing
        """
        return ("[Square] ({0}) {1}/{2} - {3}/{4}"
                .format(self.id, self.x, self.y, self.width, self.width))
