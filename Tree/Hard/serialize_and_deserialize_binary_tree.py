# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

class Codec:
    NONE = "#"

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        result = ""
        node_queue = deque([root])
        while node_queue:
            curr = node_queue.popleft()

            if not curr:
                result += f"{self.NONE},"

            else:
                result += f"{curr.val},"

                for child in [curr.left, curr.right]:
                    node_queue.append(child)

        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        data = data.split(",")[:-1]

        root = TreeNode(data[0])

        idx, node_queue = 0, deque([root])
        while idx < len(data):
            length = len(node_queue)
            for k in range(2 ** idx):
                idx += 1
                if idx >= len(data):
                    break

                if data[idx] == self.NONE:
                    continue

                curr = TreeNode(data[idx])
                node_queue.append(curr)

                if idx % 2 == 1:
                    node_queue[(idx - 1) // 2].left = curr

                if idx % 2 == 0:
                    node_queue[(idx - 1) // 2].right = curr
        return root
