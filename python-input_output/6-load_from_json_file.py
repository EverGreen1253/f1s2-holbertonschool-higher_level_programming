#!/usr/bin/python3
"""Module docstring goes here"""
import json


def load_from_json_file(filename):
    """Read JSON data from file and create object from it

    Args:
        filename (str): the filename with the JSON data

    Returns:
        stringified version of the object data

    """

    data = ""

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            data += line

    return json.loads(data)
