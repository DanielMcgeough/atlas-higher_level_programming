#!/usr/bin/python3
"""
    This module returns true if obj is instance of
    false if it is not.
"""


def is_kind_of_class(obj, a_class):
    """this module returns true if obj is instance
    or a class that the class inherits from
    """
    return (isinstance(obj, a_class))
