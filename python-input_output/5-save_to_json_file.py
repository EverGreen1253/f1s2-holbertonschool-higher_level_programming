#!/usr/bin/python3
"""Module docstring goes here"""
import json


def save_to_json_file(my_obj, filename):
    """Convert to JSON string then write to file

    Args:
        my_obj (any): the data to convert to JSON

    Returns:
        Nothing

    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
