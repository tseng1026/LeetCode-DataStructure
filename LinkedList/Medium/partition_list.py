# https://leetcode.com/problems/partition-list/

class Solution:
    def partition(
            self,
            head: Optional[ListNode],
            x: int) -> Optional[ListNode]:
        curr = head
        smaller_head = smaller = ListNode()
        greater_head = greater = ListNode()
        while curr:
            if curr.val < x:
                smaller.next = curr
                smaller = smaller.next

            else:
                greater.next = curr
                greater = greater.next

            curr = curr.next

        smaller.next = greater_head.next
        greater.next = None
        return smaller_head.next
