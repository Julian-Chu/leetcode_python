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
    @return: the maximum weight node
    """

    def findSubtree(self, root):
        if root is None:
            return None
        subtree_sum_node = {}
        subtree_sum, max_sum = self.divideConquer(root, subtree_sum_node)
        # print(max_sum)
        return subtree_sum_node[max_sum]

    def divideConquer(self, root, subtree_sum_node):
        if root is None:
            return 0, 0

        if root.left is None and root.right is None:
            subtree_sum_node[root.val] = root
            return root.val, root.val

        left_sum, left_max_sum = self.divideConquer(root.left, subtree_sum_node)
        right_sum, right_max_sum = self.divideConquer(root.right, subtree_sum_node)

        root_sum = root.val + left_sum + right_sum
        # print(root_sum, left_max_sum, right_max_sum)
        if max(root_sum, left_max_sum, right_max_sum) == root_sum:
            subtree_sum_node[root_sum] = root
        return root_sum, max(root_sum, left_max_sum, right_max_sum)


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
    @return: the maximum weight node
    """
    result = None
    maximum_weight = 0

    def findSubtree(self, root):
        if root is None:
            return None
        self.helper(root)
        return self.result

    def helper(self, root):
        if root is None:
            return 0

        left_weight = self.helper(root.left)
        right_weight = self.helper(root.right)

        root_sum = left_weight + right_weight + root.val
        if root_sum > self.maximum_weight or self.result is None:
            self.maximum_weight = root_sum
            self.result = root

        return root_sum


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
    @return: the maximum weight node
    """
    result = None
    maximum_weight = 0

    def findSubtree(self, root):
        if root is None:
            return None
        self.helper(root)
        return self.result

    def helper(self, root):
        if root is None:
            return 0

        left_weight = self.helper(root.left)
        right_weight = self.helper(root.right)

        root_sum = left_weight + right_weight + root.val
        if root_sum > self.maximum_weight or self.result is None:
            self.maximum_weight = root_sum
            self.result = root

        return root_sum