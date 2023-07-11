#!/usr/bin/python3
"""Defines a text file line-counting function."""

def write_file(filename="", text=""):
    """Return the number of lines in a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        num_chars_written = file.write(text)
    return num_chars_written
