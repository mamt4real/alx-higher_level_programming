#!/usr/bin/python3
import json

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

    def to_json_string(list_dicts: list):
        """Convert to Json strings"""
        if list_dicts is None or list_dicts == []:
            return "[]"
        return json.dumps(list_dicts)

    def save_to_file(cls, lst_objs: list):
        """save instances to a file"""
        json_str = ""
        if lst_objs is None:
            json_str = "[]"
        else:
            list_dicts = [x.to_dictionary() for x in lst_objs]
            json_str = Base.to_json_string(list_dicts)
        fname = type(cls).__name__ + ".json"
        with open(fname, "w") as f:
            f.write(json_str)
