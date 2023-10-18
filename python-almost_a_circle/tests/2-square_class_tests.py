#!/usr/bin/python3
"""Unittests for Square Class
"""
import unittest
from models.square import Square

class TestSquareClass(unittest.TestCase):

    def test_no_args(self):
        self.assertRaises(TypeError, Square)

    def test_has_args(self):
        s = Square(3)
        assert s.id > 0

    def test_has_args_and_id(self):
        s = Square(3, 0, 0, 12)
        self.assertEqual(s.id, 12)


if __name__ == '__main__':
    unittest.main()
