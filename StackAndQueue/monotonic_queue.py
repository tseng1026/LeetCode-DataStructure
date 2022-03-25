from typing import List


class MonotonicQueue:
    def __init__(self, nums: List, capacity: int):
        self.nums = nums
        self.capacity = capacity

    def get_increasing_queue(self):
        monotonic = []
        for idx, num in enumerate(self.nums):
            while monotonic and monotonic[0][0] <= idx - self.capacity:
                monotonic.pop(0)

            while monotonic and monotonic[-1][1] < num:
                curr_num, curr_idx = monotonic.pop()
                # write your codes here

            monotonic.append((num, idx))

    def get_decreasing_queue(self):
        monotonic = []
        for idx, num in enumerate(self.nums):
            while monotonic and monotonic[0][0] <= idx - self.capacity:
                monotonic.pop(0)

            while monotonic and monotonic[-1][1] > num:
                curr_num, curr_idx = monotonic.pop()
                # write your codes here

            monotonic.append((idx, num))
