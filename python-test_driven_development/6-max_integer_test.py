
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer function"""

    def test_normal_list(self):
        """Test with a normal list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        
    def test_mixed_numbers(self):
        """Test with a mix of positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        
    def test_duplicate_numbers(self):
        """Test with duplicate numbers"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
        
    def test_single_element_list(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([5]), 5)
        
    def test_float_numbers(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        
    def test_mixed_types(self):
        """Test with mixed types (int and float)"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)
        
    def test_string(self):
        """Test with a string"""
        self.assertEqual(max_integer("abcdefg"), "g")
        
    def test_list_of_strings(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")
        
    def test_empty_string(self):
        """Test with an empty string"""
        self.assertIsNone(max_integer(""))


if __name__ == '__main__':
    unittest.main()
