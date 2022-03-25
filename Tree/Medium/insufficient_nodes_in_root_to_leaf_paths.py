# https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

class Solution:
    def sufficientSubset(
            self,
            root: Optional[TreeNode],
            limit: int) -> Optional[TreeNode]:
        def sufficientSubsetHelper(
                root: Optional[TreeNode],
                limit: int) -> bool:
            if not root:
                return False

            if root and not root.left and not root.right:
                return root.val >= limit

            if not (
                left := sufficientSubsetHelper(
                    root.left,
                    limit - root.val)):
                root.left = None

            if not (
                right := sufficientSubsetHelper(
                    root.right,
                    limit - root.val)):
                root.right = None

            return left or right

        result = sufficientSubsetHelper(root, limit)
        return root if result else None
