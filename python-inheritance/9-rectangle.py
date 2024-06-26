#!/usr/bin/python3"
"""Defines a class Rectangle that inherits from BaseGeomtery"""
BaseGeomtery = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeomtery):
    """this class represents a Rectangle with superclass BaseGeomtery"""

    def __init__(self, width, height):
        """initialize a new rectangle"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the print() and str() representation of a Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
