# https://leetcode.com/problems/mini-parser/

class Solution:
    def deserialize(self, string: str) -> NestedInteger:
        LEFT, RIGHT, NEGATIVE, COMMA = "[", "]", "-", ","

        stack = []
        number_string = ""
        for letter in string:
            if letter.isdigit() or letter == NEGATIVE:
                number_string += letter

            elif letter == LEFT:
                stack.append(NestedInteger())

            elif letter == COMMA:
                if len(number_string) > 0:
                    nested_integer = NestedInteger(int(number_string))
                    stack[-1].add(nested_integer)
                number_string = ""

            elif letter == RIGHT:
                if len(number_string) > 0:
                    nested_integer = NestedInteger(int(number_string))
                    stack[-1].add(nested_integer)
                number_string = ""

                poppedList = stack.pop()
                if len(stack) == 0:
                    return poppedList
                stack[-1].add(poppedList)

        return NestedInteger(0)
