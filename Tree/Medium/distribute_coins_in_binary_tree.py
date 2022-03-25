# https://leetcode.com/problems/distribute-coins-in-binary-tree/

class Solution:
    movement = 0

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def distributeCoinsHelper(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left = distributeCoinsHelper(root.left)
            right = distributeCoinsHelper(root.right)
            self.movement += abs(left) + abs(right)
            return root.val + left + right - 1

        distributeCoinsHelper(root)
        return self.movement
