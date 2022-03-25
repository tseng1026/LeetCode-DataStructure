# https://leetcode.com/problems/unique-binary-search-trees-ii/

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def generateTreesHelper(lower: int,
                                upper: int) -> List[Optional[TreeNode]]:
            if upper == lower:
                return [TreeNode(lower)]

            if upper < lower:
                return [None]

            result = []
            for k in range(lower, upper + 1):
                left_results = generateTreesHelper(lower, k - 1)
                right_results = generateTreesHelper(k + 1, upper)

                child_results = list(product(left_results, right_results))
                for left, right in child_results:
                    result.append(TreeNode(k, left, right))
            return result

        return generateTreesHelper(1, n)
