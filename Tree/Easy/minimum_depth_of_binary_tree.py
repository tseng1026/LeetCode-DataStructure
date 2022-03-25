# https://leetcode.com/problems/minimum-depth-of-binary-tree/

class Solution:
    def bfs(self, root: Optional[TreeNode]) -> int:
        min_level = float("inf")
        node_queue = deque([(1, root)])
        while node_queue:
            level, curr = node_queue.popleft()

            has_children = False
            for child in {curr.left, curr.right}:
                if child:
                    node_queue.append((level + 1, child))
                    has_children = True

            if not has_children:
                min_level = min(level, min_level)

        return min_level

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 1

        min_level = float("inf")
        for child in {root.left, root.right}:
            if child:
                min_level = min(self.dfs(child) + 1, min_level)
        return min_level

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # return self.bfs(root)
        return self.dfs(root)
