#!/usr/bin/python3
"""JSON representation"""

import json


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    string = json.loads(my_str)
    return string
