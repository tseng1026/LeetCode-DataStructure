# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        curr_level = 0
        number_string = ""
        for letter in traversal + "#":
            if letter.isdigit():
                number_string += letter

            else:
                if number_string:
                    while stack and stack[-1][0] >= curr_level:
                        stack.pop()

                    curr_node = TreeNode(number_string)
                    if stack and not stack[-1][1].left:
                        stack[-1][1].left = curr_node
                    elif stack and not stack[-1][1].right:
                        stack[-1][1].right = curr_node

                    stack.append((curr_level, curr_node))
                    curr_level = 0
                    number_string = ""

                curr_level += 1

        return stack[0][1]
