#!/usr/bin/python3
import unittest
from models.base import Base


import unittest

class TestBase(unittest.TestCase):

    def setUp(self):
        # Resetting the _id_counter before each test
        Base._id_counter = 1

    def test_auto_id_assignment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id_assignment(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_mixed_id_assignment(self):
        b1 = Base()
        b2 = Base(10)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 10)
        self.assertEqual(b3.id, 2)

if __name__ == '__main__':
    unittest.main()