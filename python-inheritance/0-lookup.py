#!/usr/bin/python3
def lookup(obj):
    """returns a list of available attrs and methods for obj."""

    mylist = []

    mylist = mylist + dir(obj)

    return mylist
