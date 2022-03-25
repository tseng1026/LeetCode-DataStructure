# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

class Solution:
    P, Q, NONE, BOTH = 0, 1, 2, 3
    UP, LEFT, RIGHT = "U", "L", "R"

    def lowestCommonAncestor(
            self,
            root: Optional[TreeNode],
            p: int,
            q: int) -> int:
        if not root:
            return self.NONE

        is_p_included = root.val == p
        is_q_included = root.val == q

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        is_left_included = left in {self.P, self.Q}
        is_right_included = right in {self.P, self.Q}

        if left == self.BOTH or right == self.BOTH:
            return self.BOTH

        if self.P == left or self.P == right:
            self.path[self.P] += self.UP

        if self.Q == left:
            self.path[self.Q] += self.LEFT

        if self.Q == right:
            self.path[self.Q] += self.RIGHT

        status = self.NONE
        if not is_p_included and not is_q_included:
            status = left if is_left_included else status
            status = right if is_right_included else status
            status = self.BOTH if is_left_included and is_right_included else status

        else:
            status = self.P if is_p_included else status
            status = self.Q if is_q_included else status
            status = self.BOTH if is_left_included or is_right_included else status

        return status

    def getDirections(
            self,
            root: Optional[TreeNode],
            startValue: int,
            destValue: int) -> str:
        self.path = ['', '']
        self.lowestCommonAncestor(root, startValue, destValue)
        return self.path[0] + self.path[1][::-1]
