# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [(x**2 + y**2, [x, y]) for x, y in points]
        heapq.heapify(distance)

        return [heapq.heappop(distance)[1] for _ in range(k)]
