"""
Calculator: ties together the calculation and history management.
"""
from typing import Union
from app.calculation import BasicCalculation
from app.historymanager import HistoryManager

class Calculator:
    """Class that integrates calculation and history management."""
    def __init__(self):
        """Initialize the calculator with a calculation and history manager."""
        self.calculation = BasicCalculation()
        self.history_manager = HistoryManager()

    def calculate_and_log(self, a: float, b: float, operation: str) -> Union[float, str]:
        """Calculate the result, log the operation in history, and return the result or error."""
        result = self.calculation.calculate(a, b, operation)
        if isinstance(result, float):
            entry = f"{a} {operation} {b} = {result}"
            self.history_manager.add_to_history(entry)
        return result

    def get_history(self) -> list:
        """Return the calculation history."""
        return self.history_manager.get_history()

    def undo_last(self) -> Union[str, None]:
        """Undo the last calculation."""
        return self.history_manager.undo_last()
