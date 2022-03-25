# https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = None
        while head and head.next:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        head.next = prev
        return head
