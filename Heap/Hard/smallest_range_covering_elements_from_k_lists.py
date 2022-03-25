# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(nums[idx][0], 0, idx) for idx in range(len(nums))]
        heapq.heapify(heap)

        minima = min(heap, key=lambda x: x[0])[0]
        maxima = max(heap, key=lambda x: x[0])[0]
        curr_maxima = maxima
        while len(heap) == len(nums):
            num, pos, idx = heapq.heappop(heap)

            if curr_maxima - num < maxima - minima:
                minima = num
                maxima = curr_maxima

            if pos + 1 < len(nums[idx]):
                heapq.heappush(heap, (nums[idx][pos + 1], pos + 1, idx))
                curr_maxima = max(nums[idx][pos + 1], curr_maxima)

        return [minima, maxima]
