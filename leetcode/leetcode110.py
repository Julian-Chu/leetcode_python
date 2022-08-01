# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def getHeight(node: TreeNode) -> int:
            if not node:
                return 0

            left = getHeight(node.left)
            right = getHeight(node.right)

            return max(left, right) + 1

        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        if abs(getHeight(root.left) - getHeight(root.right)) <= 1:
            return True

        return False