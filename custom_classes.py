class Calculator:
    def __init__(self):
        self._current_val = 0
    def add(self, value):
        self._current_val += value 
        return self._current_val