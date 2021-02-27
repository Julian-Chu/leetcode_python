from helper import TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        self.recur(root)

    def recur(self, root) -> TreeNode:
        if not root or (root.left is None and root.right is None):
            return root

        if root.right is None:
            root.right = root.left
            root.left = None
            return self.recur(root.right)

        if root.left is None:
            return self.recur(root.right)

        temp = root.right
        root.right = root.left
        root.left = None
        self.recur(root.right).right = temp
        return self.recur(temp)


