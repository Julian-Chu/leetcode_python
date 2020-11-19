# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    pre = -1 << 31
    res = 1 << 31 - 1

    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.res

    def minDiffinBST(self, root):
        stack = []
        curr = root
        preValue = -1 << 31
        res = 1 << 31 - 1
        while curr or stack:
            if not curr:
                curr = stack.pop()
                res = min(res, curr.val - preValue)
                preValue = curr.val
                curr = curr.right
            else:
                stack.append(curr)
                curr = curr.left
        return res

    def minDiffInOrderList(self, root):
        nodes = []

        def inOrder(node: TreeNode, nodeList):
            if node.left:
                inOrder(node.left, nodeList)
            nodeList.append(node.val)
            if node.right:
                inOrder(node.right, nodeList)

        inOrder(root, nodes)
        res = float('inf')
        for i in range(1, len(nodes)):
            res = min(res, nodes[i] - nodes[i - 1])
        return res
