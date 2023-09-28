#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x elements of list"""

    max = x
    if x > len(my_list):
        max = len(my_list)

    try:
        for i in range(max):
            print("{0}".format(my_list[i]), end="")
        print("")
        return max
    except TypeError:
        return 0
