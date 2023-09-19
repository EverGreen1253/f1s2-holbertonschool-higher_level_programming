#!/usr/bin/python3
def pow(a, b):
    """return nth power result"""
    if b == 0:
        return 1
    elif b < 0:
        c = 1 / a
        for x in range((b * -1) - 1):
            c = c * 1 / a

        if 'e' in str(c):
            return "{0:.15e}".format(c)
        return c
    else:
        c = a
        for x in range(b - 1):
            c = c * a

        if 'e' in str(c):
            return "{0:.15e}".format(c)
        return c

    return None
