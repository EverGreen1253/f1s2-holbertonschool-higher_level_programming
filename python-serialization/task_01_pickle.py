#!/usr/bin/python3
""" Nameless module for Task 1 """

import sys
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
        if not filename:
            print("Invalid filename specified!")
            sys.exit()

        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except FileNotFoundError:
            print("Specified file not found!")

    @classmethod
    def deserialize(cls, filename):
        """Loads class instance from provided filename
        """
        # pass the file object into pickle.load, not the filename

        if not filename:
            print("Invalid filename specified!")
            sys.exit()

        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        # except FileNotFoundError:
        except Exception:
            print("Specified file not found!")
        
        return None
