#!/usr/bin/python3
"""Unittests for Shape Class
"""
import unittest
import sys, io
from task_01_duck_typing import Circle, Rectangle, shape_info


class TestShape(unittest.TestCase):
    """Test functions for Shape Class
    """
    def test_shape_info(self):
        """Tests that shape info works as expected for Circle and Rectangle
        """
        c = Circle(5)
        r = Rectangle(2, 3)

        c_info = shape_info(c)
        r_info = shape_info(r)

        self.assertEqual(c_info['area'], 78.53981633974483)
        self.assertEqual(c_info['perimeter'], 31.41592653589793)

        self.assertEqual(r_info['area'], 6.00)
        self.assertEqual(r_info['perimeter'], 10.00)

    def test_circle_negative(self):
        """Test Circle with negative radius."""
        circle_negative = Circle(radius=-5)
        assert abs(circle_negative.area() - 78.53981633974483) < 1e-5, "Area should handle negative radius"
        assert abs(circle_negative.perimeter() - 31.41592653589793) < 1e-5, "Perimeter should handle negative radius"

    def test_rectangle_negative(self):
        """Test Rectangle with negative dimensions."""
        rectangle_negative = Rectangle(width=-4, height=7)
        assert rectangle_negative.area() == -28, "Area should handle negative dimensions"
        assert rectangle_negative.perimeter() == 6, "Incorrect perimeter for negative dimensions"

    def test_shape_info_2(self):
        """Test shape_info function."""
        circle = Circle(radius=5)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        shape_info(circle)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        assert "Area: 78.5" in output, "Incorrect area output in shape_info"
        assert "Perimeter: 31.4" in output, "Incorrect perimeter output in shape_info"



if __name__ == '__main__':
    unittest.main()
