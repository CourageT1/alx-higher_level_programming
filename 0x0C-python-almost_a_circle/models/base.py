#!/usr/bin/python3
"""Defines a base model class."""
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.
        If id is provided, assigns it to the instance's id attribute.
        Otherwise, increments __nb_objects and assigns the new value to the instance's id attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to its JSON string representation.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of instances to a JSON file.

        Args:
            list_objs (list): A list of instances.

        Returns:
            None
        """
        file_name = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(file_name, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string representation to a list of dictionaries.

        Args:
            json_string (str): The JSON string representation.

        Returns:
            list: The list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with all attributes already set based on a dictionary.

        Args:
            **dictionary (dict): A dictionary containing attribute values.

        Returns:
            Base: The created instance with all attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a JSON file.

        Returns:
            list: The list of instances loaded from the file.
        """
        file_name = cls.__name__ + ".json"
        if not os.path.exists(file_name):
            return []
        with open(file_name, "r") as file:
            json_string = file.read()
        dictionaries = cls.from_json_string(json_string)
        instances = [cls.create(**dictionary) for dictionary in dictionaries]
        return instances
