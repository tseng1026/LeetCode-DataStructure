# https://leetcode.com/problems/balanced-binary-tree/

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        max_level = float("-inf")
        for child in {root.left, root.right}:
            if child:
                max_level = max(self.maxDepth(child) + 1, max_level)
        return max_level

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and \
            self.isBalanced(root.right)
