#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints everything in the list in reverse."""
    if mylist == None or len(my_list) == 0:
        return None

    i = len(my_list) - 1
    while i >= 0:
        print("{:d}".format(my_list[i]))
        i = i - 1
