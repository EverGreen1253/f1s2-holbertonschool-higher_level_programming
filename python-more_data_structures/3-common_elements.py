#!/usr/bin/python3
def common_elements(set_1, set_2):
    """return common elements."""

    new_set = set()

    for val in set_2:
        if val in set_1:
            new_set.add(val)
    return new_set
