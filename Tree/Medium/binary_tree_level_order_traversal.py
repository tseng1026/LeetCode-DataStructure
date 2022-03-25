# https://leetcode.com/problems/binary-tree-level-order-traversal/

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = defaultdict(list)
        result[0].append(root.val)
        node_queue = deque([(0, root)])
        while node_queue:
            level, curr = node_queue.popleft()

            for neighbor in [curr.left, curr.right]:
                if neighbor:
                    node_queue.append((level + 1, neighbor))
                    result[level + 1].append(neighbor.val)

        return [result[k] for k in range(len(result))]
