# https://leetcode.com/problems/sort-list/

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        fir = head
        sec = slow.next
        slow.next = None

        curr = dummy = ListNode()
        fir = self.sortList(fir)
        sec = self.sortList(sec)

        while fir and sec:
            if fir.val <= sec.val:
                curr.next = fir
                fir = fir.next

            else:
                curr.next = sec
                sec = sec.next

            curr = curr.next

        curr.next = fir if fir else sec
        return dummy.next
