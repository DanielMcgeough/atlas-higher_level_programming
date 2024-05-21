#!/usr/bin/python3
"""This module defines a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """returns JSON reppresentation of a string obj"""
    return json.dumps(my_obj)
