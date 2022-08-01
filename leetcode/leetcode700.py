# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root and root.val == val:
            return root

        if root.val > val:
            return self.searchBST(root.left, val)

        return self.searchBST(root.right, val)


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        node = root

        while node:
            if node.val == val:
                return node
            elif node.val > val:
                node = node.left
            else:
                node = node.right
        return None