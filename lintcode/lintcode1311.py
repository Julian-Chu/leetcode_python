"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """

    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None

        if root == p or root == q:
            return root

        if p.val > q.val:
            p, q = q, p

        if p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        if q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return root