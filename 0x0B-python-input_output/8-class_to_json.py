#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary representation of the object with simple data structure.

    Note:
        This implementation assumes that all attributes of the object are serializable: list, dictionary, string, integer, and boolean.
        No module imports are allowed.
    """
    attributes = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            attributes[attr] = value
    return attributes
