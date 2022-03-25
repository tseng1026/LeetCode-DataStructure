# https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n: int) -> int:
        result = [1]
        for k in range(1, n + 1):
            result.append(0)
            for left in range(k):
                right = k - 1 - left
                result[k] += result[left] * result[right]
        return result[n]
