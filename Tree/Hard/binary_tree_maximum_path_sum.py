# https://leetcode.com/problems/binary-tree-maximum-path-sum/

class Solution:
    max_path_sum = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxPathSumHelper(root: Optional[TreeNode]) -> int:
            if not root:
                return float("-inf")

            left = maxPathSumHelper(root.left)
            right = maxPathSumHelper(root.right)

            self.max_path_sum = max(
                max(left + right, left, right, 0) + root.val,
                self.max_path_sum
            )

            return max(left, right, 0) + root.val

        maxPathSumHelper(root)
        return self.max_path_sum
