#!/usr/bin/python3
"""function that writes an object to a text file"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file using JSON repre"""
    with open("filename.json", "w") as f:
        json.dump(my_obj, f)
