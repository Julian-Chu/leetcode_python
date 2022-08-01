class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        res = []

        def dfs(node: TreeNode, tmp: []):
            if not node:
                return
            tmp.append(node.val)
            if not node.left and not node.right:
                # to str
                path = '->'.join([str(x) for x in tmp])
                res.append(path)
                tmp.pop()
                return

            dfs(node.left, tmp)
            dfs(node.right, tmp)
            tmp.pop()

        dfs(root, [])
        return res

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        res = []
        self.dfs(root, '', res)
        return res

    def dfs(self, node: TreeNode, path: str, res: List[str]):
        path += str(node.val)
        if not node.left and not node.right:
            res.append(path)
            return

        if node.left:
            self.dfs(node.left, path + "->", res)
        if node.right:
            self.dfs(node.right, path + "->", res)


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        res = []
        stack = [root]
        paths = [str(root.val)]

        while stack:
            node = stack.pop()
            path = paths.pop()
            if not node.left and not node.right:
                res.append(path)
                continue

            if node.left:
                stack.append(node.left)
                paths.append(path + "->" + str(node.left.val))
            if node.right:
                stack.append(node.right)
                paths.append(path + "->" + str(node.right.val))

        return res