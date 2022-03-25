# https://leetcode.com/problems/validate-binary-search-tree/

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSTHelper(
                root: Optional[TreeNode],
                lower: int,
                upper: int) -> bool:
            if not root:
                return True

            if not lower < root.val < upper:
                return False

            return isValidBSTHelper(root.left, lower, root.val) and \
                isValidBSTHelper(root.right, root.val, upper)

        return isValidBSTHelper(root, float("-inf"), float("inf"))
