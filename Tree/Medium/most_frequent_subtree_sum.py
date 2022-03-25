# https://leetcode.com/problems/most-frequent-subtree-sum/

class Solution:
    def findTreeSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        tree_sum = root.val
        for child in {root.left, root.right}:
            tree_sum += self.findTreeSum(child)

        self.tree_sum_frequency[tree_sum] += 1
        return tree_sum

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.tree_sum_frequency = defaultdict(int)
        self.findTreeSum(root)

        highest_frequency = max(self.tree_sum_frequency.values())
        return [key for key, freq in self.tree_sum_frequency.items()
                if freq == highest_frequency]
