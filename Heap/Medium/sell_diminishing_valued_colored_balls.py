# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

class Solution:
    MOD = 10**9 + 7

    def maxProfit(self, inventory: List[int], orders: int) -> int:
        counter = Counter(inventory)
        heap = [(-remains, count)
                for remains, count in counter.items()] + [(0, 0)]
        heapq.heapify(heap)

        result = 0
        while heap and orders > 0:
            fir_remains, fir_count = heapq.heappop(heap)
            sec_remains, sec_count = heapq.heappop(heap)

            height = abs(sec_remains - fir_remains)
            width = fir_count
            rest = 0
            if width * height > orders:
                height, rest = map(int, divmod(orders, width))

            result += width * (-fir_remains * height - height *
                               (height - 1) // 2) + rest * (-fir_remains - height)

            orders -= width * height + rest

            if orders > 0:
                heapq.heappush(heap, (sec_remains, fir_count + sec_count))

        return int(result % self.MOD)
