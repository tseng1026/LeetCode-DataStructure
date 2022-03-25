# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

class Solution:
    MOD = 10**9 + 7

    def numOfWays(self, nums: List[int]) -> int:
        def numOfWaysHelper(nums: List[int]) -> int:
            if len(nums) <= 2:
                return 1

            left_nums, right_nums = [], []
            for num in nums:
                if num < nums[0]:
                    left_nums.append(num)

                if num > nums[0]:
                    right_nums.append(num)

            left = numOfWaysHelper(left_nums)
            right = numOfWaysHelper(right_nums)

            return left * right * \
                math.comb(len(left_nums) + len(right_nums), len(left_nums))

        return int((numOfWaysHelper(nums) - 1) % self.MOD)
