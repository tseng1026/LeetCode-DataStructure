# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        frequency = [(-count, num) for num, count in counter.items()]
        heapq.heapify(frequency)

        return [heapq.heappop(frequency)[1] for _ in range(k)]
