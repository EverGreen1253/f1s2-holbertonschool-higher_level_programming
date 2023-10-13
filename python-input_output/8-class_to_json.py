#!/usr/bin/python3
"""Module docstring goes here"""
import json


def class_to_json(obj):
    """Converts Class obj to JSON

    Args:
        obj (obj): the Class

    Returns:
        JSON representation of the Class

    """

    return obj.__dict__
