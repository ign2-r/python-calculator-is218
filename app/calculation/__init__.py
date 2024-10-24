"""
Calculation module: abstract base class for calculator operations.
"""
from abc import ABC, abstractmethod
from typing import Union
from app.operations import addition, subtraction, multiplication, division, modulo, power

class Calculation(ABC):
    """Abstract base class for calculator operations."""
    @abstractmethod
    def calculate(self, a: float, b: float, operation: str) -> Union[float, str]:
        """Abstract method to perform a calculation."""
        pass # pragma: no cover

class BasicCalculation(Calculation):
    """Concrete class for basic calculations."""
    def calculate(self, a: float, b: float, operation: str) -> Union[float, str]:
        """Perform the operation based on the input."""
        if operation == 'add':
            return addition(a, b)
        elif operation == 'subtract':
            return subtraction(a, b)
        elif operation == 'multiply':
            return multiplication(a, b)
        elif operation == 'divide':
            return division(a, b)
        elif operation == 'modulo':
            return modulo(a, b)
        elif operation == 'power':
            return power(a, b)
        else:
            return "Invalid operation."
