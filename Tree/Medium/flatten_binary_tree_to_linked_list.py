# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or \
                not root.left and not root.right:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        right_node = root.right
        root.right = root.left
        root.left = None

        curr = root
        while curr.right:
            curr = curr.right
        curr.right = right_node
