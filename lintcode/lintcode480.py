"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]

        leftPaths = self.binaryTreePaths(root.left)
        rightPaths = self.binaryTreePaths(root.right)

        paths = []
        for path in leftPaths + rightPaths:
            paths.append(str(root.val) + '->' + path)

        return paths


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        if not root:
            return []
        paths = []
        self.dfs(root, [], paths)
        return paths

    def dfs(self, root, path, paths):
        if not root:
            return

        path.append(root.val)
        if not root.left and not root.right:
            paths.append("->".join([str(val) for val in path]))

        self.dfs(root.left, path, paths)
        self.dfs(root.right, path, paths)
        path.pop()



class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        if root is None:
            return []

        result = []
        self.dfs(root, [str(root.val)], result)
        return result

    def dfs(self, node, path, result):
        if node is None:
            return

        if node.left is None and node.right is None:
            result.append('->'.join(path))
            return

        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, result)
            path.pop()

        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, result)
            path.pop()
