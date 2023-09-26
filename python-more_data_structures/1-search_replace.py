#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Search and destroy."""

    if len(my_list) == 0:
        return None

    new_list = [None] * len(my_list)

    i = 0
    while i < len(my_list):
        if my_list[i] == search:
            new_list[i] = replace
        else:
            new_list[i] = my_list[i]
        i = i + 1

    return new_list
