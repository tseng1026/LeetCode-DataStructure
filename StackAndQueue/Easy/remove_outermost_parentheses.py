# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, string: str) -> str:
        LEFT, RIGHT = "(", ")"

        result = ""
        stack = []
        for idx, letter in enumerate(string):
            if letter == LEFT:
                stack.append(idx)

            else:
                start = stack.pop()

                if not stack:
                    result += string[start + 1: idx]

        return result
