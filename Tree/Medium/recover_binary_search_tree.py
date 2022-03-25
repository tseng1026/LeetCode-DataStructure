# https://leetcode.com/problems/recover-binary-search-tree/

class Solution:
    def recursion(self, root: Optional[TreeNode]) -> list[TreeNode]:
        if not root:
            return []

        return self.recursion(root.left) + [root] + \
            self.recursion(root.right)

    def iteration(self, root: Optional[TreeNode]) -> list[TreeNode]:
        if not root:
            return []

        result = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root)

            root = root.right
        return result

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        traversal = self.iteration(root)
        template = sorted(traversal, key=lambda x: x.val)
        different = [
            node1 for node1,
            node2 in zip(
                traversal,
                template) if node1 != node2]
        different[0].val, different[1].val = different[1].val, different[0].val
