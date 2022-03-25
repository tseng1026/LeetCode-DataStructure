# https://leetcode.com/problems/clumsy-factorial/

class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        operation = ["*", "/", "+", "-"]
        for op_idx, k in enumerate(range(n - 1, 0, -1)):
            if operation[op_idx % 4] == "+":
                stack.append(k)

            elif operation[op_idx % 4] == "-":
                stack.append(-k)

            elif operation[op_idx % 4] == "*":
                stack.append(stack.pop() * k)

            elif operation[op_idx % 4] == "/":
                stack.append(int(stack.pop() / k))
        return sum(stack)
