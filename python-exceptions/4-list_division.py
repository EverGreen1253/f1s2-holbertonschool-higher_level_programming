#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """divides corresponding elems in the 2 lists"""

    str_len_1 = len(my_list_1)
    str_len_2 = len(my_list_2)

    new_list = []

    for i in range(list_length):
        val = 0

        try:
            if i >= str_len_1 or i >= str_len_2:
                raise IndexError

            t_1 = type(my_list_1[i])
            t_2 = type(my_list_2[i])

            if ((t_1 is not int and t_1 is not float)
                or (t_2 is not int and t_2 is not float)):
                raise TypeError
            elif my_list_2[i] == 0:
                raise ValueError
            else:
                val = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ValueError:
            print("division by 0")
        finally:
            new_list.append(val)

    return new_list
