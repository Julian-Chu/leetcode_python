from helper import TreeNode


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)

    def dfs(self, root: TreeNode, sum: int):
        if not root:
            return sum
        sum *= 10
        sum += root.val
        if not root.left and not root.right:
            return sum
        res = 0
        if root.left:
            res += self.dfs(root.left, sum)
        if root.right:
            res += self.dfs(root.right, sum)

        return res
