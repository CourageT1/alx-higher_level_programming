#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("Type exception raised")
    except TypeError as error:
        raise error
