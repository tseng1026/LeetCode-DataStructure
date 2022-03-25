# https://leetcode.com/problems/odd-even-linked-list/

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        idx = 0
        odd_head, even_head = ListNode(), ListNode()
        odd_even = [odd_head, even_head]
        while head:
            odd_even[idx].next = head

            odd_even[idx] = odd_even[idx].next
            head = head.next
            idx = (idx + 1) % 2

        odd_even[0].next = even_head.next
        odd_even[1].next = None
        return odd_head.next
