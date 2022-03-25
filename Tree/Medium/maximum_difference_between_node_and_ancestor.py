# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def maxAncestorDiffHelper(
                root: Optional[TreeNode],
                maxima: int,
                minima: int) -> None:
            if not root:
                self.result = max(maxima - minima, self.result)
                return

            maxima = max(root.val, maxima)
            minima = min(root.val, minima)
            maxAncestorDiffHelper(root.left, maxima, minima)
            maxAncestorDiffHelper(root.right, maxima, minima)

        self.result = -1
        maxAncestorDiffHelper(root, float("-inf"), float("inf"))
        return self.result
