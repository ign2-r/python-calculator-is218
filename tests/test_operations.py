"""
Unit tests for the arithmetic functions in the app.operations module.

This module contains tests for addition, subtraction, multiplication, 
and division, including a test for division by zero.
"""

import pytest
from app.operations import addition, subtraction, multiplication, division

# Test addition
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (5, 5, 10)
])
def test_addition(a, b, expected):
    """
    Test that the addition function returns the correct result.
    """
    assert addition(a, b) == expected

# Test subtraction
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 0),
    (5, 3, 2),
    (10, 5, 5)
])
def test_subtraction(a, b, expected):
    """
    Test that the subtraction function returns the correct result.
    """
    assert subtraction(a, b) == expected

# Test multiplication
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),
    (3, 4, 12),
    (5, 5, 25)
])
def test_multiplication(a, b, expected):
    """
    Test that the multiplication function returns the correct result.
    """
    assert multiplication(a, b) == expected

# Test division
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1),
    (6, 2, 3),
    (10, 5, 2)
])
def test_division(a, b, expected):
    """
    Test that the division function returns the correct result.
    """
    assert division(a, b) == expected

# Test division by zero
@pytest.mark.parametrize("a, b", [
    (10, 0),
    (5, 0)
])
def test_division_by_zero(a, b):
    """
    Test that division by zero returns the appropriate error message.
    """
    assert division(a, b) == "Cannot divide by zero."
