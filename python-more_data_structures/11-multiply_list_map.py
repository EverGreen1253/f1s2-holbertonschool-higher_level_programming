#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """multiply everything using map"""

    if len(my_list) == 0:
        return []

    return list(map(lambda x: x * 2, my_list))
