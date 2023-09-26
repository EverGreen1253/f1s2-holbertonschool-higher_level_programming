#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """return different elements."""

    common_set = set()
    new_set = set()

    for val in set_2:
        if val in set_1:
            common_set.add(val)

    for val in set_1:
        if val not in common_set:
            new_set.add(val)

    for val in set_2:
        if val not in common_set:
            new_set.add(val)

    return sorted(new_set)
