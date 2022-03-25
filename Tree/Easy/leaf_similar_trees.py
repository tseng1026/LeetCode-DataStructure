# https://leetcode.com/problems/leaf-similar-trees/

class Solution:
    def getLeaves(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        return self.getLeaves(root.left) + self.getLeaves(root.right)

    def leafSimilar(
            self,
            root1: Optional[TreeNode],
            root2: Optional[TreeNode]) -> bool:
        return self.getLeaves(root1) == self.getLeaves(root2)
