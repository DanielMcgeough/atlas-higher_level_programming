#!/usr/bin/python3
"""a class that defines a rectangle"""


class Rectangle:
    """Its a class that represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing the class
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        Raises:
            TypeError: if size is not an integers
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width attribute"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__hieght = value
