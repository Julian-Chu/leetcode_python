class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        left = 0
        if root.left:
            if not root.left.left and not root.left.right:
                left = root.left.val
            else:
                left = self.sumOfLeftLeaves(root.left)
        right = 0
        if root.right:
            right = self.sumOfLeftLeaves(root.right)

        return left + right


import collections


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = collections.deque([root])
        res = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left and not node.left.left and not node.left.right:
                    res += node.left.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res