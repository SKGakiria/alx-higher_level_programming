#!/usr/bin/python3
"""Unittest for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Tests an ordered list of integers."""
        ordered = [2, 3, 4, 5, 6]
        self.assertEqual(max_integer(ordered), 5)

    def test_unordered_list(self):
        """Tests an unordered list of integers."""
        unordered = [2, 3, 6, 5, 4]
        self.assertEqual(max_integer(unordered), 5)

    def test_max_at_beginning(self):
        """Tests a list of integers with max value at the beginning."""
        max_at_beginning = [6, 5, 4, 3, 2]
        self.assertEqual(max_integer(max_at_beginning), 6)

    def test_empty_list(self):
        """Tests an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Tests single element list."""
        one_element = [9]
        self.assertEqual(max_integer(one_element), 9)

    def test_floats(self):
        """Tests a floats list."""
        floats = [2.1, 3.2, 4.5, 5.7, -6.6]
        self.assertEqual(max_integer(floats), 5.7)

    def test_ints_and_floats(self):
        """Tests an ints and floats list."""
        ints_and_floats = [1, 2.1, 3, 4.5, 6]
        self.assertEqual(max_integer(ints_and_floats), 6)

    def test_string(self):
        """Tests a string."""
        strings = ["Beauty"]
        self.assertEqual(max_integer(string), 'e')

    def test_list_of_strings(self):
        """Tests a string list."""
        strings = ["Beauty", "is", "in", "looking", "around"]
        self.assertEqual(max_integer(strings), "around")

    def test_empty_string(self):
        """Tests an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
