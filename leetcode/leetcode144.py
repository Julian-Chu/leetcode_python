# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from helper import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        node = root
        res = []
        stack = []
        while node:
            res.append(node.val)
            if node.left:
                if node.right:
                    stack.append(node.right)
                node = node.left
            else:
                if node.right:
                    node = node.right
                else:
                    if len(stack) == 0:
                        break
                    else:
                        node = stack[-1]
                        stack = stack[:-1]

        return res


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []

        def traverse(node: TreeNode):
            if node is None:
                return

            res.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return res