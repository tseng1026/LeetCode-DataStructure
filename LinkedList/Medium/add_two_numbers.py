# https://leetcode.com/problems/add-two-numbers/

class Solution:
    def addTwoNumbers(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = head = ListNode()
        carrier = 0
        while l1 or l2 or carrier:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carrier, val = divmod(val1 + val2 + carrier, 10)
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next
