# https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        heapq.heapify(heap)

        for _ in range(n - 1):
            min_element = heapq.heappop(heap)

            for prime in [2, 3, 5]:
                heapq.heappush(heap, min_element * prime)

                if min_element % prime == 0:
                    break

        return heap[0]
