#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # print(sys.argv)
    count = len(sys.argv) - 1

    if count == 0:
        print("0")
    else:
        total = 0
        for x in range(1, count + 1):
            total = total + int(sys.argv[x])

        print('{0}'.format(total))
