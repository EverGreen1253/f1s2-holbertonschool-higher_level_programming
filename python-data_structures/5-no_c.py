#!/usr/bin/python3
def no_c(my_string):
    """removes c or C from the string."""

    my_list = list(my_string)

    stop = 0
    while stop == 0:
        try:
            my_list.remove('c')
        except ValueError:
            stop = 1

    stop = 0
    while stop == 0:
        try:
            my_list.remove('C')
        except ValueError:
            stop = 1

    my_new_string = ""
    for c in my_list:
        my_new_string += c

    return my_new_string
