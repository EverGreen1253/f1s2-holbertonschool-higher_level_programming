#!/usr/bin/python3
""" test import """

def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

# example to demonstrate how imports will skip the __name__ == "__main__"
if __name__ == "__main__":
    print("hi there!")
