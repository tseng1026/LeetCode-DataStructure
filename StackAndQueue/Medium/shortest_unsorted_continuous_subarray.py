# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        increasing = []
        for idx in range(len(nums)):
            if not increasing or increasing[-1] <= nums[idx]:
                increasing.append(nums[idx])

            else:
                minima = min(nums[idx:])
                while increasing and increasing[-1] > minima:
                    increasing.pop()
                break

        decreasing = []
        for idx in range(len(nums) - 1, -1, -1):
            if not decreasing or decreasing[-1] >= nums[idx]:
                decreasing.append(nums[idx])

            else:
                maxima = max(nums[:idx + 1])
                while decreasing and decreasing[-1] < maxima:
                    decreasing.pop()
                break

        return max(0, len(nums) - len(increasing) - len(decreasing))
