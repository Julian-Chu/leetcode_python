# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
from unittest import TestCase


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []

        return self.helper(1, n + 1)

    def helper(self, start, end) -> List[TreeNode]:
        if start == end:
            return [None]

        result = []
        for i in range(start, end):
            left = self.helper(start, i)
            right = self.helper(i + 1, end)
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    result.append(root)

        return result


class TestSolution(TestCase):
    def test_generateTrees(self):
        solution = Solution()
        res = solution.generateTrees(4)
        self.assertEquals(res, [])
