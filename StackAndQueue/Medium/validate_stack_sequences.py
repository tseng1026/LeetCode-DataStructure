# https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(
            self,
            pushed: List[int],
            popped: List[int]) -> bool:
        stack = []
        push_idx, pop_idx = 0, 0
        while push_idx < len(pushed) or pop_idx < len(popped):
            if stack and pop_idx < len(popped) and \
                    stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1

            elif push_idx < len(pushed):
                stack.append(pushed[push_idx])
                push_idx += 1

            else:
                break

        return not stack
