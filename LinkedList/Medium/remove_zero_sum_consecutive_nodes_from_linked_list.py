# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

class Solution:
    def removeZeroSumSublists(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)
        prefix_map = defaultdict(ListNode)

        curr = dummy
        prefix_sum = 0
        while curr:
            prefix_sum += curr.val

            prefix_map[prefix_sum] = curr
            curr = curr.next

        curr = dummy
        prefix_sum = 0
        while curr:
            prefix_sum += curr.val

            curr.next = prefix_map[prefix_sum].next
            curr = curr.next

        return dummy.next
