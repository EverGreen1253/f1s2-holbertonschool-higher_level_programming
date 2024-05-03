#!/usr/bin/python3
""" Nameless module for Task 0 """

import json

def serialize_and_save_to_file(data, filename):
    """serialize_and_save_to_file

    Args:
        data: dictionary
        filename: output filename

    Returns:
        Nothing

    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename) -> dict:
    """load_and_deserialize

    Args:
        filename: input filename

    Returns:
        dictionary

    """
    data = {}
    with open(filename, 'r') as f:
        jo = json.load(f)
    for key in jo:
        data[key] = jo[key]

    return data
