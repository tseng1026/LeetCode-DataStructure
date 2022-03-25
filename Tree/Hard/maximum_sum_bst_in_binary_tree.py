# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

CustomTreeNode = namedtuple('Node', ["is_valid_bst", "sum", "lower", "upper"])


class Solution:
    max_sum = 0

    def getSumBST(self, root: Optional[TreeNode]) -> CustomTreeNode:
        if not root:
            return CustomTreeNode(True, 0, float("-inf"), float("inf"))

        left = self.getSumBST(root.left)
        right = self.getSumBST(root.right)

        is_valid_bst = left.is_valid_bst and right.is_valid_bst and \
            (left.upper == float("inf") or left.upper < root.val) and \
            (right.lower == float("-inf") or right.lower > root.val)
        total_sum = left.sum + right.sum + root.val
        if is_valid_bst:
            self.max_sum = max(total_sum, self.max_sum)

        lower = root.val if left.lower == float("-inf") else left.lower
        upper = root.val if right.upper == float("inf") else right.upper
        return CustomTreeNode(is_valid_bst, total_sum, lower, upper)

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.getSumBST(root)
        return self.max_sum
