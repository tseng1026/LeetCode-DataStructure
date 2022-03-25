# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

class Solution:
    MOD = 10**9 + 7

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v, time in roads:
            graph[u].add((time, v))
            graph[v].add((time, u))

        count = defaultdict(list)
        count[0] = [0, 1]
        heap_queue = [(0, 0)]
        heapq.heapify(heap_queue)
        while heap_queue:
            time, curr = heapq.heappop(heap_queue)

            if n - 1 in count and count[n - 1][0] < time:
                continue

            for neighbor_time, neighbor in graph[curr]:
                path_time = time + neighbor_time
                if neighbor not in count or count[neighbor][0] > path_time:
                    count[neighbor] = [path_time, count[curr][1]]
                    heapq.heappush(heap_queue, (path_time, neighbor))

                elif count[neighbor][0] == path_time:
                    count[neighbor][1] += count[curr][1]

        return int(count[n - 1][1] % self.MOD)
