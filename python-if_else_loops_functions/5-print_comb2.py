#!/usr/bin/python3
for x in range(0, 100):
    print('{0:02d}'.format(x), end="")
    if x != 99:
        print(", ", end="")
    else:
        print("")
