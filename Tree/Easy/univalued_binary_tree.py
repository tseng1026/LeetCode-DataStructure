# https://leetcode.com/problems/univalued-binary-tree/

class Solution:
    def bfs(self, root: Optional[TreeNode]) -> bool:
        value = root.val
        node_queue = deque([root])
        while node_queue:
            curr = node_queue.popleft()

            if curr.val != value:
                return False

            for child in {curr.left, curr.right}:
                if child:
                    node_queue.append(child)
        return True

    def dfs(self, root: Optional[TreeNode]) -> bool:
        for child in {root.left, root.right}:
            if child:
                if root.val != child.val or \
                        not self.isUnivalTree(child):
                    return False
        return True

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.bfs(root)
        # return self.dfs(root)
