# https://leetcode.com/problems/longest-absolute-file-path/

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = [(-1, 0)]
        max_length = 0
        for directory in input.split("\n"):
            level = directory.count("\t")

            while stack[-1][0] >= level:
                stack.pop()
            length = len(directory) - level + stack[-1][1]

            if "." in directory:
                max_length = max(length, max_length)

            else:
                stack.append((level, length + 1))

        return max_length
