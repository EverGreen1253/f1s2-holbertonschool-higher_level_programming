#!/usr/bin/python3
""" Nameless module for Task 2 """

import sys
import csv
import json

def convert_csv_to_json(filename):
    """ does what it says """

    if not filename:
        print("Invalid filename specified!")
        sys.exit()

    try:
        with open(filename, 'r') as csvfile:
            data = []

            # manually reformatting of data
            # read_data = csv.reader(csvfile, delimiter=',', quotechar='"')
            # keys = []
            # row_index = 0
            # for row in read_data:
            #     j = {}
            #     col_index = 0
            #     for i in row:
            #         if row_index == 0:
            #             keys.append(i)
            #         else:
            #             j[keys[col_index]] = i
            #         col_index += 1
            #     row_index += 1

            #     if row_index > 1:
            #         data.append(j)

            for row in csv.DictReader(csvfile):
                data.append(row)

            with open('data.json', 'w') as f:
                json.dump(data, f)
    except FileNotFoundError:
        print("Input file {} not found".format(filename))
        sys.exit()
