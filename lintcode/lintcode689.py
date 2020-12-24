"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        if not root:
            return

        min_node = root
        max_node = root
        while min_node.left:
            min_node = min_node.left
        while max_node.right:
            max_node = max_node.right

        while min_node != max_node:
            pivot = min_node.val + max_node.val
            if pivot == n:
                return [min_node.val, max_node.val]
            elif pivot < n:
                min_node = self.get_successor_node(root, min_node)
            else:
                max_node = self.get_predecessor_node(root, max_node)
        return []

    def get_successor_node(self, root, p):
        node, upper = root, None
        while node:
            if node.val > p.val:  # 找到比p.val大的node，繼續尋找是否有更小的目標
                upper = node
                node = node.left
            else:
                node = node.right  # node.val <=p, 切換至node.right比較
        return upper

    def get_predecessor_node(self, root, p):
        node, lower = root, None
        while node:
            if node.val < p.val:
                lower = node
                node = node.right
            else:
                node = node.left
        return lower