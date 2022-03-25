# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, string: str) -> int:
        A, B = "a", "b"

        delete_a = string.count(A)
        delete_b = 0
        result = delete_b + delete_a
        for letter in string:
            if letter == A:
                delete_a -= 1
            else:
                delete_b += 1

            result = min(delete_b + delete_a, result)

        return result
