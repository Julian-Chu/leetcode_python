"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """

    def __init__(self, root):
        self.stack = []
        self.find_most_left(root)

    """
    @return: True if there has next node, or false
    """

    def hasNext(self):
        return len(self.stack) > 0

    """
    @return: return next node
    """

    def next(self):
        node = self.stack.pop()
        if node.right is not None:
            self.find_most_left(node.right)

        return node

    def find_most_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """

    def __init__(self, root):
        self.stack = []
        self.find_most_left(root)

    """
    @return: True if there has next node, or false
    """

    def hasNext(self):
        return len(self.stack) > 0

    """
    @return: return next node
    """

    def next(self):
        node = self.stack[-1]
        if node.right is not None:
            self.find_most_left(node.right)
        else:
            n = self.stack.pop()
            while len(self.stack) > 0 and self.stack[-1].right == n:
                n = self.stack.pop()

        return node

    def find_most_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

