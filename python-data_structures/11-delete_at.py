#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """deletes item at specified index."""

    if len(my_list) == 0 or idx < 0 or idx > len(my_list) - 1:
        return my_list

    del my_list[idx]
    return my_list
