"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """

    def removeNode(self, root, value):
        if not root:
            return root

        if value > root.val:
            root.right = self.removeNode(root.right, value)
            return root
        elif value < root.val:
            root.left = self.removeNode(root.left, value)
            return root
        else:
            next_node = self.find_next(root)
            if next_node == None:
                return None
            # print('next',next_node, next_node.left, next_node.right)
            if next_node != root.left:
                next_node.left = root.left
            if next_node != root.right:
                next_node.right = root.right
            root.left = None
            root.right = None
            root = None
            print('next', next_node, next_node.left, next_node.right)
            return next_node

    def inorder(self, root):
        stack = []
        while root:
            stack.append(root)
            root = root.left

        res = []
        while stack:
            node = stack.pop()
            print(node.val)
            res.append(node)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        return res

    def find_next(self, root):
        if root.right:
            node = root.right
            prev = node
            while node.left:
                prev = node
                node = node.left

            prev.left = node.right
            return node
        elif root.left:
            node = root.left
            prev = node
            while node.right:
                prev = node
                node = node.right
            prev.right = node.left
            return node
        else:
            return None