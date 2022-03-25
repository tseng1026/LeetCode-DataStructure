# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxima, minima = [], []
        heapq.heapify(maxima)
        heapq.heapify(minima)

        start, max_length = 0, 0
        for idx, num in enumerate(nums):
            heapq.heappush(maxima, (-num, idx))
            heapq.heappush(minima, (num, idx))

            while maxima and maxima[0][1] < start:
                heapq.heappop(maxima)

            while minima and minima[0][1] < start:
                heapq.heappop(minima)

            if -maxima[0][0] - minima[0][0] <= limit:
                max_length = max(idx - start + 1, max_length)

            else:
                start += 1

        return max_length
