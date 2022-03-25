# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

class Solution:
    def nodesBetweenCriticalPoints(
            self, head: Optional[ListNode]) -> List[int]:
        if not head.next:
            return [-1]

        result = float("inf")
        first_critical_point, prev_critical_point = None, None

        idx = 1
        prev = head
        curr = head.next
        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
                    (curr.val < prev.val and curr.val < curr.next.val):
                if not first_critical_point:
                    first_critical_point = idx
                    prev_critical_point = idx

                else:
                    result = min(idx - prev_critical_point, result)
                    prev_critical_point = idx

            idx += 1
            prev = curr
            curr = curr.next

        return [result, prev_critical_point - first_critical_point] \
            if first_critical_point != prev_critical_point \
            else [-1, -1]
