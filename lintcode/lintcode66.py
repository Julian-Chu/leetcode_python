"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        if not root:
            return []

        stack = [root]
        results = []
        prev = None

        while stack:
            curr = stack[-1]
            if not prev or prev.left == curr or prev.right == curr:
                results.append(curr.val)
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
            elif curr.left == prev:
                if curr.right:
                    stack.append(curr.right)
            else:
                stack.pop()
            prev = curr

        return results


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        if not root:
            return []

        nums = []
        cur = None

        while root:
            if root.left:
                cur = root.left
                # 將最右邊指向root
                while cur.right and cur.right != root:
                    cur = cur.right
                if cur.right == root:
                    cur.right = None
                    root = root.right
                else:
                    nums.append(root.val)
                    cur.right = root
                    root = root.left
            else:
                nums.append(root.val)
                root = root.right

        return nums