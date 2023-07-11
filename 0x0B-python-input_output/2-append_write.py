#!/usr/bin/python3
"""Defines a text file-reading function."""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8)"""
    with open(filename, "a", encoding="utf-8") as file:
        num_chars_added = file.write(text)
    return num_chars_added
