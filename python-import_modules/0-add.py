#!/usr/bin/python3
if __name__ == "__main__":
    add = __import__('add_0').add

    a = 1
    b = 2
    c = add(a, b)
    print('{0} + {1} = {2}'.format(a, b, c))
