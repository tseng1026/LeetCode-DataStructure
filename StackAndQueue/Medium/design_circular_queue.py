# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = deque()
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.queue.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.queue.popleft()
        return True

    def Front(self) -> int:
        return self.queue[0] if self.queue else -1

    def Rear(self) -> int:
        return self.queue[-1] if self.queue else -1

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.capacity
