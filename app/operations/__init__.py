"""
Operations module: basic calculator functions.
"""

def addition(a: float, b: float) -> float:
    """Perform addition."""
    return a + b

def subtraction(a: float, b: float) -> float:
    """Perform subtraction."""
    return a - b

def multiplication(a: float, b: float) -> float:
    """Perform multiplication."""
    return a * b

def division(a: float, b: float) -> float:
    """Perform division, with zero division handling."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
