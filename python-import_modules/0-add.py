#!/usr/bin/python3
if __name__ == "__main__":
    import add_0 as add_module

    a = 1
    b = 2
    c = add_module.add(a, b)
    print('{0} + {1} = {2}'.format(a, b, c))
