# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

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

    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        fir = head
        sec = self.reverseList(slow.next)
        slow.next = None

        result = float("-inf")
        while fir and sec:
            result = max(fir.val + sec.val, result)
            fir = fir.next
            sec = sec.next
        return result
