# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

class Solution:
    def smallestSubsequence(self, string: str) -> str:
        counter = Counter(string)
        monotonic = []
        for letter in string:
            counter[letter] -= 1
            if letter in monotonic:
                continue

            while monotonic and \
                    monotonic[-1] > letter and \
                    counter[monotonic[-1]] > 0:
                monotonic.pop()
            monotonic.append(letter)

        return "".join(monotonic)
