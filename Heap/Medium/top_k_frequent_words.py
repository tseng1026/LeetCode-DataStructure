# https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        frequency = [(-count, word) for word, count in counter.items()]
        heapq.heapify(frequency)

        return [heapq.heappop(frequency)[1] for _ in range(k)]
