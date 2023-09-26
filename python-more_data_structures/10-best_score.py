#!/usr/bin/python3
def best_score(a_dictionary):
    """get largest value's key"""

    if a_dictionary is None:
        return None

    wanted = None
    largest = None
    for key, val in a_dictionary.items():
        if largest is None:
            largest = val
            wanted = key
        elif val > largest:
            largest = val
            wanted = key

    return wanted
