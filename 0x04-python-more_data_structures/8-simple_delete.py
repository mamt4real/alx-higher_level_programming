#!/usr/bin/python3

def simple_delete(a_dict, key=""):
    """
    removes a key in a dict
    """
    if a_dict is None:
        return None
    if key:
        del a_dict[key]
    return a_dict
