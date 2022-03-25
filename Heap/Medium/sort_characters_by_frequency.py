# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, string: str) -> str:
        counter = Counter(string)
        frequency = [(-count, letter) for letter, count in counter.items()]

        result = ""
        heapq.heapify(frequency)
        while frequency:
            count, letter = heapq.heappop(frequency)
            result += letter * -count
        return result
