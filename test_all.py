"""
Python script for measuring the coverage of the math function factorial
Author: Georgi Marinov
VUM SW Metrics Exam 08/05/2018
"""

import unittest
from factorial import fact


class FactorialTest(unittest.TestCase):
    """Factorial test class for SW Metrics Exam"""

    def test_positive(self):
        """Test factorial function with valid, positive input"""
        res = fact(4)
        self.assertEqual(24, res)

    def test_zero(self):
        """Test factorial function with zero"""
        res = fact(0)
        self.assertEqual(1, res)

    def test_negative(self):
        """Test factorial function with invalid, negative input"""
        self.assertRaises(ValueError, fact, -5)


if __name__ == "__main__":
    unittest.main()
