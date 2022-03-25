# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacks = [[], []]
        for idx, string in enumerate([s, t]):
            for letter in string:
                if letter != "#":
                    stacks[idx].append(letter)

                else:
                    if stacks[idx]:
                        stacks[idx].pop()

        return stacks[0] == stacks[1]
