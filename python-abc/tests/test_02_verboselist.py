#!/usr/bin/python3
"""Unittests for VerboseList Class
"""
import unittest
from task_02_verboselist import VerboseList


class TestVerboselist(unittest.TestCase):
    """Test functions for Shape Class
    """
    def test_append(self):
        """Tests that extended list append method is works as expected
        """
        # ignore the linter
        l = VerboseList([1, 2, 5, 100])

        print("\n\nBefore append: {0}".format(l))

        l.append(9999)

        print("After append: {0}".format(l))

        self.assertEqual(len(l), 5)
        self.assertEqual(l[4], 9999)


    def test_extend(self):
        """Tests that extended list extend method is works as expected
        """
        # ignore the linter
        l = VerboseList([1, 2, 5, 100])

        print("\n\nBefore extend: {0}".format(l))

        l.extend([9, 6, 3])

        print("After extend: {0}".format(l))

        self.assertEqual(len(l), 7)


    def test_remove(self):
        """Tests that extended list remove method is works as expected
        """
        # ignore the linter
        l = VerboseList([1, 2, 5, 100])

        print("\n\nBefore remove: {0}".format(l))

        l.remove(5)

        print("After remove: {0}".format(l))

        self.assertEqual(len(l), 3)


    def test_remove_non_existent(self):
        """Tests that extended list remove method is works as expected
        """
        # ignore the linter
        l = VerboseList([1, 2, 5, 100])

        print("\n\nBefore remove: {0}".format(l))

        with self.assertRaises(ValueError):
            l.remove(9999)

        print("After remove: {0}".format(l))


    def test_pop_index_one(self):
        """Tests that extended list pop method is works as expected
        """
        # ignore the linter
        l = VerboseList([1, 2, 5, 100])

        print("\n\nBefore pop: {0}".format(l))

        l.pop(1)

        print("After pop: {0}".format(l))

        self.assertEqual(len(l), 3)


    def test_pop_index_out_of_range(self):
        """Tests that extended list pop method is works as expected
        """
        # ignore the linter
        l = VerboseList([1, 2, 5, 100])

        print("\n\nBefore pop: {0}".format(l))

        with self.assertRaises(IndexError):
            l.pop(9999)

        print("After pop: {0}".format(l))


    def test_pop_index_not_specified(self):
        """Tests that extended list pop method is works as expected when the index is not specified
        """
        # ignore the linter
        l = VerboseList([1, 2, 5, 100])

        print("\n\nBefore pop: {0}".format(l))

        l.pop()

        print("After pop: {0}".format(l))

        self.assertEqual(len(l), 3)

    def test_pop(self):
        """Test pop."""
        vl = VerboseList([1, 2, 3])
        item_popped = vl.pop()
        assert item_popped == 3, "Pop does not work as expected"
        assert vl == [1, 2], "Pop does not update list correctly"
        item_popped = vl.pop(0)
        assert item_popped == 1, "Pop with index does not work as expected"
        assert vl == [2], "Pop with index does not update list correctly"
        try:
            vl.pop()
            assert vl == [], "Pop does not empty list as expected"
        except IndexError:
            pass

    def test_edge_cases(self):
        """Test edge cases."""
        vl = VerboseList()
        vl.append(None)
        assert vl == [None], "Append None does not work as expected"
        vl.extend([])
        assert vl == [None], "Extend with empty list does not work as expected"

if __name__ == '__main__':
    unittest.main()
