class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = ListNode()  # dummyhead is helpful

    def search(self, idx: int) -> int:
        curr = self.head
        for k in range(idx + 1):
            curr = curr.next
            if not curr:
                raise IndexError
        return curr.val

    def insert(self, idx: int, val: int) -> None:
        curr = self.head
        for k in range(idx):
            curr = curr.next
            if not curr:
                raise IndexError
        temp = curr.next
        curr.next = ListNode(val, temp)

    def delete(self, idx: int) -> None:
        curr = self.head
        for k in range(idx):
            curr = curr.next
            if not curr:
                raise IndexError
        if not curr.next:
            raise IndexError
        curr.next = curr.next.next if curr.next else None
