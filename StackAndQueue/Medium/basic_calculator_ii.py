# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def push_number_string(self) -> None:
        if len(self.number_string) != 0:
            number = int(self.number_string)
            self.stack.append(number if self.operand != "-" else -number)
            self.number_string = ""

    def compute(self, operand: str, val1: int, val2: int) -> int:
        if operand == "*":
            self.multiply(val1, val2)

        if operand == "/":
            self.divide(val1, val2)

    def multiply(self, val1: int, val2: int) -> None:
        self.stack.append(val1 * val2)

    def divide(self, val1: int, val2: int) -> None:
        self.stack.append(int(val1 / val2))

    def calculate(self, string: str) -> int:
        self.stack = []
        self.number_string = ""
        self.operand = ""
        for letter in string + "#":
            if letter.isspace():
                continue

            elif letter.isdigit():
                self.number_string += letter

            else:
                self.push_number_string()

                if self.operand in {"*", "/"}:
                    val2 = self.stack.pop()
                    val1 = self.stack.pop()
                    self.compute(self.operand, val1, val2)
                self.operand = letter

        return sum(self.stack)
