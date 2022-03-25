# https://leetcode.com/problems/reverse-nodes-in-k-group/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev = None
        while head and head.next:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        head.next = prev
        return head

    def reverseKGroup(
            self,
            head: Optional[ListNode],
            k: int) -> Optional[ListNode]:
        if not head:
            return head

        curr = temp = head
        for _ in range(k - 1):
            curr = curr.next
            if not curr:
                return head

        next_group = curr.next
        curr.next = None

        head = self.reverseList(head)
        temp.next = self.reverseKGroup(next_group, k)
        return head
