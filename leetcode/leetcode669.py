class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val < low:
            right = self.trimBST(root.right, low, high)
            return right

        if root.val > high:
            left = self.trimBST(root.left, low, high)
            return left

        root.right = self.trimBST(root.right, low, high)
        root.left = self.trimBST(root.left, low, high)
        return root