# https://leetcode.com/problems/swap-nodes-in-pairs/

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = None
        node1 = head
        node2 = head.next
        while node1 and node2:
            temp = node2.next
            node2.next = node1
            node1.next = temp

            if prev:
                prev.next = node2
            else:
                head = node2

            prev = node1
            node1 = prev.next
            node2 = prev.next.next if prev.next else None
        return head
