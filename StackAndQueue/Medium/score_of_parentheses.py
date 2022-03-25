# https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, string: str) -> int:
        LEFT, RIGHT = "(", ")"

        stack = []
        for letter in string:
            if letter == LEFT:
                stack.append(LEFT)

            else:
                temp_score = 0
                while stack and stack[-1] != LEFT:
                    temp_score += stack.pop()
                stack.pop()

                if temp_score == 0:
                    stack.append(1)

                else:
                    stack.append(2 * temp_score)

        return sum(stack)
