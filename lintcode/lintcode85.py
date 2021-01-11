class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        if not root:
            return node

        curr = root
        while curr != node:
            if curr.val > node.val:
                if curr.left is None:
                    curr.left = node
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = node
                curr = curr.right
        return root


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        if not root:
            return node

        if node.val > root.val:
            root.right = self.insertNode(root.right, node)
        else:
            root.left = self.insertNode(root.left, node)
        return root