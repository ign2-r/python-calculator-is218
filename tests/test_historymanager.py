from app.historymanager import HistoryManager

def test_add_to_history():
    history_manager = HistoryManager()
    history_manager.add_to_history("1 + 1 = 2")
    assert history_manager.get_history() == ["1 + 1 = 2"]

def test_get_history():
    history_manager = HistoryManager()
    assert history_manager.get_history() == []

def test_undo_last():
    history_manager = HistoryManager()
    history_manager.add_to_history("5 - 3 = 2")
    history_manager.add_to_history("10 / 2 = 5")
    undo = history_manager.undo_last()
    assert undo == "10 / 2 = 5"
    assert history_manager.get_history() == ["5 - 3 = 2"]

def test_undo_last_empty():
    history_manager = HistoryManager()
    assert history_manager.undo_last() is None
