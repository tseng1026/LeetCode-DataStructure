# https://leetcode.com/problems/merge-bsts-to-create-single-bst/

class Solution:
    def validBSTSize(
            self,
            root: Optional[TreeNode],
            lower: int,
            upper: int) -> int:
        if not root:
            return 0

        if not lower < root.val < upper:
            return float("-inf")

        left = self.validBSTSize(root.left, lower, root.val)
        right = self.validBSTSize(root.right, root.val, upper)
        return left + right + 1

    def bfs(self, root: Optional[TreeNode]) -> bool:
        node_queue = deque([root])
        while node_queue:
            curr = node_queue.popleft()

            for child in {curr.left, curr.right}:
                if child:
                    if child.val in self.nodes:
                        return False

                    self.nodes[child.val] = child
                    node_queue.append(child)
        return True

    def dfs(self, root: Optional[TreeNode]) -> bool:
        result = True
        for child in {root.left, root.right}:
            if child:
                if child.val in self.nodes:
                    return False

                self.nodes[child.val] = child
                result = result and self.dfs(child)
        return result

    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        roots = set(trees)

        self.nodes = defaultdict(TreeNode)
        for tree in trees:
            if not self.bfs(tree):
                # if not self.dfs(tree):
                return None

        ancestor = None
        for root in roots:
            if root.val not in self.nodes:
                if not ancestor:
                    ancestor = root
                else:
                    return None

            replace = self.nodes[root.val]
            replace.left = root.left
            replace.right = root.right

        result = self.validBSTSize(ancestor, float("-inf"), float("inf"))
        return ancestor if result == len(self.nodes) else None
