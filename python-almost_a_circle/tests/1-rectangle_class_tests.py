#!/usr/bin/python3
"""Unittests for Rectangle Class
"""
import unittest
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):

    def test_no_args(self):
        self.assertRaises(TypeError, Rectangle)

    def test_has_args(self):
        r = Rectangle(1, 3)
        assert r.id > 0

    def test_has_args_and_id(self):
        r = Rectangle(1, 3, 0, 0, 12)
        self.assertEqual(r.id, 12)


if __name__ == '__main__':
    unittest.main()
