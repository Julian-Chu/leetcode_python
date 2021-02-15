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


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum2(self, root, target):
        if not root:
            return []
        result = []
        self.dfs(root, [], result, target)
        return result

    def dfs(self, root, path, result, target):
        if root is None:
            return

        path.append(root.val)

        sum = 0
        for i in range(len(path) - 1, -1, -1):
            sum += path[i]
            if sum == target:
                result.append(path[i:])

        self.dfs(root.left, path, result, target)
        self.dfs(root.right, path, result, target)
        path.pop()