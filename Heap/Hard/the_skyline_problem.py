# https://leetcode.com/problems/the-skyline-problem/

class Solution:
    LEFT, RIGHT = 0, 1

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        flatten = []
        for idx, (left, right, height) in enumerate(buildings):
            flatten.append((left, self.LEFT, -height, idx))
            flatten.append((right, self.RIGHT, height, idx))
        flatten = sorted(flatten)

        heap = []
        heapq.heapify(heap)

        seen = set()
        current_height, result = 0, []
        for pos, left_or_right, height, idx in flatten:
            if left_or_right == self.LEFT:
                if current_height < -height:
                    result.append([pos, -height])
                    current_height = -height
                heapq.heappush(heap, (height, idx))

            else:
                seen.add(idx)
                while heap and heap[0][1] in seen:
                    heapq.heappop(heap)

                if not heap or -heap[0][0] < current_height:
                    current_height = -heap[0][0] if heap else 0
                    result.append([pos, current_height])

        return result
