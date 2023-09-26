#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in list."""

    if len(my_list) == 0:
        return None

    new_list = [None] * len(my_list)
    i = 0
    while i < len(my_list):
        new_list[i] = my_list[i] % 2 == 0
        i = i + 1

    return new_list
