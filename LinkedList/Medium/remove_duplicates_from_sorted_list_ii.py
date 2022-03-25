# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(104, head)
        curr = head
        while curr:
            next_node = curr.next
            while next_node and next_node.val == curr.val:
                next_node = next_node.next

            if next_node == curr.next:
                prev = curr
            else:
                prev.next = next_node
            curr = next_node

        return dummy.next
