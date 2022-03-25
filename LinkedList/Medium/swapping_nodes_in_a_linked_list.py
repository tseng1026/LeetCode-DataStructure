# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

class Solution:
    def swapNodes(
            self,
            head: Optional[ListNode],
            k: int) -> Optional[ListNode]:
        total_nodes = 0
        curr = head
        while curr:
            total_nodes += 1
            curr = curr.next

        curr = head
        fir = sec = None
        for idx in range(total_nodes):
            if idx == k - 1:
                fir = curr

            if idx == total_nodes - k + 1 - 1:
                sec = curr

            curr = curr.next

        fir.val, sec.val = sec.val, fir.val
        return head
