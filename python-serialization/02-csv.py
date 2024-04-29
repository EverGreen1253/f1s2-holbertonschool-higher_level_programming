#!/usr/bin/python3
""" Nameless module for Task 2 """

import csv
import json

def convert_csv_to_json(filename):
    """ does what it says """

    with open('data.csv', newline='') as csvfile:
        read_data = csv.reader(csvfile, delimiter=',', quotechar='"')

        keys = []
        data = []
        row_index = 0
        for row in read_data:
            j = {}
            col_index = 0
            for i in row:
                if row_index == 0:
                    keys.append(i)
                else:
                    j[keys[col_index]] = i
                col_index += 1
            row_index += 1

            if row_index > 1:
                data.append(j)

        with open('data.json', 'w') as f:
            json.dump(data, f)
