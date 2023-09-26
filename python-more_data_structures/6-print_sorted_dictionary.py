#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """return sorted dict items"""

    sorted_keys = sorted(list(a_dictionary))

    i = 0
    while i < len(sorted_keys):
        print("{0}: {1}".format(sorted_keys[i], a_dictionary[sorted_keys[i]]))
        i = i + 1
