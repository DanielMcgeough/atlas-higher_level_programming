#!/usr/bin/python3
"""This module adds two integers called
a and b together"""


def add_integer(a, b=98):
    """
    Returns the sum of two ints or floats as an int

    Args:
        a: first argument
        b: second argument

    Returns:
        sum of a and b or both arguments

    Raises:
        TypeError: if either of args or not an
        int or float throws error
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
