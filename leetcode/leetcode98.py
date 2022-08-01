# Definition for a binary tree node.
from unittest import TestCase

from helper import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        prev = None

        while stack:
            node = stack.pop()

            if node:
                if node.right:
                    stack.append(node.right)

                stack.append(node)
                stack.append(None)

                if node.left:
                    stack.append(node.left)
            else:
                node = stack.pop()
                if not prev:
                    prev = node
                else:
                    if prev.val >= node.val:
                        return False
                    prev = node
        return True
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, (-1 << 31) - 1, 1 << 31)

    def helper(self, root: TreeNode, min_val: int, max_val: int) -> bool:
        if not root:
            return True

        if root.val <= min_val or root.val >= max_val:
            return False

        return self.helper(root.left, min_val, root.val) and self.helper(root.right, root.val, max_val)

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
