"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        sum_of_subtree, min_sum, root_of_min = self.getMinSubtree(root)
        return root_of_min

    def getMinSubtree(self, root):

        if root is None:
            return 0, sys.maxsize, None

        sum_of_left, min_sum_left, root_of_min_left = self.getMinSubtree(root.left)
        sum_of_right, min_sum_right, root_of_min_right = self.getMinSubtree(root.right)

        sum_of_root = root.val + sum_of_left + sum_of_right

        min_sum = min(sum_of_root, min_sum_left, min_sum_right)
        if min_sum == min_sum_left:
            return sum_of_root, min_sum_left, root_of_min_left
        elif min_sum == min_sum_right:
            return sum_of_root, min_sum_right, root_of_min_right
        return sum_of_root, sum_of_root, root


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        self.minimum_weight = float('inf')
        self.minimum_subtree_root = None
        self.getTreeSum(root)
        return self.minimum_subtree_root

    def getTreeSum(self, root):

        if root is None:
            return 0

        left_weight = self.getTreeSum(root.left)
        right_weight = self.getTreeSum(root.right)

        root_weight = root.val + left_weight + right_weight

        if root_weight < self.minimum_weight:
            self.minimum_weight = root_weight
            self.minimum_subtree_root = root

        return root_weight