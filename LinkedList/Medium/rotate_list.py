# https://leetcode.com/problems/rotate-list/

class Solution:
    def rotateRight(
            self,
            head: Optional[ListNode],
            k: int) -> Optional[ListNode]:
        if not head:
            return head

        length = 1
        tail = head
        while tail and tail.next:
            tail = tail.next
            length += 1
        tail.next = head

        temp = head
        for _ in range(length - (k % length) - 1):
            temp = temp.next
        head = temp.next
        temp.next = None
        return head
