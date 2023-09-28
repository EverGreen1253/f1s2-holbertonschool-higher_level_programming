#!/usr/bin/python3
def safe_print_integer(value):
    """prints value if integer"""

    try:
        if value - value == 0:
            print("{:d}".format(value))
            return True
        else:
            return False
    except TypeError:
        return False
