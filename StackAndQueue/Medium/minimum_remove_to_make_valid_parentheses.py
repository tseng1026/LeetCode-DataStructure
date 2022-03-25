# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, string: str) -> str:
        LEFT, RIGHT = "(", ")"

        stack, result = [], list(string)
        for idx, letter in enumerate(string):
            if letter == LEFT:
                stack.append(idx)

            elif letter == RIGHT:
                if len(stack) <= 0:
                    result[idx] = ""
                else:
                    stack.pop()

        while stack:
            result[stack.pop()] = ""
        return "".join(result)
