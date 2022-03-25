# https://leetcode.com/problems/path-with-minimum-effort/

class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        visit = set()
        heap_queue = [(0, (0, 0))]
        heapq.heapify(heap_queue)
        while heap_queue:
            effort, curr = heapq.heappop(heap_queue)

            if curr in visit:
                continue

            visit.add(curr)
            if curr == (rows - 1, cols - 1):
                return effort

            for direction in self.directions:
                i = curr[0] + direction[0]
                j = curr[1] + direction[1]
                if not 0 <= i < rows or \
                        not 0 <= j < cols:
                    continue

                path_effort = abs(heights[i][j] - heights[curr[0]][curr[1]])
                if (i, j) not in visit:
                    heapq.heappush(
                        heap_queue, (max(
                            effort, path_effort), (i, j)))
