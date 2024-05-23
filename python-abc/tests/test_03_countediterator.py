#!/usr/bin/python3
"""Unittests for CountedIterator Class
"""
import unittest
from task_03_countediterator import CountedIterator


class TestCountedIterator(unittest.TestCase):
    """Test functions for CountedIterator Class
    """
    def test_subclassed_next(self):
        """Tests that the modified __next__ works as expected
        """
        numlist = [1, 2, 5, 10, 50]
        it = CountedIterator(numlist)

        for n in range(0, 5, 1):
            i = next(it)
            print("Value is {}".format(i))
            self.assertEqual(i, numlist[n])
            print("Current counter value is {}".format(it.get_count()))

            # call next one more time on final loop to trigger out of range error
            if n == 4:
                with self.assertRaises(StopIteration):
                    i = next(it)
                print("StopIteration exception successfully caught")

if __name__ == '__main__':
    unittest.main()
