# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for row in matrix:
            for num in row:
                heapq.heappush(heap, -num)

                if len(heap) > k:
                    heapq.heappop(heap)

        return -heapq.heappop(heap)
