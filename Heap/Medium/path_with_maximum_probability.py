# https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self,
                       n: int,
                       edges: List[List[int]],
                       succ_prob: List[float],
                       start: int,
                       end: int) -> float:
        graph = defaultdict(set)
        for idx, (a, b) in enumerate(edges):
            graph[a].add((succ_prob[idx], b))
            graph[b].add((succ_prob[idx], a))

        visit = set()
        heap_queue = [(-1, start)]
        heapq.heapify(heap_queue)
        while heap_queue:
            prob, curr = heapq.heappop(heap_queue)
            if curr in visit:
                continue

            visit.add(curr)
            if curr == end:
                return -prob

            for neighbor_prob, neighbor in graph[curr]:
                path_prob = -prob * neighbor_prob
                if neighbor not in visit:
                    heapq.heappush(heap_queue, (-path_prob, neighbor))

        return 0
