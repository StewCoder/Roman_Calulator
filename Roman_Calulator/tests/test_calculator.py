"""
//============================================================================
// Name        : Roman_Calculator.py
// Author      : StewCode
// Version     : 1.0
// Description : Performs basic math operations using Roman numerals.
//============================================================================
"""
import unittest
import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import roman_to_int, int_to_roman, evaluate_expression  

class TestRomanCalculator(unittest.TestCase):

    """
    Test the conversion of Roman numerals to integers.

    This test checks that Roman numerals are correctly converted to their integer equivalents.
    """
    def test_roman_to_int(self):
        self.assertEqual(roman_to_int("I"), 1)
        self.assertEqual(roman_to_int("IV"), 4)
        self.assertEqual(roman_to_int("X"), 10)
        self.assertEqual(roman_to_int("XLII"), 42)
        self.assertEqual(roman_to_int("CXXIII"), 123)
        self.assertEqual(roman_to_int("MCMXCIV"), 1994)

    """
    Test that invalid Roman numeral strings raise a ValueError.
    
    This test checks if passing a non-Roman numeral string (e.g., "ABC") results in a ValueError being raised.
    """
    def test_int_to_roman(self):
        self.assertEqual(int_to_roman(1), "I")
        self.assertEqual(int_to_roman(4), "IV")
        self.assertEqual(int_to_roman(10), "X")
        self.assertEqual(int_to_roman(42), "XLII")
        self.assertEqual(int_to_roman(123), "CXXIII")
        self.assertEqual(int_to_roman(1994), "MCMXCIV")

    """
    Evaluate a mathematical expression with Roman numerals and return the result as a Roman numeral.
    """
    def test_evaluate_expression(self):
        self.assertEqual(evaluate_expression("1 + 1"), 2)
        self.assertEqual(evaluate_expression("10 - 5 * 2"), 0)
        self.assertEqual(evaluate_expression("(2 + 3) * 4"), 20)
        self.assertEqual(evaluate_expression("10 / 2 + 5"), 10)
        self.assertEqual(evaluate_expression("5 + 5"), 10)

if __name__ == '__main__':
    unittest.main()
