# https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(set)
        for u, v, w in times:
            graph[u].add((w, v))

        visit = set()
        heap_queue = [(0, k)]
        heapq.heapify(heap_queue)
        while heap_queue:
            duration, curr = heapq.heappop(heap_queue)
            if curr in visit:
                continue

            visit.add(curr)
            if len(visit) == n:
                return duration

            for neighbor_duration, neighbor in graph[curr]:
                path_duration = duration + neighbor_duration
                if neighbor not in visit:
                    heapq.heappush(heap_queue, (path_duration, neighbor))

        return -1
