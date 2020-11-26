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
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):
        upper, lower = root.val, root.val

        while root:
            if root.val > target:
                upper = root.val
                root = root.left
            elif root.val < target:
                lower = root.val
                root = root.right
            else:
                return root.val

        if abs(upper - target) <= abs(lower - target):
            return upper
        return lower