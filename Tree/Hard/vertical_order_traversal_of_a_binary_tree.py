# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

class Solution:
    def bfs(self, root: Optional[TreeNode]) -> None:
        node_queue = deque([(0, 0, root)])
        while node_queue:
            x, y, curr = node_queue.popleft()
            self.vertical[x].append((y, curr.val))

            for idx, child in enumerate([curr.left, curr.right]):
                if child:
                    node_queue.append((x + idx * 2 - 1, y + 1, child))

    def dfs(self, root: Optional[TreeNode], x: int, y: int) -> None:
        if not root:
            return

        self.vertical[x].append((y, root.val))
        self.dfs(root.left, x - 1, y + 1)
        self.dfs(root.right, x + 1, y + 1)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.vertical = defaultdict(list)
        self.bfs(root)
        # self.dfs(root, 0, 0)

        result = []
        for key in sorted(self.vertical.keys()):
            nodes = sorted(self.vertical[key])
            result.append([val for _, val in nodes])
        return result
