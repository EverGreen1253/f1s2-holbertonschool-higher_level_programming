#!/usr/bin/python3
""" Nameless module for extending the List built-in class """


class VerboseList(list):
    """VerboseList

    Args:
        list

    Returns:
        Nothing

    """

    def __init__(self, items):
        super().__init__(items)

    def append(self, item):
        super().append(item)
        print("Added {0} to the list.".format(item))

    def extend(self, items):
        super().extend(items)
        count = sum(1 for _ in items)
        print("Extended the list with {0} items.".format(count))

    def remove(self, item):
        print("Removed {0} from the list.".format(item))
        super().remove(item)

    def pop(self, index = None):
        if index is None:
            index = len(super()) - 1

        print("Popped {0} from the list.".format(index))
        super().pop(index)
