"""
Calculator Test Module

This module contains unit tests for basic arithmetic operations such as addition, 
subtraction, multiplication, and division. The tests use pytest and cover both 
valid operations and error handling (like division by zero).
"""

import pytest
from app.operations import addition, subtraction, multiplication, division

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (5, 5, 10)
])
def test_addition(a, b, expected):
    """
    Test addition function with multiple sets of input values.

    Args:
        a (int, float): The first operand.
        b (int, float): The second operand.
        expected (int, float): The expected result of adding `a` and `b`.

    Asserts:
        The result of addition(a, b) is equal to `expected`.
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

    Args:
        a (int, float): The first operand.
        b (int, float): The second operand.
        expected (int, float): The expected result of subtracting `b` from `a`.

    Asserts:
        The result of subtraction(a, b) is equal to `expected`.
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

    Args:
        a (int, float): The first operand.
        b (int, float): The second operand.
        expected (int, float): The expected result of multiplying `a` and `b`.

    Asserts:
        The result of multiplication(a, b) is equal to `expected`.
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

    Args:
        a (int, float): The dividend.
        b (int, float): The divisor.
        expected (int, float): The expected result of dividing `a` by `b`.

    Asserts:
        The result of division(a, b) is equal to `expected`.
    """
    assert division(a, b) == expected

@pytest.mark.parametrize("a, b", [
    (10, 0),
    (5, 0)
])
def test_negative_division(a, b):
    """
    Test division function for division by zero, ensuring an error is raised.

    Args:
        a (int, float): The dividend.
        b (int, float): The divisor (zero).

    Asserts:
        A ZeroDivisionError is raised when dividing by zero.
    """
    with pytest.raises(ZeroDivisionError):
        division(a, b)
