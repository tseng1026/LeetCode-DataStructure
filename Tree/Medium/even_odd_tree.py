# https://leetcode.com/problems/even-odd-tree/

class Solution:
    def bfs(self, root: Optional[TreeNode]) -> bool:
        level = 0
        node_queue = deque([root])
        while node_queue:
            length = len(node_queue)

            prev = None
            for _ in range(length):
                curr = node_queue.popleft()

                if curr.val % 2 != (level + 1) % 2:
                    return False

                if prev and \
                        ((level % 2 == 0 and prev.val >= curr.val) or
                         (level % 2 == 1 and prev.val <= curr.val)):
                    return False
                prev = curr

                for child in [curr.left, curr.right]:
                    if child:
                        node_queue.append(child)

            level += 1

        return True

    def dfs(self, level: int, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if root.val % 2 != (level + 1) % 2:
            return False

        if level in self.prev_node:
            prev = self.prev_node[level]
            if (level % 2 == 0 and prev.val >= root.val) or \
               (level % 2 == 1 and prev.val <= root.val):
                return False
        self.prev_node[level] = root

        return self.dfs(level + 1, root.left) and \
            self.dfs(level + 1, root.right)

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        return self.bfs(root)

        # self.prev_node = defaultdict(list)
        # return self.dfs(0, root)
