#!/usr/bin/python3
"""this module defines a JSON-file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an obj to a text file using JSON format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
