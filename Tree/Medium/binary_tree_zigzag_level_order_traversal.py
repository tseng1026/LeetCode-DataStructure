# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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

        return [result[k] if k % 2 == 0 else reversed(result[k])
                for k in range(len(result))]
