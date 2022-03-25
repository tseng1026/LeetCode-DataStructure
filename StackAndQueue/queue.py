class QueueNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, val: int) -> None:
        temp = QueueNode(val)
        if self.last:
            self.last.next = temp

        self.last = temp
        if not self.first:
            self.first = self.last

    def dequeue(self) -> int:
        if not self.first:
            raise IndexError

        temp = self.first.val
        self.first = self.first.next
        if not self.first:
            self.last = None
        return temp

    def peek(self) -> int:
        if not self.first:
            raise IndexError

        return self.first.val

    def isEmpty(self) -> bool:
        return self.first is None
