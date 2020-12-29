"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """

    def inorderPredecessor(self, root, p):
        if not root:
            return None

        stack = []

        while root:
            stack.append(root)
            root = root.left
        last = None
        while stack:
            node = stack[-1]
            if node == p:
                return last

            last = node

            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            else:
                node = stack.pop()
                while stack[-1].right == node:
                    node = stack.pop()

        return None


class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """

    def inorderPredecessor(self, root, p):
        if not root:
            return None

        predecessor = None
        while root:
            if root.val < p.val:
                predecessor = root
                root = root.right
            else:
                root = root.left
        return predecessor
