# https://leetcode.com/problems/maximum-number-of-eaten-apples/

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []
        heapq.heapify(heap)

        idx, result = 0, 0
        while heap or idx < len(apples):
            if idx < len(apples) and apples[idx] > 0:
                heapq.heappush(heap, (idx + days[idx] - 1, apples[idx]))

            while heap and heap[0][0] < idx:
                heapq.heappop(heap)

            if heap:
                day, apple = heapq.heappop(heap)
                if apple - 1 > 0:
                    heapq.heappush(heap, (day, apple - 1))
                result += 1

            idx += 1

        return result
