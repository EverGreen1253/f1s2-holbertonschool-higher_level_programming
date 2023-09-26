#!/usr/bin/python3
def roman_to_int(roman_string):
    """roman numeral to number"""

    if isinstance(roman_string, str) is not True or roman_string is None:
        return 0

    div = 1
    total = 0
    i = len(roman_string) - 1
    while i >= 0:
        c = roman_string[i]

        if c == 'I':
            if (i + 1) < len(roman_string):
                if roman_string[i + 1] == 'V' or roman_string[i + 1] == 'X':
                    total = total - 1
                elif roman_string[i + 1] == 'I':
                    total = total + 1
            else:
                total = total + 1
        elif c == 'V':
            total = total + 5
        elif c == 'X':
            total = total + 10
        elif c == 'L':
            total = total + 50
        elif c == 'C':
            total = total + 100
        elif c == 'D':
            total = total + 500
        elif c == 'M':
            total = total + 1000

        i = i - 1

    return total
