from typing import List

from helper import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = self.BuildLevelOrder(root, [], 0)
        return res

    def BuildLevelOrder(self, root, res: List[List[int]], level) -> List[List[int]]:
        if not root:
            return res

        if len(res) == level:
            res.append([])

        res[level].append(root.val)
        res = self.BuildLevelOrder(root.left, res, level+1)
        res = self.BuildLevelOrder(root.right, res, level+1)
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]

        while len(stack) > 0:
            n = stack.pop()
            if n:
                if n.right:
                    stack.append(n.right)
                if n.left:
                    stack.append(n.left)

                stack.append(n)
                stack.append(None)
            else:
                n = stack.pop()
                res.append(n.val)
        return res