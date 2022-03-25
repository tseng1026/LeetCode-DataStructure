# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flattenHelper(curr: Optional[TreeNode]) -> Optional[TreeNode]:
            if not curr:
                return curr

            head = curr
            while curr:
                if curr.left:
                    temp = curr.right
                    curr.right = flattenHelper(curr.left)
                    curr.left = None

                    while curr.right:
                        curr = curr.right
                    curr.right = flattenHelper(temp)
                curr = curr.right
            return head
        flattenHelper(root)
