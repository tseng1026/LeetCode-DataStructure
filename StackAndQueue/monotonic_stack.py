from typing import List


class MonotonicStack:
    def __init__(self, nums: List):
        self.nums = nums

    def get_increasing_stack(self):
        monotonic = []
        for idx, num in enumerate(self.nums):
            while monotonic and monotonic[-1][1] < num:
                curr_idx, curr_num = monotonic.pop()
                # write your codes here

            monotonic.append((idx, num))

    def get_decreasing_stack(self):
        monotonic = []
        for idx, num in enumerate(self.nums):
            while monotonic and monotonic[-1][1] > num:
                curr_idx, curr_num = monotonic.pop()
                # write your codes here

            monotonic.append((idx, num))
