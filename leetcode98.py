# Definition for a binary tree node.
from unittest import TestCase

from helper import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.isValidSubBST(root, None, None)

    def isValidSubBST(self, root, lower, upper) -> bool:
        if not root:
            return True
        if lower is not None and root.val <= lower:
            return False
        if upper is not None and root.val >= upper:
            return False
        if not self.isValidSubBST(root.left, lower, root.val):
            return False
        if not self.isValidSubBST(root.right, root.val, upper):
            return False
        return True


class TestSolution(TestCase):
    def test_isValidBST(self):
        case1 = TreeNode(0)
        case1.right = TreeNode(-1)
        testcases = [
            {
                "root": case1,
                "expected": False
            }
        ]
        solution = Solution()
        for ts in testcases:
            self.assertEqual(ts["expected"], solution.isValidBST(ts["root"]))
