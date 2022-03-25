# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        paranthesis = {"(": ")", "[": "]", "{": "}"}
        for letter in string:
            if letter in paranthesis.keys():
                stack.append(letter)

            else:
                if not stack or \
                        letter != paranthesis[stack.pop()]:
                    return False

        return len(stack) == 0
