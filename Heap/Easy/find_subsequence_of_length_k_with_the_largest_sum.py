# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums = [(-num, idx) for idx, num in enumerate(nums)]
        heapq.heapify(nums)

        idxs = []
        heapq.heapify(idxs)
        for _ in range(k):
            num, idx = heapq.heappop(nums)
            heapq.heappush(idxs, (idx, -num))

        return [heapq.heappop(idxs)[1] for _ in range(k)]
