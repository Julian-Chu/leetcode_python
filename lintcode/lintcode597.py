"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    avg, node = 0, None

    def findSubtree2(self, root):
        self.helper(root)
        return self.node

    def helper(self, root):
        if root is None:
            return 0, 0

        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)

        sum, size = left_sum + right_sum + root.val, left_size + right_size + 1

        if self.node is None or sum * 1.0 / size > self.avg:
            self.node = root
            self.avg = sum * 1.0 / size

        return sum, size

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """

    def findSubtree2(self, root):
        _, _, ans, _ = self.findSumAndNodeCountOfSubstree(root)
        return ans

    def findSumAndNodeCountOfSubstree(self, node):
        if not node:
            return 0, 0, None, -float('inf')

        if not node.left and not node.right:
            return node.val, 1, node, node.val

        leftSum, leftCount, leftNode, leftMaxAvg = self.findSumAndNodeCountOfSubstree(node.left)
        rightSum, rightCount, rightNode, rightMaxAvg = self.findSumAndNodeCountOfSubstree(node.right)

        treeSum = leftSum + rightSum + node.val
        treeNodecount = leftCount + rightCount + 1
        curAvg = treeSum / treeNodecount

        maxAvgNode = node
        maxAvg = curAvg
        if leftNode and leftMaxAvg > maxAvg:
            maxAvgNode = leftNode
            maxAvg = leftMaxAvg
        if rightNode and rightMaxAvg > maxAvg:
            maxAvgNode = rightNode
            maxAvg = rightMaxAvg

        return treeSum, treeNodecount, maxAvgNode, maxAvg
