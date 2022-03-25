# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution:
    def removeDuplicates(self, string: str, k: int) -> str:
        stack = []
        for letter in string:
            times = 1
            while stack and stack[-1][0] == letter:
                _, curr_times = stack.pop()
                times += curr_times
            stack.append([letter, times])

            if stack[-1][1] == k:
                stack.pop()

        result = ""
        for letter, times in stack:
            result += letter * times
        return result
