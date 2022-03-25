# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

class Solution:
    longest_path = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        LEFT, RIGHT = 0, 1

        def longestZigZagHelper(
                root: Optional[TreeNode],
                direction: int) -> int:
            if not root:
                return 0

            passed_result = 0
            unpassed_result = 0

            if direction == LEFT:
                passed_result = longestZigZagHelper(root.left, RIGHT) + 1
                unpassed_result = longestZigZagHelper(root.left, LEFT)

            else:
                passed_result = longestZigZagHelper(root.right, LEFT) + 1
                unpassed_result = longestZigZagHelper(root.right, RIGHT)

            self.longest_path = max(
                passed_result - 1,
                unpassed_result - 1,
                self.longest_path)
            return passed_result

        longestZigZagHelper(root, LEFT)
        longestZigZagHelper(root, RIGHT)
        return self.longest_path
