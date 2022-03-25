# https://leetcode.com/problems/maximum-score-from-removing-stones/

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [a, b, c]
        heapq.heapify(heap)

        result = 0
        while len(heap) >= 2:
            result += 1
            heap[-1] -= 1
            heap[-2] -= 1
            heapq.heapify(heap)

            while heap and heap[0] <= 0:
                heapq.heappop(heap)

        return result
