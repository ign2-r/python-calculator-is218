"""
Calculator Test Module

This module contains unit tests for basic arithmetic operations and the calculator
class. The tests use pytest with parameterization to cover multiple scenarios, including
valid operations and error handling (like division by zero).
"""

import pytest
from operations import addition, subtraction, multiplication, division
from calculator import Calculator

# Parameterized tests for basic arithmetic functions

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (5, 5, 10)
])
def test_addition(a, b, expected):
    """
    Test addition function with multiple sets of input values.
    """
    assert addition(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 0),
    (5, 3, 2),
    (10, 5, 5)
])
def test_subtraction(a, b, expected):
    """
    Test subtraction function with multiple sets of input values.
    """
    assert subtraction(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),
    (3, 4, 12),
    (5, 5, 25)
])
def test_multiplication(a, b, expected):
    """
    Test multiplication function with multiple sets of input values.
    """
    assert multiplication(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1),
    (6, 2, 3),
    (10, 5, 2)
])
def test_positive_division(a, b, expected):
    """
    Test division function with valid input values.
    """
    assert division(a, b) == expected


@pytest.mark.parametrize("a, b", [
    (10, 0),
    (5, 0)
])
def test_division_by_zero(a, b):
    """
    Test division function for division by zero, ensuring an error is raised.
    """
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        division(a, b)


# Parameterized tests for the Calculator class
@pytest.mark.parametrize("a, b, operation, expected", [
    (1, 1, 'add', 2),
    (5, 3, 'subtract', 2),
    (3, 4, 'multiply', 12),
    (10, 2, 'divide', 5),
])
def test_calculator_valid_operations(a, b, operation, expected):
    """
    Test the Calculator class for valid operations.
    """
    calc = Calculator()
    assert calc.calculate_and_log(a, b, operation) == expected


@pytest.mark.parametrize("a, b, operation", [
    (10, 0, 'divide'),
    (5, 0, 'divide')
])
def test_calculator_division_by_zero(a, b, operation):
    """
    Test the Calculator class for division by zero, ensuring an error is returned.
    """
    calc = Calculator()
    assert calc.calculate_and_log(a, b, operation) == "Cannot divide by zero."


@pytest.mark.parametrize("a, b, operation", [
    (1, 1, 'invalid'),
    (5, 3, 'unknown'),
])
def test_calculator_invalid_operation(a, b, operation):
    """
    Test the Calculator class for invalid operations, ensuring an error is returned.
    """
    calc = Calculator()
    assert calc.calculate_and_log(a, b, operation) == "Invalid operation."
