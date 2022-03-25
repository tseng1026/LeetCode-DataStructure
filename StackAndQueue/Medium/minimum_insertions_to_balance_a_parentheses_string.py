# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

class Solution:
    def minInsertions(self, string: str) -> int:
        LEFT, RIGHT = "(", ")"

        result = 0
        idx, stack = 0, 0
        while idx < len(string):
            if string[idx] == LEFT:
                stack += 1

            else:
                count = 1
                if idx + 1 < len(string) and string[idx + 1] == RIGHT:
                    count += 1
                    idx += 1

                if stack:
                    result += 2 - count
                    stack -= 1
                else:
                    result += 2 - count + 1

            idx += 1

        return result + 2 * stack
