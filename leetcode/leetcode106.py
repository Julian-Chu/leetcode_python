# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        rootVal = postorder[-1]
        rootIdx = inorder.index(rootVal)

        node = TreeNode(rootVal)
        node.left = self.buildTree(inorder[:rootIdx], postorder[:rootIdx])
        node.right = self.buildTree(inorder[rootIdx + 1:], postorder[rootIdx:len(postorder) - 1])

        return node