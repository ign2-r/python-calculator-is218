"""
Test module for the BasicCalculation class.

This module contains tests to validate the basic operations like addition, subtraction,
multiplication, division, modulo, and power, as well as error handling for division by zero
and invalid operations.
"""

import pytest
from app.calculation import BasicCalculation

# Test valid calculations
@pytest.mark.parametrize("a, b, operation, expected", [
    (1, 1, 'add', 2),
    (5, 3, 'subtract', 2),
    (3, 4, 'multiply', 12),
    (10, 2, 'divide', 5),
    (10, 3, 'modulo', 1),
    (2, 3, 'power', 8)
])
def test_basic_calculation_valid(a, b, operation, expected):
    """
    Test operations (add, subtract, multiply, divide, modulo, power) return the expected results.
    """
    calc = BasicCalculation()
    assert calc.calculate(a, b, operation) == expected

# Test division by zero in calculation class
@pytest.mark.parametrize("a, b, operation", [
    (10, 0, 'divide'),
    (5, 0, 'divide'),
    (10, 0, 'modulo')
])
def test_calculation_division_by_zero(a, b, operation):
    """
    Test that division and modulo by zero raise the appropriate error message.
    """
    calc = BasicCalculation()
    if operation == 'divide':
        assert calc.calculate(a, b, operation) == "Cannot divide by zero."
    elif operation == 'modulo':
        assert calc.calculate(a, b, operation) == "Cannot modulo by zero."

# Test invalid operations
@pytest.mark.parametrize("a, b, operation", [
    (1, 1, 'invalid'),
    (5, 3, 'unknown'),
])
def test_calculation_invalid_operation(a, b, operation):
    """
    Test that invalid operations return the appropriate error message.
    """
    calc = BasicCalculation()
    assert calc.calculate(a, b, operation) == "Invalid operation."

# Test unsupported operations
@pytest.mark.parametrize("a, b, operation", [
    (1, 1, 'log'),  # Unsupported operation
    (2, 2, 'sqrt')  # Unsupported operation
])
def test_calculation_unsupported_operation(a, b, operation):
    """
    Test that unsupported operations return an invalid operation error message.
    """
    calc = BasicCalculation()
    assert calc.calculate(a, b, operation) == "Invalid operation."

# Test edge cases for valid operations
@pytest.mark.parametrize("a, b, operation, expected", [
    (-1, 1, 'add', 0),        # negative + positive
    (0, 0, 'add', 0),         # zero + zero
    (1.5, 2.5, 'add', 4),     # floats
    (-5, -5, 'multiply', 25), # negative * negative
    (2, -3, 'power', 0.125)   # positive base, negative exponent
])
def test_edge_cases(a, b, operation, expected):
    """
    Test edge cases like negative numbers, zeros, and floats.
    """
    calc = BasicCalculation()
    assert calc.calculate(a, b, operation) == expected
