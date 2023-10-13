#!/usr/bin/python3
"""Module docstring goes here"""
import json


def from_json_string(my_str):
    """Convert from JSON string

    Args:
        my_str (str): the string to convert from JSON

    Returns:
        (obj) the JSON object

    """

    return json.loads(my_str)
