#!/usr/bin/python3
"""Unittests for FlyingFish Class
"""
from io import StringIO
import sys
import unittest
from task_04_flyingfish import FlyingFish, Fish, Bird


class TestFlyingFish(unittest.TestCase):
    """Test functions for FlyingFish Class
    """
    def test_fly_output(self):
        """Tests that the overridden methods work as expected
        """
        ff = FlyingFish()

        capturedOutput = StringIO()     # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        ff.fly()                        # Call unchanged function.
        sys.stdout = sys.__stdout__     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), "The flying fish is soaring!\n")


    def test_swim_output(self):
        """Tests that the overridden methods work as expected
        """
        ff = FlyingFish()

        capturedOutput = StringIO()     # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        ff.swim()                       # Call unchanged function.
        sys.stdout = sys.__stdout__     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), "The flying fish is swimming!\n")


    def test_habitat_output(self):
        """Tests that the overridden methods work as expected
        """
        ff = FlyingFish()

        capturedOutput = StringIO()     # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        ff.habitat()                    # Call unchanged function.
        sys.stdout = sys.__stdout__     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), "The flying fish lives both in water and the sky!\n")

    def test_method_resolution_order(self):
        """Tests that the overridden methods work as expected
        """
        order = FlyingFish.mro()
        # print(order)

        # Note: order of inheritance affects mro ordering
        self.assertEqual(order[0], FlyingFish)
        self.assertEqual(order[1], Fish)
        self.assertEqual(order[2], Bird)


if __name__ == '__main__':
    unittest.main()
