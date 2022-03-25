# https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

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

    def reverseByLength(
            self,
            head: Optional[ListNode],
            k: int) -> Optional[ListNode]:
        if not head:
            return head

        curr = temp = head
        for count in range(k - 1):
            curr = curr.next
            if not curr:
                if (count + 1) % 2 == 0:
                    return self.reverseList(head)
                else:
                    return head

        if k % 2 == 0:
            next_group = curr.next
            curr.next = None

            head = self.reverseList(head)
            temp.next = self.reverseByLength(next_group, k + 1)

        else:
            curr.next = self.reverseByLength(curr.next, k + 1)

        return head

    def reverseEvenLengthGroups(
            self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseByLength(head, 1)
