# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from unittest import TestCase

from helper import TreeNode


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.push(root)

    def next(self) -> int:
        node = self.stack.pop()
        self.push(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def push(self, root: TreeNode):
        while root:
            self.stack.append(root)
            root = root.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
class TestBSTIterator(TestCase):
    def test_hasNext(self):
        node = TreeNode(1)
        it = BSTIterator(node)
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 1)
        self.assertFalse(it.hasNext())
