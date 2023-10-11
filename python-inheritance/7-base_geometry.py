#!/usr/bin/python3
""" Nameless module containing BaseGeometry class """


class BaseGeometry():
    """BaseGeometry Class.
    """

    def area(self):
        """returns area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""

        if type(value) is not int:
            raise TypeError("{0} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{0} must be greater than 0".format(name))
