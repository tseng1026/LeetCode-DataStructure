# https://leetcode.com/problems/palindrome-linked-list/

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        temp = slow
        prev = None
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next

        fir_head = head
        sec_head = prev
        while fir_head and sec_head:
            if fir_head.val != sec_head.val:
                return False

            fir_head = fir_head.next
            sec_head = sec_head.next
        return True
