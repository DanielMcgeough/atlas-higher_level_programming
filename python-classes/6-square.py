#!/usr/bin/python3

"""Module defines geometric class Square."""


class Square:
    """Class represents a square.

    Attributes:
        size (int): length of each side.
        position (tuple): position of new square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize new Square instance."""
        self.size = size
        self.position - position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)
    
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers.")
        self.__position = value

    def area(self):
        """Method calculates the area of new instance Square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Method prints instance of Square represented by '#'."""
        if self.__size == 0:
            print("")
            return
            
    [print("") for i in range(0, self.__position[1])]
    for i in range(0, self.__size):
        [print(" ", end="") for j in range(0, self.__position[0])]
        [print("#", end="") for k in range(0, self.__size)]
        print("")