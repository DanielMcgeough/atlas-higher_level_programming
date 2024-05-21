#!/usr/bin/python3
"""this module defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Creates a python obj from a JSON file"""
    with open(filename) as f:
        return json.load(f)
