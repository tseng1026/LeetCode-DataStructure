# https://leetcode.com/problems/relative-ranks/

class Solution:
    top_ranking = ["Gold Medal", "Silver Medal", "Bronze Medal"]

    def getRanking(self, place: int) -> str:
        if place < len(self.top_ranking):
            return self.top_ranking[place]
        return str(place + 1)

    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        scores = [(-1 * score, idx) for idx, score in enumerate(scores)]
        heapq.heapify(scores)

        place = 0
        result = defaultdict(int)
        while scores:
            _, idx = heapq.heappop(scores)
            result[idx] = self.getRanking(place)
            place += 1
        return [result[place] for place in range(len(scores))]
