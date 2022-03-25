# https://leetcode.com/problems/split-linked-list-in-parts/

class Solution:
    def splitListToParts(self,
                         head: Optional[ListNode],
                         k: int) -> List[Optional[ListNode]]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        default_count, one_more = divmod(n, k)

        result = []
        for group in range(k):
            result.append(head)
            if not head:
                continue

            count = default_count + (group < one_more)
            for _ in range(count - 1):
                head = head.next

            temp = head.next
            head.next = None
            head = temp
        return result
