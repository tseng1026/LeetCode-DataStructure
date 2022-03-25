# https://leetcode.com/problems/diagonal-traverse-ii/

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        heap = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                heap.append((i + j, j, nums[i][j]))
        heapq.heapify(heap)

        return [heapq.heappop(heap)[2] for _ in range(len(heap))]
