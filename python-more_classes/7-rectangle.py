#!/usr/bin/python3
""" Nameless module for Rectangle class """


class Rectangle:
    """A rectangle.

    Args:
        None

    Returns:
        Nothing

    """

    number_of_instances = 0
    print_symbol = "#"

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

        if value < 0:
            raise ValueError("width must be >= 0")

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

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

            Returns:
                Calculated area
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

            Returns:
                Calculated perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Stringify the graphical representation of the rect.

            Returns:
                printable string of rectangle shape
        """
        s = ""

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                s = s + str(self.print_symbol)

            if i != self.__height - 1:
                s = s + ("\n")

        return s

    def __repr__(self):
        """Generate a command to create duplicate Rectangle.

            Returns:
                command to instantiate new Rectangle
        """
        s = "Rectangle({0}, {1})".format(self.__width, self.__height)

        return s

    def __del__(self):
        """Destructor method for Rectangle

            Returns:
                printed string to indicate instance destruction
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
