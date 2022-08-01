import collections


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])

        res = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == 0:
                    res = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        res = 0
        max_depth = -1

        def dfs(node: TreeNode, depth: int):
            nonlocal max_depth, res
            if not node.left and not node.right:
                if depth > max_depth:
                    max_depth = depth
                    res = node.val

            if node.left:
                dfs(node.left, depth + 1)

            if node.right:
                dfs(node.right, depth + 1)

        dfs(root, 0)

        return res


class Solution:
    def __init__(self):
        self.res = 0
        self.max_depth = -1

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0)
        return self.res

    def dfs(self, node: TreeNode, depth: int):
        if not node.left and not node.right:
            if depth > self.max_depth:
                self.max_depth = depth
                self.res = node.val

        if node.left:
            self.dfs(node.left, depth + 1)

        if node.right:
            self.dfs(node.right, depth + 1)