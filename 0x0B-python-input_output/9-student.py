#!/usr/bin/python3
"""Defines a class Student."""

class Student:
    """represent a student"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the given first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        attributes = {}
        for attr, value in self.__dict__.items():
            attributes[attr] = value
        return attributes
