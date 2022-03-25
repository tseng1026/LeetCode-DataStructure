# https://leetcode.com/problems/sliding-window-maximum/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result, heap = [], []
        heapq.heapify(heap)
        for idx, num in enumerate(nums):
            heapq.heappush(heap, (-num, idx))

            while heap and heap[0][1] <= idx - k:
                heapq.heappop(heap)

            result.append(-heap[0][0])

        return result[k - 1:]
