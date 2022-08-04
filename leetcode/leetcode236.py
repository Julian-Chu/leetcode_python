class Solution:
    # if p or q not exist
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        (res, _, _) = self.find(root, p, q)
        return res

    def find(self, node: TreeNode, p: TreeNode, q: TreeNode) -> (TreeNode, bool, bool):
        if not node:
            return None, False, False

        (leftAncestor, p_found_left, q_found_left) = self.find(node.left, p, q)
        (rightAncestor, p_found_right, q_found_right) = self.find(node.right, p, q)
        if leftAncestor and p_found_left and q_found_left:
            return leftAncestor, True, True
        if rightAncestor and p_found_right and q_found_right:
            return rightAncestor, True, True

        if (p_found_left and q_found_right) or (p_found_right and q_found_left):
            return node, True, True

        if node == p:
            return node, True, (q_found_left or q_found_right)

        if node == q:
            return node, (p_found_left or p_found_right), True

        return None, p_found_left or p_found_right, q_found_left or q_found_right


class Solution:
    # p and q must exist
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root

        if left:
            return left
        if right:
            return right

        return None