# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

class Node:
    def __init__(
            self,
            val: int = 0,
            left: Node = None,
            right: Node = None,
            next: Node = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root

        node_queue = deque([(0, root)])
        while node_queue:
            level, curr = node_queue.popleft()

            for child in [curr.left, curr.right]:
                if child:
                    if node_queue and \
                            node_queue[-1][0] == level + 1:
                        node_queue[-1][1].next = child
                    node_queue.append((level + 1, child))
        return root
