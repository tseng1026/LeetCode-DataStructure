# https://leetcode.com/problems/binary-tree-cameras/

class Solution:
    def checkSubtree(self, root: Optional[TreeNode]) -> bool:
        return root is not None and root.val == 0 and \
            (root.left is None or root.left.val == 0) and \
            (root.right is None or root.right.val == 0)

    def checkSetCamera(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return

        if root.left is not None and root.left.val == 0 and \
                self.checkSubtree(root.left):
            root.val = 1

        if root.right is not None and root.right.val == 0 and \
                self.checkSubtree(root.right):
            root.val = 1

        return

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def minCameraCoverHelper(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left = minCameraCoverHelper(root.left)
            right = minCameraCoverHelper(root.right)
            self.checkSetCamera(root)
            return left + right + root.val

        return minCameraCoverHelper(root) + self.checkSubtree(root)
