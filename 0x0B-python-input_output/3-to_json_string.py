#!/usr/bin/python3
""" returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """
    Converts an object (string) to its JSON representation.

    Args:
        my_obj (str): The object (string) to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
