#!/usr/bin/python3
Square = __import__('0-square').Square
# doc = __import__('0-square').__doc__
# print(doc)

my_square = Square()
print(type(my_square))
print(my_square.__dict__)