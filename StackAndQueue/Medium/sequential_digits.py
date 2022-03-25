# https://leetcode.com/problems/sequential-digits/

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_string, low_digits = str(low), len(str(low))
        high_string, high_digits = str(high), len(str(high))
        template = [str(k) for k in range(10)]

        result = []
        for length in range(low_digits, high_digits + 1):
            if length == low_digits:
                start = int(low_string[0])
            else:
                start = 1

            if length == high_digits:
                end = min(int(high_string[0]), 9 - length + 1)
            else:
                end = 9 - length + 1

            for k in range(start, end + 1):
                temp_result = int("".join(template[k: k + length]))
                if not low <= temp_result <= high:
                    continue

                result.append(temp_result)

        return result
