#!/usr/bin/python3
def element_at(my_list, idx):
    """prints the list element at the specified index."""

    if idx < 0 or idx >= len(my_list):
        return None

    return my_list[idx]
