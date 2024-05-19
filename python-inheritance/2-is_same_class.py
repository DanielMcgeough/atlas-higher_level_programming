#!/usr/bin/python3
"""
    This module returns true if object is exactly
    an instance of the spec class, otherwise false
"""


def is_same_class(obj, a_class):
    """return ture if exact same, false if not"""
    return (type(obj) is a_class)
