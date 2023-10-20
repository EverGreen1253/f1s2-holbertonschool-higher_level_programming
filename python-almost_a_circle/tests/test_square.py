#!/usr/bin/python3
"""Unittests for Square Class
"""
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_no_args(self):
        """Tests initialising Square with no args
        """
        self.assertRaises(TypeError, Square)

    def test_init_with_size(self):
        """Tests initialising Square with size
        """
        s = Square(3)
        self.assertEqual(s.size, 3)

    def test_init_with_size_and_x(self):
        """Tests initialising Square with size and x
        """
        s = Square(3, 5)
        self.assertEqual(s.x, 5)

    def test_init_with_size_x_and_y(self):
        """Tests initialising Square with size, x and y
        """
        s = Square(3, 5, 10)
        self.assertEqual(s.y, 10)

    def test_init_with_size_string(self):
        """Tests initialising Square with string size
        """
        self.assertRaises(TypeError, Square, "10")

    def test_init_with_x_string(self):
        """Tests initialising Square with string x offset
        """
        self.assertRaises(TypeError, Square, 5, "10")

    def test_init_with_y_string(self):
        """Tests initialising Square with string y offset
        """
        self.assertRaises(TypeError, Square, 5, 10, "10")

    def test_init_with_negative_size(self):
        """Tests initialising Square with negative size
        """
        self.assertRaises(ValueError, Square, -1)

    def test_init_with_negative_x(self):
        """Tests initialising Square with negative x
        """
        self.assertRaises(ValueError, Square, 5, -1)

    def test_init_with_negative_y(self):
        """Tests initialising Square with negative y
        """
        self.assertRaises(ValueError, Square, 5, 1, -1)

    def test_init_with_zero_size(self):
        """Tests initialising Square with zero size
        """
        self.assertRaises(ValueError, Square, 0)


if __name__ == '__main__':
    unittest.main()
