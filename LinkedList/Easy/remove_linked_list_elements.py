# https://leetcode.com/problems/remove-linked-list-elements/

class Solution:
    def removeElements(
            self,
            head: Optional[ListNode],
            val: int) -> Optional[ListNode]:
        curr = dummy = ListNode(-1, head)
        while curr:
            next_node = curr.next
            while next_node and next_node.val == val:
                next_node = next_node.next

            curr.next = next_node
            curr = curr.next
        return dummy.next


class Solution:
    def removeElements(
            self,
            head: Optional[ListNode],
            val: int) -> Optional[ListNode]:
        if not head:
            return head

        curr = dummy = ListNode(-1, head)
        while curr and curr.next:
            if val == curr.next.val:
                curr.next = self.removeElements(curr.next.next, val)

            curr = curr.next
        return dummy.next
