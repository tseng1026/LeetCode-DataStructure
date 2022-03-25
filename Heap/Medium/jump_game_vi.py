# https://leetcode.com/problems/jump-game-vi/

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        result = 0
        for idx, num in enumerate(nums):
            while heap and idx - heap[0][1] > k:
                heapq.heappop(heap)

            result = -heap[0][0] + num if heap else num
            heapq.heappush(heap, (-result, idx))

        return result
