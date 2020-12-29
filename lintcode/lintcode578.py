"""
top-down

"""
class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        if not self.find_node(root, A) or not self.find_node(root, B):
            return None

        if self.find_node(root.left, A) and self.find_node(root.left, B):
            return self.lowestCommonAncestor3(root.left, A, B)
        if self.find_node(root.right, A) and self.find_node(root.right, B):
            return self.lowestCommonAncestor3(root.right, A, B)
        return root

    def find_node(self, root, node):
        if root is None:
            return False

        if root == node:
            return True

        return self.find_node(root.left, node) or self.find_node(root.right, node)

"""
bad bottom-up
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        a, b, lca = self.helper(root, A, B)
        if a and b:
            return lca
        return None

    def helper(self, root, A, B):
        if root is None:
            return False, False, None

        found_a_left, found_b_left, lca_left = self.helper(root.left, A, B)
        found_a_right, found_b_right, lca_right = self.helper(root.right, A, B)
        if root == A:
            if found_b_left or found_b_right:
                return True, True, root
            return True, False, None

        if root == B:
            if found_a_left or found_a_right:
                return True, True, root
            return False, True, None

        if found_a_right and found_b_right:
            return True, True, lca_right

        if found_a_left and found_b_left:
            return True, True, lca_left
        if (found_a_left or found_a_right) and (found_b_left or found_b_right):
            return True, True, root

        return found_a_left or found_a_right, found_b_left or found_b_right, None


"""
better bottom-up
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        a, b, lca = self.helper(root, A, B)
        if a and b:
            return lca
        return None

    def helper(self, root, A, B):
        if root is None:
            return False, False, None

        a_left, b_left, left_node = self.helper(root.left, A, B)
        a_right, b_right, right_node = self.helper(root.right, A, B)

        a = a_left or a_right or root == A
        b = b_left or b_right or root == B

        if root == A or root == B:
            return a, b, root

        if left_node and right_node:
            return a, b, root
        if left_node:
            return a, b, left_node
        if right_node:
            return a, b, right_node
        return a, b, None
