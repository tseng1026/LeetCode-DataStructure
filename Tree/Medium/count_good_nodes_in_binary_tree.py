# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

class Solution:
    good_notes = 0

    def bfs(self, root: Optional[TreeNode]) -> None:
        node_queue = deque([(root.val, root)])
        while node_queue:
            maxima, curr = node_queue.popleft()

            if curr.val >= maxima:
                self.good_notes += 1
            maxima = max(curr.val, maxima)

            for child in {curr.left, curr.right}:
                if child:
                    node_queue.append((maxima, child))

    def dfs(self, root: Optional[TreeNode], maxima: int) -> None:
        if not root:
            return

        if root.val >= maxima:
            self.good_notes += 1
        maxima = max(root.val, maxima)

        self.dfs(root.left, maxima)
        self.dfs(root.right, maxima)

    def goodNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # self.bfs(root)
        self.dfs(root, root.val)

        return self.good_notes
