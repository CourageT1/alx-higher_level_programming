#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.
    """
    if issubclass(obj.__class__, a_class) and obj.__class__ is not a_class:
        return True
    return False
