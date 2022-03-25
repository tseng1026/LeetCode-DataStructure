# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, string: str) -> int:
        LEFT, RIGHT, DUMMY = "(", ")", "#"

        result = 0
        stack = []

        def calculateScore():
            temp_result = 0
            while stack and stack[-1] != LEFT:
                temp_result += stack.pop()

            if stack:
                stack.pop()
            return temp_result

        for letter in string + DUMMY:
            if letter == LEFT:
                stack.append(LEFT)

            else:
                if LEFT in stack and letter != DUMMY:
                    temp_result = calculateScore()
                    stack.append(temp_result + 2)

                else:
                    while stack:
                        temp_result = calculateScore()
                        result = max(temp_result, result)
                    stack = []

        return result
