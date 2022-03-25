# https://leetcode.com/problems/intersection-of-two-linked-lists/

class Solution:
    def getIntersectionNode(
            self,
            head_a: ListNode,
            head_b: ListNode) -> Optional[ListNode]:
        curr_a = head_a
        curr_b = head_b
        while curr_a != curr_b:
            curr_a = curr_a.next if curr_a else head_b
            curr_b = curr_b.next if curr_b else head_a
        return curr_a
