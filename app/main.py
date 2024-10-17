# main.py
from calculator import Calculator

def repl():
    calc = Calculator()
    print("Welcome to the REPL Calculator. Type 'exit' to quit. Type 'history' to view history. Type 'undo' to undo last.")
    while True:
        user_input = input("Enter operation (e.g., 1 1 add): ").strip()
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'history':
            history = calc.get_history()
            if history:
                for entry in history:
                    print(entry)
            else:
                print("No history available.")
        elif user_input.lower() == 'undo':
            undo = calc.undo_last()
            if undo:
                print(f"Undone: {undo}")
            else:
                print("No operations to undo.")
        else:
            try:
                a, b, operation = user_input.split()
                a = float(a)
                b = float(b)
                result = calc.calculate_and_log(a, b, operation)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Invalid input or operation: {e}")

if __name__ == "__main__":
    repl()
