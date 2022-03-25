# https://leetcode.com/problems/maximum-width-of-binary-tree/

class Solution:
    max_width = 0

    def bfs(self, root: Optional[TreeNode]) -> None:
        if not root:
            return 0

        self.max_width = 1
        node_queue = deque([(0, root)])
        while node_queue:
            length = len(node_queue)
            for _ in range(length):
                index, curr = node_queue.popleft()

                for direction, child in enumerate([curr.left, curr.right]):
                    if child:
                        node_queue.append((2 * index + direction, child))

            if node_queue:
                width = node_queue[-1][0] - node_queue[0][0] + 1
                self.max_width = max(width, self.max_width)
                node_queue = deque(node_queue)

    def dfs(self, level: int, index: int, root: Optional[TreeNode]) -> None:
        if not root:
            return

        if level not in self.first_index:
            self.first_index[level] = index
            self.max_width = max(1, self.max_width)
        else:
            width = index - self.first_index[level] + 1
            self.max_width = max(width, self.max_width)

        for direction, child in enumerate([root.left, root.right]):
            if child:
                self.dfs(level + 1, 2 * index + direction, child)

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.bfs(root)

        # self.first_index = defaultdict(int)
        # self.dfs(0, 0, root)

        return self.max_width
