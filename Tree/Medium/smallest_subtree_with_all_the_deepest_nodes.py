# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

class Solution:
    deepest_nodes = None
    common_ancestor_node = None

    def findDeepestNodes(self, root: Optional[TreeNode]) -> None:
        node_queue = deque([root])
        while node_queue:
            length = len(node_queue)
            self.deepest_nodes = [node_queue[0], node_queue[-1]]

            for _ in range(length):
                curr = node_queue.popleft()

                for child in {curr.left, curr.right}:
                    if child:
                        node_queue.append(child)

    def lowestCommonAncestor(
            self,
            root: Optional[TreeNode],
            p: Optional[TreeNode],
            q: Optional[TreeNode]) -> bool:
        if not root:
            return False

        node = root == p or root == q
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if node + left + right >= 2:
            self.common_ancestor_node = root

        return node or left or right

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.findDeepestNodes(root)
        if self.deepest_nodes[0] == self.deepest_nodes[1]:
            return self.deepest_nodes[0]

        self.lowestCommonAncestor(
            root,
            self.deepest_nodes[0],
            self.deepest_nodes[1])
        return self.common_ancestor_node
