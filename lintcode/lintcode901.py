"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """

    def closestKValues(self, root, target, k):
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left

        inoder = []

        while len(self.stack) > 0:
            node = self.stack.pop()
            next = node.right
            while next:
                self.stack.append(next)
                next = next.left

            inoder.append(node.val)

        minIndex = 0
        for i in range(len(inoder)):
            if abs(inoder[i] - target) < abs(inoder[minIndex] - target):
                minIndex = i

        left, right = minIndex, minIndex
        print('min:', minIndex)

        for _ in range(k - 1):
            if left <= 0 and right + 1 >= len(inoder):
                break
            if right + 1 >= len(inoder):
                left -= 1
                continue
            if left <= 0:
                right += 1
                continue

            if abs(inoder[left - 1] - target) > abs(inoder[right + 1] - target):
                right += 1
            elif abs(inoder[left - 1] - target) < abs(inoder[right + 1] - target):
                left -= 1
            else:
                left -= 1

            print(left, right)

        return inoder[left:right + 1]