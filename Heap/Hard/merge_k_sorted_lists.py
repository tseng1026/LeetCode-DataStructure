# https://leetcode.com/problems/merge-k-sorted-lists/

class Solution:
    def mergeKLists(self,
                    lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(lists[idx].val, idx)
                for idx in range(len(lists)) if lists[idx]]
        heapq.heapify(heap)

        dummy = curr = ListNode()
        while heap:
            _, idx = heapq.heappop(heap)
            curr.next = lists[idx]
            curr = curr.next

            lists[idx] = lists[idx].next
            if lists[idx] is not None:
                heapq.heappush(heap, (lists[idx].val, idx))

        return dummy.next
