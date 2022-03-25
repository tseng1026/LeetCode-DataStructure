# https://leetcode.com/problems/copy-list-with-random-pointer/

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        mapping = {None: None}

        curr = head
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            mapping[curr].next = mapping[curr.next]
            mapping[curr].random = mapping[curr.random]
            curr = curr.next
        return mapping[head]
