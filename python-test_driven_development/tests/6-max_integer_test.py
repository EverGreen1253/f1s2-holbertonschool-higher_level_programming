#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_ok(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_min_ok(self):
        self.assertNotEqual(max_integer([1, 2, 3, 4]), 1)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()