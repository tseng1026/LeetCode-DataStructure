# https://leetcode.com/problems/sum-root-to-leaf-numbers/

class Solution:
    sum_number = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumNumberHelper(root: Optional[TreeNode]) -> None:
            if not root:
                return

            if not root.left and not root.right:
                self.sum_number += root.val
                return

            for child in {root.left, root.right}:
                if child:
                    child.val += root.val * 10
                    sumNumberHelper(child)

        sumNumberHelper(root)
        return self.sum_number
