# https://leetcode.com/problems/house-robber-iii/

class Solution:
    @cache
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        link, skip = 0, root.val
        for child in {root.left, root.right}:
            if child:
                link += self.rob(child)
                skip += self.rob(child.left) + self.rob(child.right)
        return max(link, skip)
