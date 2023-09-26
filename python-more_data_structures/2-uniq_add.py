#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add unique integers."""

    num = set()

    total = 0
    i = 0
    while i < len(my_list):
        if my_list[i] not in num:
            num.add(my_list[i])
            total = total + my_list[i]
        i = i + 1

    return total
