class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum2(self, root, target):
        if not root:
            return []
        paths = []
        self.dfs(root, [], paths, 0, target)
        return paths

    def dfs(self, root, path, paths, index, target):
        if root == None:
            return
        path.append(root.val)
        tmp = target
        for i in range(index, -1, -1):
            tmp -= path[i]
            if tmp == 0:
                paths.append(path[i:])

        self.dfs(root.left, path, paths, index + 1, target)
        self.dfs(root.right, path, paths, index + 1, target)
        path.pop()