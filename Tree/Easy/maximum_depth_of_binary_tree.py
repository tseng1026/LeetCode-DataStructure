# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution:
    def bfs(self, root: Optional[TreeNode]) -> int:
        max_level = float("-inf")
        node_queue = deque([(1, root)])
        while node_queue:
            level, curr = node_queue.popleft()
            max_level = max(level, max_level)

            for child in {curr.left, curr.right}:
                if child:
                    node_queue.append((level + 1, child))
        return max_level

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 1

        max_level = float("-inf")
        for child in {root.left, root.right}:
            if child:
                max_level = max(self.dfs(child) + 1, max_level)
        return max_level

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # return self.bfs(root)
        return self.dfs(root)
