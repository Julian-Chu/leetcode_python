from typing import List

from helper import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        curPath = []
        res = self.recur(root, sum, res, curPath)
        return res

    def recur(self, node: TreeNode, sum: int, res: List[List[int]], curpath: List[int]) -> List[List[int]]:
        if not node:
            return res

        curpath = curpath.copy()
        curpath.append(node.val)
        if not node.left and not node.right:
            if node.val == sum:
                res.append(curpath)
            return res
        sum -= node.val
        if node.left is not None:
            res = self.recur(node.left, sum, res, curpath)
        if node.right is not None:
            res = self.recur(node.right, sum, res, curpath)

        return res
