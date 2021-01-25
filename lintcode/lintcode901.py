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


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """

    def closestKValues(self, root, target, k):
        lower_stack = []

        while root:
            lower_stack.append(root)
            if root.val > target:
                root = root.left
            else:
                root = root.right

        upper_stack = lower_stack[:]

        if target < lower_stack[-1].val:
            self.move_lower(lower_stack)
        else:
            self.move_upper(upper_stack)

        result = []
        for _ in range(k):
            if lower_stack and upper_stack:
                if abs(lower_stack[-1].val - target) < abs(upper_stack[-1].val - target):
                    result.append(lower_stack[-1].val)
                    self.move_lower(lower_stack)
                else:
                    result.append(upper_stack[-1].val)
                    self.move_upper(upper_stack)
            elif lower_stack:
                result.append(lower_stack[-1].val)
                self.move_lower(lower_stack)
            elif upper_stack:
                result.append(upper_stack[-1].val)
                self.move_upper(upper_stack)
            else:
                break

        return result

    def move_lower(self, stack):
        if not stack:
            return

        node = stack[-1]
        if not node.left:
            node = stack.pop()
            while stack and stack[-1].left == node:
                node = stack.pop()
            return

        node = node.left
        while node:
            stack.append(node)
            node = node.right

    def move_upper(self, stack):
        if not stack:
            return
        node = stack[-1]
        if not node.right:
            node = stack.pop()
            while stack and stack[-1].right == node:
                node = stack.pop()
            return

        # push left node of curr node
        node = node.right
        while node:
            stack.append(node)
            node = node.left