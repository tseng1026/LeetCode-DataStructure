# https://leetcode.com/problems/basic-calculator-iii/

class Solution:
    def push_number_string(self) -> None:
        if len(self.number_string) != 0:
            number = int(self.number_string)
            self.stack.append(number if self.operand != "-" else -number)
            self.number_string = ""

    def push_operand(self) -> None:
        if len(self.operand) != 0:
            self.stack.append(self.operand)
            self.operand = ""

    def pop_till_parenthesis(self) -> int:
        temp_number = 0
        while self.stack:
            token = self.stack.pop()
            if token == "(":
                break

            temp_number += token
        return temp_number

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

            elif letter not in {"(", ")"}:
                self.push_number_string()

                if self.operand in {"*", "/"}:
                    val2 = self.stack.pop()
                    val1 = self.stack.pop()
                    self.compute(self.operand, val1, val2)
                self.operand = letter

            elif letter == "(":
                self.push_operand()
                self.stack.append(letter)

            elif letter == ")":
                self.push_number_string()
                if self.operand in {"*", "/"}:
                    val2 = self.stack.pop()
                    val1 = self.stack.pop()
                    self.compute(self.operand, val1, val2)
                self.operand = ""

                temp_number = self.pop_till_parenthesis()

                if self.stack and \
                        self.stack[-1] in {"+", "-", "*", "/"}:
                    temp_operand = self.stack.pop()
                    if temp_operand in {"*", "/"}:
                        self.compute(
                            temp_operand, self.stack.pop(), temp_number)
                    else:
                        self.stack.append(
                            temp_number if temp_operand != "-" else -temp_number)

                else:
                    self.stack.append(temp_number)

        return sum(self.stack)
