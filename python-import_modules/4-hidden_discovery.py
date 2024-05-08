#!/usr/bin/python3.10

# Note the shebage uses python 3.10 as the hidden_4 binary is compiled in python 3.10
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)

    for x in range(len(names)):
        if (names[x][0] != '_' or names[x][1] != '_'):
            print(names[x])
