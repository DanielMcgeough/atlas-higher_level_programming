#!/usr/bin/python3
"""
    This module will return tur if the object is
    an instance of a class that inherited from the
    specifie class, another boolean.
"""


def inherits_from(obj, a_class):
    """
    returns true if an instance, otherwise it will
    return false
    """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
