# https://leetcode.com/problems/invert-binary-tree/

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root

        root.left, root.right = \
            self.invertTree(root.right), \
            self.invertTree(root.left)
        return root
