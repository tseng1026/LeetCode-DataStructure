# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, string: str) -> str:
        stack = []
        for letter in string:
            if stack and stack[-1] == letter:
                stack.pop()

            else:
                stack.append(letter)
        return "".join(stack)
