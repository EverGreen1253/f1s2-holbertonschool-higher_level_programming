#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x elements of list"""

    str_len = 0
    for i in my_list:
        str_len = i

    max_len = x
    if x > str_len:
        max_len = str_len

    try:
        for i in range(max_len):
            print("{0}".format(my_list[i]), end="")
        print("")
        return max_len
    except TypeError:
        return 0
