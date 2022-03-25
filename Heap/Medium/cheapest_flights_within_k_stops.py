# https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self,
                          n: int,
                          flights: List[List[int]],
                          src: int,
                          dst: int,
                          k: int) -> int:
        graph = defaultdict(set)
        for from_city, to_city, price in flights:
            graph[from_city].add((price, to_city))

        visit = defaultdict(list)
        visit[src] = (0, 0)

        node_heapq = [(0, 0, src)]
        heapq.heapify(node_heapq)
        while node_heapq:
            price, stops, city = heapq.heappop(node_heapq)

            if city == dst:
                return price
            if stops > k:
                continue

            for neighbor_price, neighbor in graph[city]:
                path_price = price + neighbor_price
                path_stops = stops + 1

                if neighbor not in visit or \
                        path_price <= visit[neighbor][0] or \
                        path_stops <= visit[neighbor][1]:
                    visit[neighbor] = [path_price, path_stops]
                    heapq.heappush(
                        node_heapq, (path_price, path_stops, neighbor))
        return -1
