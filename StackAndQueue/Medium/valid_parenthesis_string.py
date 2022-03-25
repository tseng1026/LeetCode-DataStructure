# https://leetcode.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, string: str) -> bool:
        LEFT, RIGHT = "(", ")"

        count = 0
        for idx in range(len(string)):
            if string[idx] != RIGHT:
                count += 1
            else:
                count -= 1

            if count < 0:
                return False

        count = 0
        for idx in range(len(string) - 1, -1, -1):
            if string[idx] != LEFT:
                count += 1
            else:
                count -= 1

            if count < 0:
                return False

        return True
