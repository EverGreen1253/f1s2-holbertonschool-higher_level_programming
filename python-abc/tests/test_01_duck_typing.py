#!/usr/bin/python3
"""Unittests for Shape Class
"""
import unittest
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

    def test_circle_negative_radius(self):
        """Tests that Circle will throw an error for negative radius values
        """

        self.assertRaises(ValueError, Circle, -5)

    def test_rectangle_negative_dimensions(self):
        """Tests that Rectangle will throw an error for negative height / width values
        """

        self.assertRaises(ValueError, Rectangle, -2, 3)



if __name__ == '__main__':
    unittest.main()
