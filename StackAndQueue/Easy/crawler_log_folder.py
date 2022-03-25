# https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0
        for log in logs:
            if log == "./":
                continue

            elif log == "../":
                result = max(0, result - 1)

            else:
                result += 1
        return result
