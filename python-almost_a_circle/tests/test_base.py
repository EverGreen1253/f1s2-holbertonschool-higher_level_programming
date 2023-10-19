#!/usr/bin/python3
"""Unittests for Base Class
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test functions for Base Class
    """
    def test_id_selfgen(self):
        """Tests self-generated ids for Base instances
        """
        b = Base()
        self.assertEqual(b.id, 1)

        c = Base()
        self.assertEqual(c.id, 2)

    def test_id_specified(self):
        """Tests specified id for Base instance
        """
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_none_to_json_str(self):
        """Tests converting None to json string
        """
        str = Base.to_json_string(None)
        self.assertEqual(str, "[]")

    def test_empty_list_to_json_str(self):
        """Tests converting empty List to json string
        """
        str = Base.to_json_string([])
        self.assertEqual(str, "[]")

    def test_nonempty_list_to_json_str(self):
        """Tests converting non-empty List to json string
        """
        str = Base.to_json_string([{'id': 12}])
        self.assertEqual(str, "[{\"id\": 12}]")

    def test_type_of_list_to_json_str(self):
        """Tests converting non-empty List to json string
        """
        str = Base.to_json_string([{'id': 12}])
        self.assertEqual(type(str).__name__, "str")

    def test_from_json_str_none(self):
        """Tests extracting json string from None
        """
        l = Base.from_json_string(None)
        self.assertEqual(l, [])

    def test_from_json_str_empty_list(self):
        """Tests extracting json string from empty list
        """
        l = Base.from_json_string("[]")
        self.assertEqual(l, [])

    def test_from_json_str_non_empty_list(self):
        """Tests extracting json string from non-empty list
        """
        l = Base.from_json_string("[{\"id\": 12}]")
        self.assertEqual(l, [{"id": 12}])

    def test_from_json_str_non_empty_list(self):
        """Tests extracting json string from non-empty list
        """
        l = Base.from_json_string("[{\"id\": 12}]")
        self.assertEqual(type(l).__name__, "list")

if __name__ == '__main__':
    unittest.main()
