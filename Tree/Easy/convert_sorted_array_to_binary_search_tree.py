# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        center_idx = len(nums) // 2
        root = TreeNode(nums[center_idx])
        root.left = self.sortedArrayToBST(nums[:center_idx])
        root.right = self.sortedArrayToBST(nums[center_idx + 1:])
        return root
