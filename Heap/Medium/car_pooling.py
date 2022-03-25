# https://leetcode.com/problems/car-pooling/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pick_up = [(src, dest, num) for num, src, dest in trips]
        heapq.heapify(pick_up)

        drop_off = []
        heapq.heapify(drop_off)

        curr_passenger = 0
        while pick_up:
            src, dest, num = heapq.heappop(pick_up)
            heapq.heappush(drop_off, (dest, num))
            curr_passenger += num

            while drop_off and drop_off[0][0] <= src:
                _, num = heapq.heappop(drop_off)
                curr_passenger -= num

            if curr_passenger > capacity:
                return False
        return True
