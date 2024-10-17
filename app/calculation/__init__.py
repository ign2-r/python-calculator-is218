# calculation/__init__.py
from abc import ABC, abstractmethod
from operations import addition, subtraction, multiplication, division

class Calculation(ABC):
    @abstractmethod
    def calculate(self, a, b, operation):
        pass

class BasicCalculation(Calculation):
    def calculate(self, a, b, operation):
        if operation == 'add':
            return addition(a, b)
        elif operation == 'subtract':
            return subtraction(a, b)
        elif operation == 'multiply':
            return multiplication(a, b)
        elif operation == 'divide':
            return division(a, b)
        else:
            return " You have entered an nvalid operation."
