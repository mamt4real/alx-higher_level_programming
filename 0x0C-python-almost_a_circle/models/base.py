#!/usr/bin/python3

"""Defines the base model for all our classes"""


class Base:

    """The Base model for all our classes
    It manages creation of id"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def validate_size(self, name, val, low=1):
        if not isinstance(val, int):
            raise TypeError(f"{name} must be an integer")
        if val < low:
            op = ">" if low else ">="
            raise ValueError(f"{name} must be {op} {low}")
