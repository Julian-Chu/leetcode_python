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
        self.paths = []

        path = [root.val]
        self.findPaths(root, path)
        path.pop()
        return self.paths

    def findPaths(self, node, path):
        if not node:
            return

        if not node.left and not node.right:
            self.paths.append("->".join([str(val) for val in path]))
            return

        if node.left:
            path.append(node.left.val)
            self.findPaths(node.left, path)
            path.pop()

        if node.right:
            path.append(node.right.val)
            self.findPaths(node.right, path)
            path.pop()

        return


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
