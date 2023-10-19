#!/usr/bin/python3
"""Unittests for Rectangle Class
"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test functions for Rectanlge Class
    """

    def test_instantiate_no_args(self):
        """Tests error thrown when no args used in creating Rect instance
        """
        self.assertRaises(TypeError, Rectangle)

    def test_instantiate_two_args(self):
        """Tests when two args passed in creating Rect instance
        """
        r = Rectangle(1, 2)
        self.assertIsNotNone(r)

    def test_instantiate_three_args(self):
        """Tests when three args passed in creating Rect instance
        """
        r = Rectangle(1, 2, 3)
        self.assertIsNotNone(r)

    def test_instantiate_four_args(self):
        """Tests when four args passed in creating Rect instance
        """
        r = Rectangle(1, 2, 3, 4)
        self.assertIsNotNone(r)

    def test_instantiate_all_args(self):
        """Tests when four args passed in creating Rect instance
        """
        r = Rectangle(1, 2, 0, 0, 15)
        self.assertIsNotNone(r)
        self.assertEqual(r.id, 15)

    def test_instantiate_string_first_arg(self):
        """Tests when the width is str instead of int when creating Rect instance
        """
        self.assertRaises(TypeError, Rectangle, "1", 2)

    def test_instantiate_string_second_arg(self):
        """Tests when the height is str instead of int when creating Rect instance
        """
        self.assertRaises(TypeError, Rectangle, 1, "2")

    def test_instantiate_string_third_arg(self):
        """Tests when the x offset is str instead of int when creating Rect instance
        """
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")

    def test_instantiate_string_fourth_arg(self):
        """Tests when the y offset is str instead of int when creating Rect instance
        """
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")

if __name__ == '__main__':
    unittest.main()
