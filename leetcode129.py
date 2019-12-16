from helper import TreeNode


class Solution:
    cur_sum = 0

    def sumNumbers(self, root: TreeNode) -> int:

        def dfs(root, cur_val):
            if not root:
                return
            cur_val = cur_val * 10 + root.val

            if not root.left and not root.right:
                self.cur_sum += cur_val

            dfs(root.left, cur_val)
            dfs(root.right, cur_val)

        dfs(root, 0)

        return self.cur_sum
