# https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(
            self,
            nums: List[int],
            k: int,
            x: int) -> List[int]:
        heap = [(abs(num - x), num) for num in nums]
        heapq.heapify(heap)

        return sorted([heapq.heappop(heap)[1] for _ in range(k)])
