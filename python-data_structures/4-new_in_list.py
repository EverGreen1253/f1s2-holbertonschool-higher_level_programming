#!/usr/bin/python3

import copy

def new_in_list(my_list, idx, element):
    """replaces the list element at the specified index."""

    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = copy.copy(my_list)

    new_list[idx] = element
    return new_list
