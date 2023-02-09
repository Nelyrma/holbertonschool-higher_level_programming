#!/usr/bin/python3
"""JSON representation"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object"""
    obj = json.dumps(my_obj)
    return obj
