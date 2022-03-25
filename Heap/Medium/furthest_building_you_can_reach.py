# https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(
            self,
            heights: List[int],
            bricks: int,
            ladders: int) -> int:
        heap = []
        heapq.heapify(heap)

        for k in range(1, len(heights)):
            effort = heights[k] - heights[k - 1]
            if effort <= 0:
                continue

            heapq.heappush(heap, effort)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)

                if bricks < 0:
                    return k - 1

        return len(heights) - 1
