# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        inorder = []

        while stack:
            node = stack.pop()

            if node:
                if node.right:
                    stack.append(node.right)

                stack.append(node)
                stack.append(None)

                if node.left:
                    stack.append(node.left)
            else:
                node = stack.pop()
                inorder.append(node.val)

        diff = 10 ** 5
        for i in range(1, len(inorder)):
            if inorder[i] - inorder[i - 1] < diff:
                diff = inorder[i] - inorder[i - 1]

        return diff