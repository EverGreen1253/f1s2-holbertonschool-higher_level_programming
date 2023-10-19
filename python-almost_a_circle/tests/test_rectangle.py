#!/usr/bin/python3
"""Unittests for Rectangle Class
"""
from io import StringIO
import sys
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
        self.assertEqual(r.height, 2)

    def test_instantiate_three_args(self):
        """Tests when three args passed in creating Rect instance
        """
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_instantiate_four_args(self):
        """Tests when four args passed in creating Rect instance
        """
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

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

    def test_negative_width(self):
        """Tests when the width value is neg when creating Rect instance
        """
        self.assertRaises(ValueError, Rectangle, -1, 2)

    def test_negative_height(self):
        """Tests when the height value is neg when creating Rect instance
        """
        self.assertRaises(ValueError, Rectangle, 1, -2)

    def test_zero_width(self):
        """Tests when the width value is 0 when creating Rect instance
        """
        self.assertRaises(ValueError, Rectangle, 0, 2)

    def test_zero_height(self):
        """Tests when the height value is 0 when creating Rect instance
        """
        self.assertRaises(ValueError, Rectangle, 1, 0)

    def test_neg_x_offset(self):
        """Tests when the x offset value is neg when creating Rect instance
        """
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)

    def test_neg_y_offset(self):
        """Tests when the y offset value is neg when creating Rect instance
        """
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

    def test_area_non_zero(self):
        """Tests that the instance's calculated area is non-zero
        """
        r = Rectangle(2, 5)
        self.assertEqual(r.area(), 10)

    def test_printable(self):
        """Tests that the instance can be stringified
        """
        r = Rectangle(2, 5, 0, 0, 25)
        self.assertEqual(r.__str__(), "[Rectangle] (25) 0/0 - 2/5")

    def test_display_no_x_and_y_offset(self):
        """Tests that the graphical representation prints out correctly
        """
        r = Rectangle(2, 2)
        capturedOutput = StringIO()     # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        r.display()                     # Call unchanged function.
        sys.stdout = sys.__stdout__     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), "##\n##\n")

    def test_display_x_offset_only(self):
        """Tests that the graphical representation prints out correctly
        """
        r = Rectangle(2, 2, 1)
        capturedOutput = StringIO()     # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        r.display()                     # Call unchanged function.
        sys.stdout = sys.__stdout__     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), " ##\n ##\n")


if __name__ == '__main__':
    unittest.main()
