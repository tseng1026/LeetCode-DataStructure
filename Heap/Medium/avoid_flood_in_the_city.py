# https://leetcode.com/problems/avoid-flood-in-the-city/

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        rain_lake = defaultdict(list)
        for time, rain in enumerate(rains):
            if rain == 0:
                continue
            rain_lake[rain].append(time)

        full = set()
        heap, result = [], []
        heapq.heapify(heap)
        for rain in rains:
            if rain == 0:
                if not heap:
                    result.append(1)
                    continue

                _, rain = heapq.heappop(heap)
                full.discard(rain)
                result.append(rain)

            else:
                if rain in full:
                    return []

                result.append(-1)
                full.add(rain)

                rain_lake[rain].pop(0)
                if rain_lake[rain]:
                    heapq.heappush(heap, (rain_lake[rain][0], rain))

        return result
