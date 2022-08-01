class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def helper(a: TreeNode, b: TreeNode) -> bool:
            if a is None and b is None:
                return True

            if a is None or b is None:
                return False

            if a.val != b.val:
                return False

            return helper(a.left, b.right) and helper(a.right, b.left)

        return helper(root.left, root.right)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [root.left, root.right]

        while len(stack) > 0:
            a = stack.pop()
            b = stack.pop()
            if a is None and b is None:
                continue

            if not a or not b or a.val != b.val:
                return False

            stack.append(a.left)
            stack.append(b.right)

            stack.append(a.right)
            stack.append(b.left)

        return True