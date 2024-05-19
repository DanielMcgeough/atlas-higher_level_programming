#!/usr/bin/python3
"""
    This module will print a list of ints in asc order
"""


class MyList(list):
    """A class that inherits from super class list"""
    def print_sorted(self):
        """prints a sorted list in asc"""
        print(sorted(self))
