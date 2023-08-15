#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import os
import turtle


class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base instance.
        If id is provided, assigns it to the instance's id attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to its JSON string representation.

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
        """Saves a list of instances to a JSON file.

        Args:
            list_objs (list): A list of instances.

        Returns:
            None
        """
        file_name = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        json_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(json_list)
        with open(file_name, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string representation to a list of dictionaries.

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
        """Creates instance with attributes already set based on dictionary.

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
        """Loads a list of instances from a JSON file.

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of instances to a CSV file.

        Args:
            list_objs (list): A list of instances.

        Returns:
            None
        """
        file_name = cls.__name__ + ".csv"
        if list_objs is None:
            list_objs = []
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                row = obj.to_csv_row()
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of instances from a CSV file.

        Returns:
            list: The list of instances loaded from the file.
        """
        file_name = cls.__name__ + ".csv"
        if not os.path.exists(file_name):
            return []
        instances = []
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                dictionary = cls.from_csv_row(row)
                instance = cls.create(**dictionary)
                instances.append(instance)
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares.

        Args:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.

        Returns:
            None
        """
        screen = turtle.Screen()
        screen.title("Rectangles and Squares")
        screen.bgcolor("white")
        screen.setup(width=800, height=600)

        pen = turtle.Turtle()
        pen.speed(2)

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.color("red")
            for _ in range(2):
                pen.forward(rect.width)
                pen.right(90)
                pen.forward(rect.height)
                pen.right(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("blue")
            for _ in range(4):
                pen.forward(square.size)
                pen.right(90)

        turtle.done()
