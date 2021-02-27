# Definition for a binary tree node.
from typing import List
from unittest import TestCase


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur is not None or len(stack) > 0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            if len(stack) > 0:
                cur = stack[len(stack) - 1]
                res.append(cur.val)
                stack = stack[:len(stack) - 1]
                cur = cur.right
        return res


class TestSolution(TestCase):
    def test_inorderTraversal(self):
        case1 = TreeNode(1)
        case1.right = TreeNode(2)
        case1.right.left = TreeNode(3)
        test_cases = [
            {
                "name": "case1",
                "input": case1,
                "expected": [1, 3, 2]
            },
        ]
        solution = Solution();
        for ts in test_cases:
            self.assertEqual(solution.inorderTraversal(ts["input"]), ts["expected"], ts["name"])
