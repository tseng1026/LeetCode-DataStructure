# https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        heap = [(-count, num) for num, count in counter.items()]
        heapq.heapify(heap)

        result, result_length = 0, 0
        length = len(arr)
        while result_length < length // 2:
            count, curr = heapq.heappop(heap)
            result_length += -count
            result += 1

        return result
