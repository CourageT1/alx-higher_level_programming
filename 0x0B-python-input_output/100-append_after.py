#!/usr/bin/python3
"""Defines a text file insertion function."""

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text into a file after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to be inserted after each matching line.
    """
    temp_filename = filename + ".tmp"
    with open(filename, "r") as file, open(temp_filename, "w") as temp_file:
        for line in file:
            temp_file.write(line)
            if search_string in line:
                temp_file.write(new_string + "\n")
