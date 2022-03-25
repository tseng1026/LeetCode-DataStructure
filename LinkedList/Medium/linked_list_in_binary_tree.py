# https://leetcode.com/problems/linked-list-in-binary-tree/

class Solution:
    def checkRemainPath(
            self,
            head: Optional[ListNode],
            root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False

        return head.val == root.val and (
            self.checkRemainPath(head.next, root.left) or
            self.checkRemainPath(head.next, root.right)
        )

    def isSubPath(
            self,
            head: Optional[ListNode],
            root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False

        return self.checkRemainPath(head, root) or (
            self.isSubPath(head, root.left) or
            self.isSubPath(head, root.right)
        )
