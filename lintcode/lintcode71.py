"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque


class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """

    def zigzagLevelOrder(self, root):
        result = []
        if not root:
            return result
        reverse_flag = -1
        queue = deque([root])

        while queue:
            res = []
            reverse_flag *= -1
            for i in range(len(queue)):
                node = queue.popleft()
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res = res[::reverse_flag]
            result.append(res)

        return result