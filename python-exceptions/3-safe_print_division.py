#!/usr/bin/python3
def safe_print_division(a, b):
    """divides a by b"""
    if b == 0:
        print ("Inside result: None")
        return None

    try:
        result = a / b
        print ("Inside result: {0}".format(result))
        return result
    except:
        raise
