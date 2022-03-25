# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, string: str) -> str:
        LEFT, RIGHT = "[", "]"

        stack = []
        number_string = ""
        for letter in string:
            if letter.isdigit():
                number_string += letter

            elif letter.isalpha():
                stack.append(letter)

            elif letter == LEFT:
                stack.append(int(number_string))
                number_string = ""

            else:
                temp_string = ""
                while stack and not isinstance(stack[-1], int):
                    temp_string = stack.pop() + temp_string
                stack.append(temp_string * stack.pop())

        return "".join(stack)
