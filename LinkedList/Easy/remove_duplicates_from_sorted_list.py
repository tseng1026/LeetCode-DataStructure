# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            val = curr.val
            temp = curr.next
            while temp and temp.val == val:
                temp = temp.next

            curr.next = temp
            curr = curr.next
        return head
