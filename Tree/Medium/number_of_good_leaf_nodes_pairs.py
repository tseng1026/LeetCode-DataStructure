# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

class Solution:
    good_nodes_pair = 0

    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        def countPairsHelper(root: Optional[TreeNode]) -> [int]:
            if not root:
                return []

            if not root.left and not root.right:
                return [0]

            left_distance = countPairsHelper(root.left)
            right_distance = countPairsHelper(root.right)

            for left in left_distance:
                for right in right_distance:
                    if left + right + 2 <= self.distance:
                        self.good_nodes_pair += 1

            return [distance + 1 for distance in left_distance if distance < self.distance] + \
                [distance + 1 for distance in right_distance if distance < self.distance]

        self.distance = distance
        depth = countPairsHelper(root)
        return self.good_nodes_pair
