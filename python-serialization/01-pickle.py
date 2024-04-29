#!/usr/bin/python3
""" Nameless module for Task 1 """

import pickle

class CustomObject:
    """CustomObject Class
    """

    name = ''
    age = 0
    is_student = False

    def __init__(self, name="", age=0, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints out class attr data
        """

        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Saves class instance into provided filename
        """
        # pass the file object into pickle.dump, not the filename
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """Loads class instance from provided filename
        """
        with open(filename, 'rb') as f:
            return pickle.load(f)
