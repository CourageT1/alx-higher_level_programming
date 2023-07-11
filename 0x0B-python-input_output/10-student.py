#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the given first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to be retrieved (optional).

        Returns:
            dict: The dictionary representation of the Student instance.

        Note:
            If `attrs` is provided, only the attributes in the list will be included in the dictionary representation.
            If `attrs` is not provided or is None, all attributes will be included.
        """
        if attrs is None:
            return self.__dict__

        attributes = {}
        for attr in attrs:
            if hasattr(self, attr):
                attributes[attr] = getattr(self, attr)
        return attributes
