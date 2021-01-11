class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def invertBinaryTree(self, root):
        if not root:
            return
        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)
        root.left, root.right = root.right, root.left
