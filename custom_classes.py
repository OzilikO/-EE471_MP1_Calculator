class Calculator:
    def __init__(self):
        self._current_val = 0
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        self._current_val = a / b
        return self._current_val