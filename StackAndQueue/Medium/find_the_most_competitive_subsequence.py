# https://leetcode.com/problems/find-the-most-competitive-subsequence/

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        monotonic = []
        for idx, num in enumerate(nums):
            while monotonic and monotonic[-1] > num and \
                    len(monotonic) + len(nums) - idx > k:
                monotonic.pop()
            monotonic.append(num)

        return monotonic[:k]
