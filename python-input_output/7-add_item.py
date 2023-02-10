#!/usr/bin/python3
"""
contains a script that adds all arguments to
a python list, and then save them to a file
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    content = load_from_json_file(filename)
except FileNotFoundError:
    content = []

save_to_json_file(content + argv[1:], filename)
