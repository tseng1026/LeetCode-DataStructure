# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        num1 = -heapq.heappop(nums)
        num2 = -heapq.heappop(nums)
        return (num1 - 1) * (num2 - 1)
