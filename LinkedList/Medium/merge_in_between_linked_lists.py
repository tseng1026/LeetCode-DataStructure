# https://leetcode.com/problems/merge-in-between-linked-lists/

class Solution:
    def mergeInBetween(
        self,
        list1: ListNode,
        a: int,
        b: int,
            list2: ListNode) -> ListNode:
        curr = list1
        prev_a = None
        next_b = None
        for idx in range(b + 2):
            if idx == a - 1:
                prev_a = curr

            if idx == b + 1:
                next_b = curr

            curr = curr.next

        curr = list2
        prev_a.next = list2
        while curr and curr.next:
            curr = curr.next
        curr.next = next_b

        return list1
