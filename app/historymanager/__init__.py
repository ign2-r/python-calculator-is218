# historymanager/__init__.py
class HistoryManager:
    def __init__(self):
        self.history = []

    def add_to_history(self, entry):
        self.history.append(entry)

    def get_history(self):
        return self.history

    def undo_last(self):
        if self.history:
            return self.history.pop()
        return None
