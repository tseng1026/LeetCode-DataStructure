# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next

        return dummy.next
