"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
        if not root:
            return 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        root_height = max(left_height, right_height) + 1

        return root_height


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
        if not root:
            return 0

        queue = collections.deque([root])
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth


