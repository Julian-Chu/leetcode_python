from helper import TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        l = self.minDepth(root.left)
        r = self.minDepth(root.right)

        if root.left is None or root.right is None:
            return max(l, r) + 1

        return min(l, r) + 1
