# https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            try:
                stack.append(int(op))

            except BaseException:
                if op == "C":
                    stack.pop()

                elif op == "D":
                    stack.append(stack[-1] * 2)

                elif op == "+":
                    stack.append(stack[-1] + stack[-2])
        return sum(stack)
