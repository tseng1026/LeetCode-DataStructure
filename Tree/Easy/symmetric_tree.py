# https://leetcode.com/problems/symmetric-tree/

class Solution:
    def isSymmetricTree(
            self,
            p: Optional[TreeNode],
            q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSymmetricTree(p.left, q.right) and \
            self.isSymmetricTree(p.right, q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isSymmetricTree(root.left, root.right)
