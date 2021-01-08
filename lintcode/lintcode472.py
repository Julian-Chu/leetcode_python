class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum3(self, root, target):
        results = []
        self.dfs(root, target, results)
        return results

    def dfs(self, root, target, results):
        if root is None:
            return

        path = []
        self.findSum(root, None, target, path, results)

        self.dfs(root.left, target, results)
        self.dfs(root.right, target, results)

    def findSum(self, root, prev, target, path, results):
        path.append(root.val)
        target -= root.val  # 有可能sum在最後的路徑也為0

        if target == 0:
            results.append(path[:])

        if root.parent not in [None, prev]:
            self.findSum(root.parent, root, target, path, results)
        if root.left not in [None, prev]:
            self.findSum(root.left, root, target, path, results)
        if root.right not in [None, prev]:
            self.findSum(root.right, root, target, path, results)

        path.pop()