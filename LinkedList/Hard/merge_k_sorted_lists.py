# https://leetcode.com/problems/merge-k-sorted-lists/

class Solution:
    def mergeKLists(self,
                    lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        node_queue = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(node_queue)

        while node_queue:
            _, idx = heapq.heappop(node_queue)

            curr.next = lists[idx]
            curr = curr.next
            lists[idx] = lists[idx].next

            if lists[idx]:
                heapq.heappush(node_queue, (lists[idx].val, idx))
        return dummy.next
