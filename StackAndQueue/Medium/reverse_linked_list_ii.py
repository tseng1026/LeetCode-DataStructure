# https://leetcode.com/problems/reverse-linked-list-ii/

class Solution:
    def reverseBetween(
            self,
            head: Optional[ListNode],
            left: int,
            right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(0, head)

        curr = dummy
        while left - 1:
            curr = curr.next
            left -= 1
            right -= 1
        front = curr
        curr = curr.next

        prev = None
        while right - 1:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            right -= 1
        back = curr.next
        curr.next = prev

        front.next.next = back
        front.next = curr
        return dummy.next
