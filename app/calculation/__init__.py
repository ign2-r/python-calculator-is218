"""
Calculation module: abstract base class for calculator operations.
"""
from abc import ABC, abstractmethod
from typing import Union
from app.operations import addition, subtraction, multiplication, division

class Calculation(ABC):
    """Abstract base class for calculator operations."""
    @abstractmethod
    def calculate(self, a: float, b: float, operation: str) -> Union[float, str]:
        """Abstract method to perform a calculation."""
        pass

class BasicCalculation(Calculation):
    """Concrete class for basic calculations."""
    def calculate(self, a: float, b: float, operation: str) -> Union[float, str]:
        """Perform the operation based on the input and handle errors."""
        try:
            if operation == 'add':
                return addition(a, b)
            elif operation == 'subtract':
                return subtraction(a, b)
            elif operation == 'multiply':
                return multiplication(a, b)
            elif operation == 'divide':
                return division(a, b)
            else:
                return "Invalid operation."
        except ValueError as e:
            return str(e)
