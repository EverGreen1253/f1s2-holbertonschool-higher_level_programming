#!/usr/bin/python3
def safe_print_division(a, b):
    """divides a by b"""

    result = None
    try:
        if b == 0:
            print("Inside result: None")
        else:
            result = a / b
            print("Inside result: {0}".format(result))
    except ValueError:
        raise
    finally:
        return result
