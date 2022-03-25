# https://leetcode.com/problems/add-one-row-to-tree/

class Solution:
    def bfs(
            self,
            root: Optional[TreeNode],
            val: int,
            depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)

        node_queue = deque([(1, root)])
        while node_queue:
            level, curr = node_queue.popleft()

            if level + 1 == depth:
                curr.left = TreeNode(val, left=curr.left)
                curr.right = TreeNode(val, right=curr.right)

            elif level + 1 > depth:
                return root

            for child in {curr.left, curr.right}:
                if child:
                    node_queue.append((level + 1, child))

    def dfs(
            self,
            root: Optional[TreeNode],
            val: int,
            depth: int) -> Optional[TreeNode]:
        if not root:
            return root

        if depth - 1 == 1:
            root.left = TreeNode(val, left=root.left)
            root.right = TreeNode(val, right=root.right)
            return root

        elif depth - 1 < 1:
            return root

        for child in {root.left, root.right}:
            self.dfs(child, val, depth - 1)
        return root

    def addOneRow(
            self,
            root: Optional[TreeNode],
            val: int,
            depth: int) -> Optional[TreeNode]:

        if not root:
            return root

        return self.bfs(root, val, depth)
        # return self.dfs(root, val, depth)
