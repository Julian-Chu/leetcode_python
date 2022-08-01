class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = 0
        left = root.left
        while left:
            left_depth += 1
            left = left.left

        right_depth = 0
        right = root.right
        while right:
            right_depth += 1
            right = right.right

        if left_depth == right_depth:
            return (2 << left_depth) - 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1