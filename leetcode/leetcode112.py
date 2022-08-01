# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from helper import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        if root.left is None and root.right is None:
            if root.val == sum:
                return True

            return False
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node: TreeNode, restSum: int) -> bool:
            if not node:
                return False

            restSum -= node.val
            if not node.left and not node.right:
                return restSum == 0

            return dfs(node.left, restSum) or dfs(node.right, restSum)

        return dfs(root, targetSum)