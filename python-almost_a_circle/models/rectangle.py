#!/usr/bin/python3
""" Nameless module for Rectangle class """
from models.base import Base


class Rectangle(Base):
    """A Rectangle class.

    Args:
        Base class it is inheriting from

    Returns:
        Nothing

    """

    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Prints textual representation of shape dimensions.

            Returns:
                nothing
        """
        return ("[Rectangle] ({0}) {1}/{2} - {3}/{4}"
                .format(self.id, self.x, self.y, self.width, self.height))

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

        if value <= 0:
            raise ValueError("width must be > 0")

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

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Getter for private prop x

            Returns:
                value of __x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Sets value of x.

            Returns:
                Nothing
        """

        if isinstance(value, int) is not True:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Getter for private prop y

            Returns:
                value of __y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Sets value of y.

            Returns:
                Nothing
        """

        if isinstance(value, int) is not True:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Calculates the area.

            Returns:
                area value
        """
        return self.width * self.height

    def display(self):
        """Prints graphical representation of shape.

            Returns:
                nothing
        """

        for h in range(self.height):
            for w in range(self.width):
                print("#", end="")
            print("")
