#!/usr/bin/python3
"""More JSON tom-foolery"""
import json


def from_json_string(my_str):
    """Returns python obj rep of a JSON string"""
    return json.loads(my_str)
