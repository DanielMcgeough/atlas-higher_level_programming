#!/usr/bin/python3
"""this module defines a student class"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """inits the new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """gets a dict rep of the student"""
        return self.__dict__
