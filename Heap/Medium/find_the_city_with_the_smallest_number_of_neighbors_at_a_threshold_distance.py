# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self,
                    n: int,
                    edges: List[List[int]],
                    distance_threshold: int) -> int:
        graph = defaultdict(set)
        for u, v, weight in edges:
            graph[u].add((weight, v))
            graph[v].add((weight, u))

        result_neighbors, result = float("inf"), -1
        for city in range(n):
            temp_result = -1

            visit = set()
            heap_queue = [(0, city)]
            heapq.heapify(heap_queue)
            while heap_queue:
                distance, curr = heapq.heappop(heap_queue)

                if distance > distance_threshold:
                    break

                if curr in visit:
                    continue

                visit.add(curr)
                temp_result += 1

                for neighbor_distance, neighbor in graph[curr]:
                    path_distance = distance + neighbor_distance
                    if path_distance > distance_threshold:
                        continue

                    if neighbor not in visit:
                        heapq.heappush(heap_queue, (path_distance, neighbor))

            if temp_result <= result_neighbors:
                result_neighbors = temp_result
                result = city

        return result
