from typing import List

from helper import TreeNode


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        arr = [root]

        while len(arr) > 0:
            size = len(arr)
            temp = []
            for i in range(size):
                node = arr[i]
                if node.left is not None:
                    arr.append(node.left)
                    temp.append(node.left.val)

                if node.right is not None:
                    arr.append(node.right)
                    temp.append(node.right.val)

            arr = arr[size:]
            if len(temp) > 0:
                res.append(temp)

        return res[::-1]


from collections import deque


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])

        while len(queue) > 0:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)

        return res[::-1]