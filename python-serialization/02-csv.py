#!/usr/bin/python3
""" Nameless module for Task 2 """

import csv
import json

def convert_csv_to_json(filename):
    """ does what it says """

    # FIXME:

    with open(filename, 'w') as f:
        json.dump(data, f)
