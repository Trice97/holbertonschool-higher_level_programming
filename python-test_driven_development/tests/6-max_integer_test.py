#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test class for the max_integer function
    """

    def test_normal_list(self):
        """Test with a normal list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test with a list containing just one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_identical_values(self):
        """Test with a list containing identical values"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_mixed_integers_and_floats(self):
        """Test with a list of mixed integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)

    def test_string(self):
        """Test with a string (list of characters)"""
        self.assertEqual(max_integer("abcdefg"), "g")

    def test_list_of_strings(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_max_at_beginning(self):
        """Test with max value at the beginning"""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_in_middle(self):
        """Test with max value in the middle"""
        self.assertEqual(max_integer([1, 2, 9, 3, 4]), 9)
