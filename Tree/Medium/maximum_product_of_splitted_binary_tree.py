# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

class Solution:
    summantion = set()

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def maxProductHelper(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            total = root.val + \
                maxProductHelper(root.left) + \
                maxProductHelper(root.right)
            self.summantion.add(total)
            return total

        result = 0
        total = maxProductHelper(root)
        for temp in self.summantion:
            result = max(temp * (total - temp), result)
        return int(result % (1e9 + 7))
