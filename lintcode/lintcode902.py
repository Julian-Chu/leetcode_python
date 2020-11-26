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
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):
        stack = []
        while root:
            stack.append(root)
            root = root.left

        for _ in range(k - 1):
            node = stack.pop()
            n = node.right
            while n:
                stack.append(n)
                n = n.left

        return stack[-1].val


class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):
        stack = []
        while root:
            stack.append(root)
            root = root.left

        for _ in range(k - 1):
            node = stack[-1]
            if node.right is not None:
                n = node.right
                while n:
                    stack.append(n)
                    n = n.left
            else:
                node = stack.pop()
                while len(stack) > 0 and stack[-1].right == node:
                    node = stack.pop()

        return stack[-1].val