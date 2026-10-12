class Calculator:
    def __init__(self):
        self._current_val = 0
    def add(self, value):
        self._current_val += value 

    def sub(self,x,y):
        self._current_val = x - y
    def multiply(self, x, y):
        self._current_val = x * y
        return self._current_val