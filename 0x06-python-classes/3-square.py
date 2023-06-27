#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initializes a square with the given size.

        Args:
            size (int): The size of the square (default 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
