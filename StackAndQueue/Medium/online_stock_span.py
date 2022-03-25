# https://leetcode.com/problems/online-stock-span/

class StockSpanner:
    def __init__(self):
        self.monotonic = []

    def next(self, price: int) -> int:
        temp = 1
        while self.monotonic and self.monotonic[-1][0] <= price:
            temp += self.monotonic.pop()[1]
        self.monotonic.append((price, temp))
        return temp
