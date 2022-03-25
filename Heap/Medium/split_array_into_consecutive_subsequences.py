# https://leetcode.com/problems/split-array-into-consecutive-subsequences/

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap_queue = []
        heapq.heapify(heap_queue)
        for num in nums + [float("inf")]:
            while heap_queue and heap_queue[0][0] + 1 < num:
                last, length = heapq.heappop(heap_queue)

                if length < 3:
                    return False

            if not heap_queue or heap_queue[0][0] == num:
                heapq.heappush(heap_queue, (num, 1))

            else:
                last, length = heapq.heappop(heap_queue)
                heapq.heappush(heap_queue, (num, length + 1))

        return True
