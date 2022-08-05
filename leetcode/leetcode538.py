# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        prev_sum = 0

        def traverse(node: TreeNode):
            nonlocal prev_sum
            if not node:
                return None

            traverse(node.right)
            node.val += prev_sum
            prev_sum = node.val
            traverse(node.left)

        traverse(root)
        return root


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = [root]
        pre_sum = 0
        while stack:
            node = stack.pop()

            if node:
                if node.left:
                    stack.append(node.left)

                stack.append(node)
                stack.append(None)

                if node.right:
                    stack.append(node.right)

            else:
                node = stack.pop()
                node.val += pre_sum
                pre_sum = node.val

        return root