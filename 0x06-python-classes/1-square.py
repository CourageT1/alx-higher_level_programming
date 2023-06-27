#!/usr/bin/python3
class Square:
    """Represent a square."""

    def __init__(self, size):
        self.__size = size

    def get_area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def get_perimeter(self):
        """Calculate the perimeter of the square."""
        return 4 * self.__size

    def get_size(self):
        """Get the size of the square."""
        return self.__size

    def set_size(self, new_size):
        """Set the size of the square."""
        self.__size = new_siz
