# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))

            except BaseException:
                val2 = stack.pop()
                val1 = stack.pop()

                if token == "+":
                    stack.append(val1 + val2)

                elif token == "-":
                    stack.append(val1 - val2)

                elif token == "*":
                    stack.append(val1 * val2)

                elif token == "/":
                    stack.append(int(val1 / val2))

        return stack.pop()
