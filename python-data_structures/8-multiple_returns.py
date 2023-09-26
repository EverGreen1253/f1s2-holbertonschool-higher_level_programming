#!/usr/bin/python3
def multiple_returns(sentence):
    """returns a tuple with string length and first char."""

    l = 0
    c = None
    if sentence != '':
        str_list = list(sentence)
        l = len(str_list)
        c = str_list[0]

    return (l, c)
