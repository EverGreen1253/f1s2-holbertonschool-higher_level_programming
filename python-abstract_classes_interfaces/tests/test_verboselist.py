#!/usr/bin/python3
"""Unittests for VerboseList Class
"""
import unittest
from scripts.task_2 import VerboseList


class TestVerboselist(unittest.TestCase):
    """Test functions for Shape Class
    """
    def test_append(self):
        """Tests that extended list append method is works as expected
        """
        # ignore the linter
        l = VerboseList([1, 2, 5, 100])

        print("Before append: {0}".format(l))

        l.append(9999)

        print("After append: {0}".format(l))

        self.assertEqual(len(l), 5)
        self.assertEqual(l[4], 9999)

if __name__ == '__main__':
    unittest.main()
