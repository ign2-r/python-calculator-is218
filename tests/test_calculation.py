import pytest
from app.calculation import BasicCalculation

# Test valid calculations
@pytest.mark.parametrize("a, b, operation, expected", [
    (1, 1, 'add', 2),
    (5, 3, 'subtract', 2),
    (3, 4, 'multiply', 12),
    (10, 2, 'divide', 5),
])
def test_basic_calculation_valid(a, b, operation, expected):
    calc = BasicCalculation()
    assert calc.calculate(a, b, operation) == expected

# Test division by zero in calculation class
@pytest.mark.parametrize("a, b, operation", [
    (10, 0, 'divide'),
    (5, 0, 'divide')
])
def test_calculation_division_by_zero(a, b, operation):
    calc = BasicCalculation()
    assert calc.calculate(a, b, operation) == "Cannot divide by zero."

# Test invalid operations
@pytest.mark.parametrize("a, b, operation", [
    (1, 1, 'invalid'),
    (5, 3, 'unknown'),
])
def test_calculation_invalid_operation(a, b, operation):
    calc = BasicCalculation()
    assert calc.calculate(a, b, operation) == "Invalid operation."