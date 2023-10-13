#!/usr/bin/python3
"""Module docstring goes here"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

data = []
if os.path.isfile(filename) is True:
    data = load_from_json_file(filename)

for i in range(1, len(sys.argv)):
    data.append(sys.argv[i])

save_to_json_file(data, filename)
