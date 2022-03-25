# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events)

        heap = []
        heapq.heapify(heap)

        result, days = 0, 0
        while heap or events:
            days += 1

            while events and events[0][0] == days:
                heapq.heappush(heap, events.pop(0)[1])

            while heap and heap[0] < days:
                heapq.heappop(heap)

            if heap:
                heapq.heappop(heap)
                result += 1

        return result
