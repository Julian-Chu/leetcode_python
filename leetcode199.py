# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from helper import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        ls = self.rightSideView(root.left)
        rs = self.rightSideView(root.right)

        if len(ls) > len(rs):
            rs = rs + ls[len(rs):]

        res = [root.val] + rs

        return res
