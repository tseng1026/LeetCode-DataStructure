# https://leetcode.com/problems/longest-univalue-path/

class Solution:
    longest_path = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def longestUnivaluePathHelper(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left_result = longestUnivaluePathHelper(root.left)
            right_result = longestUnivaluePathHelper(root.right)

            pass_result = 0
            unpass_result = 0

            if root.left and root.val == root.left.val:
                pass_result += left_result + 1
                unpass_result = max(left_result + 1, unpass_result)

            if root.right and root.val == root.right.val:
                pass_result += right_result + 1
                unpass_result = max(right_result + 1, unpass_result)

            self.longest_path = max(
                pass_result, unpass_result, self.longest_path)
            return unpass_result

        longestUnivaluePathHelper(root)
        return self.longest_path
