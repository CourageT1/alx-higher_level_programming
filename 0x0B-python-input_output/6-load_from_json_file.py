#!/usr/bin/python3
"""Defines an Object from a “JSON file”:"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    Args:
        filename: The name of the JSON file.
    Returns:
        The object created from the JSON file.
    Note:
        This implementation uses the `json` module for JSON deserialization.
        If the JSON string does not represent a valid object, no exception handling is performed.
        File permission and exceptions are not managed.
    """
    with open(filename, "r") as file:
        obj = json.load(file)
    return obj
