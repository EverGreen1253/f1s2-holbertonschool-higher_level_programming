#!/usr/bin/python3
""" Module for Student class """


class Student:
    """A Student.

    Args:
        first_name (str): first name
        last_name (str): last name
        age (int): age

    Attributes:
        first_name (str): first name
        last_name (str): last name
        age (int): age

    """

    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """gets dict of square.

            Returns:
                str: json version of class dict
        """

        dict = self.__dict__
        filtered = {}
        if attrs is not None:
            for key in dict:
                if key in attrs:
                    filtered[key] = dict[key]
        else:
            filtered = dict

        return filtered
