#!/usr/bin/python3
"""
    This module will get dimensions of a rectangle
"""


class Rectangle(BaseGeometry):
    """a class to define a rectangle with superclass BaseGeometry"""
    def __init__(self, width, height):
        """Initialize a new Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
