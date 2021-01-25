"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """

    def removeNode(self, root, value):
        ans, found = self.inorder(root, value)
        if not found:
            return root
        return self.build(ans, 0, len(ans) - 1)

    def inorder(self, root, value):
        found = False
        if root is None:
            return [], False
        lefts, left_found = self.inorder(root.left, value)
        if root.val != value:
            lefts.append(root.val)
        else:
            found = True
        rights, right_found = self.inorder(root.right, value)
        return lefts + rights, left_found or right_found or found

    def build(self, nums, l, r):
        if l > r:
            return None
        if l == r:
            node = TreeNode(nums[l])
            return node

        mid = (l + r) // 2
        node = TreeNode(nums[mid])
        node.left = self.build(nums, l, mid - 1)
        node.right = self.build(nums, mid + 1, r)
        return node

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    ans = []

    def removeNode(self, root, value):
        self.inorder(root, value)
        return self.build(0, len(self.ans) - 1)

    def inorder(self, root, value):
        if root is None:
            return

        self.inorder(root.left, value)
        if root.val != value:
            self.ans.append(root.val)
        self.inorder(root.right, value)

    def build(self, l, r):
        if l == r:
            node = TreeNode(self.ans[l])
            return node
        if l > r:
            return None
        mid = (l + r) // 2
        node = TreeNode(self.ans[mid])
        node.left = self.build(l, mid - 1)
        node.right = self.build(mid + 1, r)
        return node


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        if not root:
            return root

        if value < root.val:
            root.left = self.removeNode(root.left, value)
        elif value > root.val:
            root.right = self.removeNode(root.right, value)
        else:
            if root.left and root.right:
                max = self.findMaxLessThan(root)
                root.val = max.val
                root.left = self.removeNode(root.left, max.val)
            elif root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                root = None
        return root

    def findMaxLessThan(self, root):
        node = root.left
        while node.right:
            node = node.right
        return node

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """

    def removeNode(self, root, value):
        if not root:
            return root

        if value > root.val:
            root.right = self.removeNode(root.right, value)
            return root
        elif value < root.val:
            root.left = self.removeNode(root.left, value)
            return root
        else:
            next_node = self.find_next(root)
            if next_node == None:
                return None
            if next_node != root.left:
                next_node.left = root.left
            if next_node != root.right:
                next_node.right = root.right
            root.left = None
            root.right = None
            return next_node


    def find_next(self, root):
        if root.right:
            node = root.right
            prev = node
            while node.left:
                prev = node
                node = node.left

            prev.left = node.right
            return node
        elif root.left:
            node = root.left
            prev = node
            while node.right:
                prev = node
                node = node.right
            prev.right = node.left
            return node
        else:
            return None