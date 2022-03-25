# https://leetcode.com/problems/count-nodes-with-the-highest-score/

class Solution:
    def getSubtreeSize(self, root: int) -> int:
        if root in self.subtree_size:
            return self.subtree_size[root]

        result = 0
        for child in self.tree[root]:
            result += self.getSubtreeSize(child)
        self.subtree_size[root] = result + 1
        return result + 1

    def countHighestScoreNodes(self, parents: List[int]) -> int:
        self.tree = defaultdict(list)
        for idx, parent in enumerate(parents):
            self.tree[parent].append(idx)

        self.subtree_size = defaultdict(int)
        self.getSubtreeSize(-1)

        result = []
        total_nodes = len(parents)
        for k in range(total_nodes):
            group_size = []
            group_size.append(total_nodes - self.subtree_size[k])
            for child in self.tree[k]:
                group_size.append(self.subtree_size[child])

            result.append(1)
            for size in group_size:
                if size != 0:
                    result[k] *= size

        max_score = max(result)
        return result.count(max_score)
