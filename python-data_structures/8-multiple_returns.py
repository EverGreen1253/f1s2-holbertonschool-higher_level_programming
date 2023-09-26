#!/usr/bin/python3
def multiple_returns(sentence):
    """returns a tuple with string length and first char."""

    str_length = 0
    first_char = None
    if sentence != '':
        str_list = list(sentence)
        str_length = len(str_list)
        first_char = str_list[0]

    return (str_length, first_char)
