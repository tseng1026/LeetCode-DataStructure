from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, target: int) -> bool:
        return self.searchHelper(self.root, target)

    def searchHelper(self, node: Optional[TreeNode], target: int) -> bool:
        if not node:
            return False

        if target == node.val:
            return True

        elif target < node.val:
            return self.searchHelper(node.left, target)

        elif target > node.val:
            return self.searchHelper(node.right, target)

    def insert(self, target: int) -> None:
        self.insertHelper(self.root, target)

    def insertHelper(self, node: Optional[TreeNode], target: int) -> TreeNode:
        if not node:
            temp = TreeNode(target)
            if not self.root:
                self.root = temp
            return temp

        if target == node.val:
            raise ValueError

        elif target < node.val:
            node.left = self.insertHelper(node.left, target)

        elif target > node.val:
            node.right = self.insertHelper(node.right, target)

        return node

    def delete(self, target: int) -> None:
        self.deleteHelper(self.root, target)

    def deleteHelper(self, node: Optional[TreeNode], target: int) -> TreeNode:
        if not node:
            raise IndexError

        if target == node.val:
            if node.left and node.right:
                node.val = self.findMax(node.left)
                node.left = self.deleteHelper(node.left, node.val)
            elif node.left:
                return node.left
            elif node.right:
                return node.right
            else:
                return None

        elif target < node.val:
            node.left = self.deleteHelper(node.left, target)

        elif target > node.val:
            node.right = self.deleteHelper(node.right, target)

        return node

    def findMin(self, node: Optional[TreeNode]) -> int:
        if node.left:
            return self.findMin(node.left)
        return node.val

    def findMax(self, node: Optional[TreeNode]) -> int:
        if node.right:
            return self.findMax(node.right)
        return node.val

    def traverse(self) -> List[int]:
        return self.traverseHelper(self.root)

    def traverseHelper(self, node: Optional[TreeNode]) -> List[int]:
        if not node:
            return []

        return self.traverseHelper(node.left) + \
            [node.val] + self.traverseHelper(node.right)
