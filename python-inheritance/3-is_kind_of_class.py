#!/usr/bin/python3
""" Nameless module """


def is_kind_of_class(obj, a_class):
    """returns true / false if obj is a subclass of a_class or not."""

    return issubclass(type(obj), a_class)
