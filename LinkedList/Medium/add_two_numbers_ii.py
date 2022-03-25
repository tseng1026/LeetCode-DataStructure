# https://leetcode.com/problems/add-two-numbers-ii/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head and head.next:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        head.next = prev
        return head

    def addTwoNumbers(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        carrier = 0
        curr = head = ListNode()
        while l1 or l2 or carrier:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carrier, val = divmod(val1 + val2 + carrier, 10)
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return self.reverseList(head.next)
