# https://leetcode.com/problems/next-greater-node-in-linked-list/

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        idx, monotonic = 0, []
        next_larger = defaultdict(int)
        while head:
            while monotonic and monotonic[-1][1] < head.val:
                curr_idx, _ = monotonic.pop()
                next_larger[curr_idx] = head.val
            monotonic.append((idx, head.val))

            idx += 1
            head = head.next

        return [next_larger[k] for k in range(idx)]
