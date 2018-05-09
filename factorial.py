"""Factorial function - Version 2 - TDD
This function was written and adapted after the tests were written
Added exception raising when argument is negative
"""

def fact(number):
    """
    Factorial function
    """
    if number < 0:
        raise ValueError('Factorial is defined only for non-negative numbers')
    if number == 0:
        return 1
    return number * fact(number - 1)
