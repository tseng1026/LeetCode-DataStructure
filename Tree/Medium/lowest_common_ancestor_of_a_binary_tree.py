# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

class Solution:
    common_ancestor_node = None

    def iteration(
            self,
            root: Optional[TreeNode],
            p: Optional[TreeNode],
            q: Optional[TreeNode]) -> None:
        one_node_found = False
        lca_index, stack = None, []
        while not self.common_ancestor_node:
            while root:
                stack.append([root, False])
                root = root.left

            curr, done_status = stack[-1]
            if done_status:
                stack.pop()
                if lca_index:
                    lca_index = min(len(stack) - 1, lca_index)
                root = None

            else:
                if curr == p or curr == q:
                    if one_node_found:
                        self.common_ancestor_node = stack[lca_index][0]
                        break

                    else:
                        one_node_found = True
                        lca_index = len(stack) - 1

                stack[-1][1] = True
                root = curr.right

    def recursion(
            self,
            root: Optional[TreeNode],
            p: Optional[TreeNode],
            q: Optional[TreeNode]) -> bool:
        if not root:
            return False

        node = root == p or root == q
        left = self.recursion(root.left, p, q)
        right = self.recursion(root.right, p, q)
        if node + left + right >= 2:
            self.common_ancestor_node = root

        return node or left or right

    def lowestCommonAncestor(
            self,
            root: Optional[TreeNode],
            p: Optional[TreeNode],
            q: Optional[TreeNode]) -> Optional[TreeNode]:

        self.recursion(root, p, q)
        # self.iteration(root, p, q)
        return self.common_ancestor_node
