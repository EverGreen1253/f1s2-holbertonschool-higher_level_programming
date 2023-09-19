#!/usr/bin/python3
def fizzbuzz():
    """return nth power result"""
    for x in range(1, 101):
        n = x

        if x % 15 == 0:
            print("FizzBuzz ", end="")
        elif x % 3 == 0:
            print("Fizz ", end="")
        elif x % 5 == 0:
            print("Buzz ", end="")
        else:
            print('{0} '.format(n), end="")
