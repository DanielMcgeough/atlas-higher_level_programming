#!/usr/bin/python3
"""
    Module that raises exception with some stuff
"""


class BaseGeometry:
    """class from earlier task no longer empty"""
    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value as an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
