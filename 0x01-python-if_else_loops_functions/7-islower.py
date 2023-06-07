#!/usr/bin/python3
def islower(c):
    if len(c) != 1:
        raise ValueError("Input must be a single character")

    return ord('a') <= ord(c) <= ord('z')
