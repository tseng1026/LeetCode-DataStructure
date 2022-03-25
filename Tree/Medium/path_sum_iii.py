# https://leetcode.com/problems/path-sum-iii/

class Solution:
    count_target = 0

    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> int:
        def pathSumHelper(root: Optional[TreeNode]) -> list[int]:
            if not root:
                return []

            left_results = pathSumHelper(root.left)
            right_results = pathSumHelper(root.right)

            result = [root.val]
            result += [left + root.val for left in left_results]
            result += [right + root.val for right in right_results]
            self.count_target += result.count(target_sum)
            return result

        pathSumHelper(root)
        return self.count_target
