"""
Class to represent a SP reg
"""
class StackPointer:

    def __init__(self) -> None:
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()
