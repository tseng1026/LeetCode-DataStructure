# https://leetcode.com/problems/basic-calculator/

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
                self.operand = letter

            elif letter == "(":
                self.push_operand()
                self.stack.append(letter)

            elif letter == ")":
                self.push_number_string()
                self.operand = ""

                temp_number = self.pop_till_parenthesis()
                if self.stack and not isinstance(self.stack[-1], int):
                    temp_operand = self.stack.pop()

                    if temp_operand == "-":
                        temp_number = -temp_number
                self.stack.append(temp_number)

        return sum(self.stack)
