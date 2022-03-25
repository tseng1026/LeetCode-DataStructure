# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        situation = []
        heapq.heapify(situation)

        for idx, row in enumerate(mat):
            soldiers = row.count(1)
            heapq.heappush(situation, (soldiers, idx))

        return [heapq.heappop(situation)[1] for _ in range(k)]
