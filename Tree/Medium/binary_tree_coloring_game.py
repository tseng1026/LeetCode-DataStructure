# https://leetcode.com/problems/binary-tree-coloring-game/

class Solution:
    def countNodes(self, root: Optional[TreeNode], target: int) -> int:
        if not root:
            return 0

        left = self.countNodes(root.left, target)
        right = self.countNodes(root.right, target)
        if root.val == target:
            self.left_nodes = left
            self.right_nodes = right
        return left + right + 1

    def btreeGameWinningMove(
            self,
            root: Optional[TreeNode],
            n: int,
            x: int) -> bool:
        self.left_nodes = 0
        self.right_nodes = 0
        self.countNodes(root, x)
        self.parent_nodes = n - self.left_nodes - self.right_nodes - 1

        max_colored_nodes = max(
            self.left_nodes,
            self.right_nodes,
            self.parent_nodes)
        return max_colored_nodes > n // 2
