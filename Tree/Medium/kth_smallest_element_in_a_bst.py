# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

class Solution:
    def iteration(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val

            root = root.right

    def recursion(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        return self.recursion(root.left) + [root.val] + \
            self.recursion(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.iteration(root, k)
        # return self.recursion(root)[k - 1]
