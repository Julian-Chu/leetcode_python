"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        if not root:
            return []

        paths = []
        self.dfs(root, [], paths, target)
        return paths

    def dfs(self, node, path, paths, target):
        if node is None:
            return

        target = target - node.val
        path.append(node.val)
        if not node.left and not node.right:
            if target == 0:
                paths.append(path[:])
        self.dfs(node.left, path, paths, target)
        self.dfs(node.right, path, paths, target)
        path.pop()