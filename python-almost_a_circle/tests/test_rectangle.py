#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
        This module defines test methods for the object class Base.
        finally we get to use unittests instead of those stupid doc ones.
    """

    def test_Rectangle_id(self):
        """id is working correctly."""
        r1 = Rectangle(2, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)
        r2 = Rectangle(1, 2, 0, 0, None)
        r3 = Rectangle(2, 1, 0, 0, None)
        self.assertEqual(r2.id, 3)
        self.assertEqual(r3.id, 4)
    
    def test_Rectangle_id_type(self):
        """id is of type int."""
        r = Rectangle(1, 2, 0, 0, 1000)
        r1 = Rectangle(2, 1, 0, 0)
        self.assertIsInstance(r.id, int)
        self.assertIsInstance(r1.id, int)

    def test_Rectangle_height(self):
        """height is of type int."""
        r = Rectangle(1, 2, 0, 0)
        self.assertEqual(r.height, 2)
        r1 = Rectangle(1, "2", 0, 0)
        self.assertRaises(TypeError)

    def test_Rectangle_width(self):
        """width is of type int."""
        r = Rectangle(3, 2)
        self.assertEqual(r.width, 3)
        r1 = Rectangle("3", 1)
        self.assertRaises(TypeError)

    def test_Rectangle_x(self):
        """x is of type int."""
        r = Rectangle(1, 1, 12)
        self.assertEqual(r.x, 12)
        r1 = Rectangle(2, 2, "12")
        self.assertRaises(TypeError)
        r2 = Rectangle(3, 1)
        self.assertEqual(r2.x, 0)

    def test_Rectangle_y(self):
        """y is of type int."""
        r = Rectangle(1, 1, 0, 4)
        self.assertEqual(r.y, 4)
        r1 = Rectangle(2, 1, 0, "4")
        self.assertRaises(TypeError)
        r2 = Rectangle(2, 3)
        self.assertEqual(r2.y, 0)
