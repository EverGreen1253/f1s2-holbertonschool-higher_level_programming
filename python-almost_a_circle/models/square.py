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
        return ("[Square] ({0}) {1}/{2} - {3}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Getter for prop size

            Returns:
                value of size
        """
        return self.width

    @size.setter
    def size(self, value):
        """Sets value of size.

            Returns:
                Nothing
        """

        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the shape.

            Returns:
                nothing
        """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        elif len(kwargs) > 0:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Converts the class to a dictionary.

            Returns:
                dictionary format for the class
        """
        return (dict(id=self.id, x=self.x, size=self.width, y=self.y))
