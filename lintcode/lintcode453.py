"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    prevNode = None

    def flatten(self, root):
        if not root:
            return

        if self.prevNode is not None:
            self.prevNode.left = None
            self.prevNode.right = root

        self.prevNode = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def flatten(self, root):
        self.flatten_root(root)
        return root

    def flatten_root(self, root):
        tail = None
        if root is None or (root.left is None and root.right is None):
            return root
        elif root.left is None:
            tail = self.flatten_root(root.right)
        elif root.right is None:
            tail = self.flatten_root(root.left)
            root.right = root.left
            root.left = None
        else:
            left_tail = self.flatten_root(root.left)
            tail = self.flatten_root(root.right)
            left_tail.right = root.right
            root.right = root.left
            root.left = None

        return tail


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def flatten(self, root):
        self.flatten_and_return_last_node(root)

    def flatten_and_return_last_node(self, root):
        if root is None:
            return None

        left_last = self.flatten_and_return_last_node(root.left)
        right_last = self.flatten_and_return_last_node(root.right)

        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None

        return right_last or left_last or root
