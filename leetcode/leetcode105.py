# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        rootVal = preorder[0]
        rootIdx = inorder.index(rootVal)

        node = TreeNode(rootVal)
        node.left = self.buildTree(preorder[1:1 + rootIdx], inorder[:rootIdx])
        node.right = self.buildTree(preorder[1 + rootIdx:], inorder[rootIdx + 1:])

        return node