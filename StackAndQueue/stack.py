class StackNode:
    def __init__(self, val: int = 0, prev=None):
        self.val = val
        self.prev = prev


class Stack:
    def __init__(self):
        self.top = None

    def push(self, val: int) -> None:
        temp = self.top
        self.top = StackNode(val, temp)

    def pop(self) -> int:
        if not self.top:
            raise IndexError

        temp = self.top.val
        self.top = self.top.prev
        return temp

    def peek(self) -> int:
        if not self.top:
            raise IndexError

        return self.top.val

    def isEmpty(self) -> bool:
        return self.top is None
