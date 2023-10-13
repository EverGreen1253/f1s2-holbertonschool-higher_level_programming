#!/usr/bin/python3
"""Module docstring goes here"""
import json


def to_json_string(my_obj):
    """Convert to JSON string

    Args:
        my_obj (any): the data to convert to JSON

    Returns:
        (str) the converted JSON string

    """

    return json.dumps(my_obj)
