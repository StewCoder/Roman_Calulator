"""
//============================================================================
// Name        : Roman_Calculator.py
// Author      : StewCode
// Version     : 1.0
// Description : Performs basic math operations using Roman numerals.
//============================================================================
"""
import sys
import os

# Adds src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import roman_to_int, int_to_roman, evaluate_expression

"""
Test the conversion of Roman numerals to integers.

This test checks that Roman numerals are correctly converted to their integer equivalents.
"""
def test_roman_to_int():
    assert roman_to_int("VI") == 6
    assert roman_to_int("XXV") == 25
    assert roman_to_int("MCMXCIV") == 1994

"""
Test that invalid Roman numeral strings raise a ValueError.

This test checks if passing a non-Roman numeral string (e.g., "ABC") results in a ValueError being raised.
"""
def test_int_to_roman():
    assert int_to_roman(6) == "VI"
    assert int_to_roman(25) == "XXV"
    assert int_to_roman(3999) == "MMMCMXCIX"

# Test invalid and edge cases
def test_zero_case():
    try:
        int_to_roman(0)
    except ValueError as x:
        assert str(x) == "0 does not exist in Roman numerals."
