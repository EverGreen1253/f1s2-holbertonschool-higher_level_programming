#!/usr/bin/python3
for x in range(0, 9):
    for y in range(x + 1, 10):
        if (x != 8 or y != 9):
            print('{0:02d}, '.format((x * 10 + y)), end="")
        else:
            print('{0:02d}'.format((x * 10 + y)))
