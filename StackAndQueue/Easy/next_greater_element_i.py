# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(
            self,
            nums1: List[int],
            nums2: List[int]) -> List[int]:
        monotonic = []
        next_greater = defaultdict(int)
        for num in nums2:
            while monotonic and monotonic[-1] < num:
                curr_num = monotonic.pop()
                next_greater[curr_num] = num
            monotonic.append(num)

        result = []
        for num in nums1:
            if num not in next_greater:
                result.append(-1)

            else:
                result.append(next_greater[num])
        return result
