# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            if curr.child is not None:
                temp = curr
                next_node = temp.next

                temp.next = self.flatten(temp.child)
                temp.next.prev = temp
                temp.child = None

                while temp and temp.next:
                    temp = temp.next
                temp.next = next_node
                if next_node:
                    next_node.prev = temp
            curr = curr.next
        return head
