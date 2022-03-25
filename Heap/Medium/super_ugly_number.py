# https://leetcode.com/problems/super-ugly-number/
# reference:
# https://leetcode.com/problems/super-ugly-number/discuss/868948/Python3-l-Faster-than-99.35-or-using-heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        heapq.heapify(heap)

        for _ in range(n - 1):
            min_element = heapq.heappop(heap)

            for prime in primes:
                heapq.heappush(heap, min_element * prime)

                if min_element % prime == 0:
                    break

        return heap[0]
