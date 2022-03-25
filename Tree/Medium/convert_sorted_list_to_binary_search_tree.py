# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.next.val)
        fast = slow.next.next
        slow.next = None
        slow = head
        root.left = self.sortedListToBST(slow)
        root.right = self.sortedListToBST(fast)
        return root
