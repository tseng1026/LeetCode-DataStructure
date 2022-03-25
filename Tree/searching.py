from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Searching:
    def breadthFirstSearch(self, root: Optional[int]) -> None:
        queue = deque([(0, root)])
        while queue:
            level, curr = queue.popleft()

            for child in {root.left, root.right}:
                if child:
                    queue.append((level + 1, child))

    def depthFirstSearch(self, root: Optional[int]) -> None:
        if not root:
            # return timestamp if needed
            return

        for child in {root.left, root.right}:
            if child:
                self.depthFirstSearch(child)
