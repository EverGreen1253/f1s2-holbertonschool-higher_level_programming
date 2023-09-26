#!/usr/bin/python3
def max_integer(my_list=[]):
    """returns biggest number in list."""

    if len(my_list) == 0:
        return None

    biggest = None
    i = 0
    while i < len(my_list):
        if biggest is None:
            biggest = my_list[i]
        else:
            if my_list[i] > biggest:
                biggest = my_list[i]
        i = i + 1

    return biggest
