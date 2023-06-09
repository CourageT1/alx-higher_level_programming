#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    lines = []
    line = ""

    for char in text:
        line += char
        if char in punctuations:
            lines.append(line.strip())
            line = ""

    lines.append(line.strip())

    for line in lines:
        print(line)
        print()
