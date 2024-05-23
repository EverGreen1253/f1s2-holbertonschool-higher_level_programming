#!/usr/bin/python3
"""Unittests for Dragon Class
"""
from io import StringIO
import sys
import unittest
from task_05_dragon import Dragon


class TestFlyingFish(unittest.TestCase):
    """Test mixins and roar method for Dragon Class
    """
    def test_swim_output(self):
        """Tests that the swim mixin works as expected
        """
        draco = Dragon()

        capturedOutput = StringIO()     # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        draco.swim()                    # Call unchanged function.
        sys.stdout = sys.__stdout__     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), "The creature swims!\n")

    def test_fly_output(self):
        """Tests that the fly mixin works as expected
        """
        draco = Dragon()

        capturedOutput = StringIO()     # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        draco.fly()                     # Call unchanged function.
        sys.stdout = sys.__stdout__     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), "The creature flies!\n")

    def test_roar_output(self):
        """Tests that the roar method works as expected
        """
        draco = Dragon()

        capturedOutput = StringIO()     # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        draco.roar()                    # Call unchanged function.
        sys.stdout = sys.__stdout__     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), "The dragon roars!\n")

if __name__ == '__main__':
    unittest.main()
