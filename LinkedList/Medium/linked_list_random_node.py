# https://leetcode.com/problems/linked-list-random-node/

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        scope, chosen_value = 1, 0
        curr = self.head
        while curr:
            if random.random() < 1.0 / scope:
                chosen_value = curr.val

            scope += 1
            curr = curr.next
        return chosen_value
