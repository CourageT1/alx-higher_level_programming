#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
            Default is 0.
            y (int, optional): The y-coordinate of the square's position.
            Default is 0.
            id (int, optional): The identity of the square. Default is None.

        Raises:
            TypeError: If size is not an int.
            ValueError: If size <= 0.
            TypeError: If x or y is not an int.
            ValueError: If x or y < 0.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value <= 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the square attributes.

        Args:
            *args: Positional arguments representing attribute values.
                - 1st argument represents id attribute.
                - 2nd argument represents size attribute.
                - 3rd argument represents x attribute.
                - 4th argument represents y attribute.
            **kwargs: Keyword arguments representing attribute assignments.
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the square.

        Returns:
            dict: The dictionary representation of the square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
