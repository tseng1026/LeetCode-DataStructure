# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

class Solution:
    def findParentBfs(
            self,
            root: Optional[TreeNode],
            target: TreeNode,
            k: int):
        if not root:
            return

        parent = defaultdict(int)

        node_queue = deque([root])
        while node_queue:
            curr = node_queue.popleft()

            for child in {curr.left, curr.right}:
                if child:
                    node_queue.append(child)
                    parent[child] = curr

        visit = set([target])
        node_queue = deque([target])
        while node_queue and k > 0:
            length = len(node_queue)
            for _ in range(length):
                curr = node_queue.popleft()

                for neighbor in {curr.left, curr.right, parent[curr]}:
                    if neighbor and neighbor not in visit:
                        node_queue.append(neighbor)
                        visit.add(neighbor)

            k -= 1

        self.result = [curr.val for curr in node_queue]

    def findPathToRootDfs(
            self,
            root: Optional[TreeNode],
            target: TreeNode,
            k: int) -> bool:
        if not root:
            return False

        if root == target:
            self.path += 1
            self.findSubtreeResult(root, k - self.path + 1)
            return True

        if left := self.findPathToRootDfs(root.left, target, k):
            self.path += 1
            self.findSubtreeResult(root.right, k - self.path)

        if right := self.findPathToRootDfs(root.right, target, k):
            self.path += 1
            self.findSubtreeResult(root.left, k - self.path)

        if (left or right) and k == self.path - 1:
            self.result.append(root.val)

        return left or right

    def findSubtreeResult(self, root: Optional[TreeNode], k: int) -> None:
        if not root or k < 0:
            return

        if k == 0:
            self.result.append(root.val)

        for child in {root.left, root.right}:
            self.findSubtreeResult(child, k - 1)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.result = []

        self.findParentBfs(root, target, k)

        # self.path = 0
        # self.findPathToRootDfs(root, target, k)

        return self.result
