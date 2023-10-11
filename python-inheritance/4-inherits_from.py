#!/usr/bin/python3
""" Nameless module """


def inherits_from(obj, a_class):
    """returns true / false if obj inherits from a_class or not."""

    return issubclass(type(obj), a_class) and type(obj) != a_class
