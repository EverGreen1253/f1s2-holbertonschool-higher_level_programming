#!/usr/bin/python3
"""Unittests for Base Class
"""
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):

    def test_id_selfgen(self):
        b = Base()
        assert b.id > 0

    def test_id_specified(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

if __name__ == '__main__':
    unittest.main()
