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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []

        def dfs(node: TreeNode, path: List[int], restSum: int):
            if not node:
                return

            path.append(node.val)
            restSum -= node.val

            if not node.left and not node.right:
                if restSum == 0:
                    res.append(path[:])
                path.pop()
                return
            dfs(node.left, path, restSum)
            dfs(node.right, path, restSum)
            path.pop()

        dfs(root, [], targetSum)
        return res


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []

        def dfs(node: TreeNode, path: List[int], remain: int):
            if not node.left and not node.right:
                if remain == 0:
                    res.append(path[:])
                return

            if node.left:
                path.append(node.left.val)
                dfs(node.left, path, remain - node.left.val)
                path.pop()

            if node.right:
                path.append(node.right.val)
                dfs(node.right, path, remain - node.right.val)
                path.pop()

        dfs(root, [root.val], targetSum - root.val)

        return res