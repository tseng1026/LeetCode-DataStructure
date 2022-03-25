# https://leetcode.com/problems/reorder-list/

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

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
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

        idx = 0
        curr = dummy = ListNode()
        while fir and sec:
            if idx == 0:
                curr.next = fir
                fir = fir.next

            else:
                curr.next = sec
                sec = sec.next

            curr = curr.next
            idx = (idx + 1) % 2

        curr.next = fir if fir else sec
        return dummy.next
