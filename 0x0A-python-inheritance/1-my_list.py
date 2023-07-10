#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    def print_sorted(self):
        """
        Prints the original list, the sorted list in ascending order, and the original list again.
        Assumes that all elements of the list are of type int.
        """
        sorted_list = sorted(self)
        print(sorted_list)
