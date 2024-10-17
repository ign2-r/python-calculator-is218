import pytest
from app.calculator import Calculator

# Test valid calculations and history logging
@pytest.mark.parametrize("a, b, operation, expected", [
    (1, 1, 'add', 2),
    (5, 3, 'subtract', 2),
    (3, 4, 'multiply', 12),
    (10, 2, 'divide', 5),
])
def test_calculator_valid_operations(a, b, operation, expected):
    calc = Calculator()
    assert calc.calculate_and_log(a, b, operation) == expected
    assert calc.get_history()[-1] == f"{a} {operation} {b} = {expected}"

# Test division by zero
@pytest.mark.parametrize("a, b, operation", [
    (10, 0, 'divide'),
    (5, 0, 'divide')
])
def test_calculator_division_by_zero(a, b, operation):
    calc = Calculator()
    assert calc.calculate_and_log(a, b, operation) == "Cannot divide by zero."

# Test invalid operations
@pytest.mark.parametrize("a, b, operation", [
    (1, 1, 'invalid'),
    (5, 3, 'unknown'),
])
def test_calculator_invalid_operation(a, b, operation):
    calc = Calculator()
    assert calc.calculate_and_log(a, b, operation) == "Invalid operation."

# Test undo functionality
def test_calculator_undo():
    calc = Calculator()
    calc.calculate_and_log(1, 1, 'add')
    calc.calculate_and_log(5, 3, 'subtract')
    undo = calc.undo_last()
    assert undo == "5.0 subtract 3.0 = 2.0"
    assert len(calc.get_history()) == 1
