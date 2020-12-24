class Solution:
    """
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree
    """

    def trimBST(self, root, minimum, maximum):
        root = self.get_tree_greater_and_equal(root, minimum)
        root = self.get_tree_smaller_and_equal(root, maximum)
        return root

    def get_tree_greater_and_equal(self, root, minimum):
        if not root:
            return None

        if root.val < minimum:
            return self.get_tree_greater_and_equal(root.right, minimum)
        elif root.val == minimum:
            root.left = None
        else:  # root.val > minimum
            root.left = self.get_tree_greater_and_equal(root.left, minimum)
        return root

    def get_tree_smaller_and_equal(self, root, maximum):
        if not root:
            return None

        if root.val > maximum:
            return self.get_tree_smaller_and_equal(root.left, maximum)
        elif root.val == maximum:
            root.right = None
        else:
            root.right = self.get_tree_smaller_and_equal(root.right, maximum)
        return root


