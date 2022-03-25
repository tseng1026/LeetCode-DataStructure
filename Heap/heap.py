from typing import List, Optional


class MinHeap:
    def __init__(self, array: Optional[List[int]]):
        self.heap = [None]
        self.length = 0

        for num in array:
            self.heappush(num)

    def heapify(self, array: List[int]):
        for num in array:
            self.heappush(num)

    def heappush(self, target: int) -> None:
        self.heap.append(target)
        self.length += 1
        self.swim(self.length)
        print(self.heap)

    def heappop(self) -> int:
        if not self.heap:
            raise IndexError

        target = self.heap[1]
        self.swap(1, self.length)
        self.heap.pop()
        self.length -= 1
        self.sink(1)
        return target

    def swim(self, idx: int) -> None:
        while idx > 1:
            if self.heap[idx] < self.heap[idx // 2]:
                self.swap(idx, idx // 2)
                idx = idx // 2
            else:
                break

    def sink(self, idx: int) -> None:
        print(self.length)
        while idx <= self.length // 2:
            left = idx * 2
            right = idx * 2 + 1

            target_idx = left
            if right <= self.length and \
                    self.heap[left] > self.heap[right]:
                target_idx = right

            if self.heap[idx] < self.heap[target_idx]:
                self.swap(idx, target_idx)
                idx = target_idx
            else:
                break

    def swap(self, a: int, b: int):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
