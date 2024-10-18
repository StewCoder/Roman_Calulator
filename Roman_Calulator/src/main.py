"""
//============================================================================
// Name        : Roman_Calculator.py
// Author      : StewCode
// Version     : 1.0
// Description : Performs basic math operations using Roman numerals.
//============================================================================
"""
import re
import argparse

"""
Convert a Roman numeral to an integer.

Parameters:
roman (str): A string representing a Roman numeral.

Returns:
int: The integer representation of the Roman numeral.

Checks:
ValueError: If the input is not a valid Roman numeral.
"""
# Roman numeral conversion functions
def roman_to_int(l):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in reversed(l):
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total



"""
Convert an integer to a Roman numeral.

Parameters:
num (int): An integer between 1 and 3999.

Returns:
str: The Roman numeral representation of the integer.

Checks:
ValueError: If the integer is less than 1 or greater than 3999.
"""
def int_to_roman(num):
    if num <= 0:
        return "0 does not exist in Roman numerals."
    if num > 3999:
        return "You’re going to need a bigger calculator."
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_number = ''
    for i in range(len(val)):
        while num >= val[i]:
            roman_number += syms[i]
            num -= val[i]
    return roman_number



"""
Evaluate a mathematical expression with Roman numerals and return the result as a Roman numeral.

This function takes an expression involving Roman numerals and arithmetic operations (+, -, *, /), evaluates it, 
and returns the result as a Roman numeral.

Parameters:
expression (str): A string containing the mathematical expression (e.g., "(VII + V) * II + I").

Returns:
str: The result of the evaluation as a Roman numeral.

Checks:
ValueError: If the input is not a valid Roman numeral expression.
RuntimeError: Check cases for zero, negative results, fractions, or numbers larger than 3999.
"""
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception:
        return "I don’t know how to read this."



"""
Main function to handle command-line input and evaluate the Roman numeral expression.

Reads the expression provided as command-line arguments then computes and prints the result in Roman numerals.
Handles error cases such as zero, negative numbers, or invalid input.

Example:
python3 main.py "(VII + V) * II + I"
XXV
"""
def main():
    # Setup argparse to handle input
    parser = argparse.ArgumentParser(description='Roman Numeral Calculator')
    
    # Use `nargs='+'` to allow the entire expression to be treated as a single argument
    parser.add_argument('expression', nargs='+', help='Mathematical expression with Roman numerals (e.g. (VII + V) * II + I)')
    
    # Parse command-line arguments
    args = parser.parse_args()
    input_expr = ' '.join(args.expression)  # Join the list of arguments into a single string

    # Replace Roman numerals with their integer values
    tokens = re.findall(r'[IVXLCDM]+|[+\-*/()]', input_expr)
    for i in range(len(tokens)):
        if re.match(r'[IVXLCDM]+', tokens[i]):
            try:
                tokens[i] = roman_to_int(tokens[i])
            except KeyError:
                print("I don’t know how to read this.")
                return

    # Join tokens back into a string to evaluate
    expr_to_eval = ''.join(str(token) for token in tokens)

    # Evaluate the expression
    result = evaluate_expression(expr_to_eval)

    # Validate the result
    if isinstance(result, int):
        if result < 0:
            print("Negative numbers can’t be represented in Roman numerals.")
        elif result == 0:
            print("0 does not exist in Roman numerals.")
        else:
            print(int_to_roman(result))
    else:
        print(result)

if __name__ == "__main__":
    main()
