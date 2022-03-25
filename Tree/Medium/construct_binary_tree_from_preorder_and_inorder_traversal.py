# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

class Solution:
    def buildTree(
            self,
            preorder: List[int],
            inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return root
