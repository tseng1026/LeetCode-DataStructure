# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

class Solution:
    def kSmallestPairs(self,
                       nums1: List[int],
                       nums2: List[int],
                       k: int) -> List[List[int]]:
        pair = list(product(nums1[:k], nums2[:k]))
        pair_sum = [(num1 + num2, [num1, num2]) for num1, num2 in pair]
        heapq.heapify(pair_sum)

        return [heapq.heappop(pair_sum)[1] for _ in range(k) if pair_sum]
