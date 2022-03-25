# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ZERO = "0"

        monotonic = []
        for digit in num:
            while k > 0 and \
                    monotonic and monotonic[-1] > digit:
                monotonic.pop()
                k -= 1

            if not monotonic and digit == ZERO:
                continue
            monotonic.append(digit)

        return ZERO if k >= len(monotonic) else "".join(
            monotonic[:len(monotonic) - k])
