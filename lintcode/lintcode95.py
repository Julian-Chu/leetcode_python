class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        if not root:
            return True

        stack = []
        while root:
            stack.append(root)
            root = root.left

        last_node = stack[-1]
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                if stack[-1].val <= last_node.val:
                    return False
                last_node = stack[-1]

        return True


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        if not root:
            return True

        return self.helper(root, -float('inf'), float('inf'))

    def helper(self, node, min_val, max_val):
        if not node:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return self.helper(node.left, min_val, node.val) and self.helper(node.right, node.val, max_val)