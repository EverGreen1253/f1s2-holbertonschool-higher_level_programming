#!/usr/bin/python3
"""Unittests for Base Class
"""
import unittest
from scripts.task_1 import Circle, Rectangle, shape_info


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

        self.assertEqual(c_info['area'], 78.54)
        self.assertEqual(c_info['perimeter'], 31.42)

        self.assertEqual(r_info['area'], 6.00)
        self.assertEqual(r_info['perimeter'], 10.00)


if __name__ == '__main__':
    unittest.main()
