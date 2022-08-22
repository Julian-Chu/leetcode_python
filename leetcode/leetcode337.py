class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(cur: TreeNode) -> List[int]:
            if not cur:
                return [0, 0]

            left = dfs(cur.left)
            right = dfs(cur.right)

            taken = cur.val + left[0] + right[0]
            nottaken = max(left) + max(right)

            return [nottaken, taken]

        return max(dfs(root))