# https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        monotonic = []
        for idx, num in enumerate(nums + nums):
            while monotonic and monotonic[-1][1] < num:
                temp_idx, _ = monotonic.pop()
                if temp_idx >= len(nums):
                    continue

                result[temp_idx] = num
            monotonic.append((idx, num))

        return result
