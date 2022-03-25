# https://leetcode.com/problems/trapping-rain-water-ii/

class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def trapRainWater(self, height_map: List[List[int]]) -> int:
        row, col = len(height_map), len(height_map[0])

        visit = set()
        heap = []
        for i in range(row - 1):
            heap.append((height_map[i][0], (i, 0)))
            heap.append((height_map[i + 1][col - 1], (i + 1, col - 1)))
            visit.add((i, 0))
            visit.add((i + 1, col - 1))
        for j in range(col - 1):
            heap.append((height_map[0][j + 1], (0, j + 1)))
            heap.append((height_map[row - 1][j], (row - 1, j)))
            visit.add((0, j + 1))
            visit.add((row - 1, j))
        heapq.heapify(heap)

        result = 0
        while heap:
            height, pos = heapq.heappop(heap)

            for direction in self.directions:
                i = pos[0] + direction[0]
                j = pos[1] + direction[1]
                if not 0 <= i < row or not 0 <= j < col:
                    continue

                if (i, j) not in visit:
                    visit.add((i, j))

                    if height <= height_map[i][j]:
                        heapq.heappush(heap, (height_map[i][j], (i, j)))

                    else:
                        result += height - height_map[i][j]
                        heapq.heappush(heap, (height, (i, j)))
        return result
