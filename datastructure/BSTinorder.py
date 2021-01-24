def BSTinorder(self, root):
    stack = []
    while root:
        stack.append(root)
        root = root.left

    while stack:
        node = stack[-1]
        if node.right is not None:
            n = node.right
            while n:
                stack.append(n)
                n = n.left
        else:
            n = stack.pop()
            while stack and stack[-1].right == n:
                n = stack.pop()


def BSTinorder_reverse(self, root):
    stack = []
    while root:
        stack.append(root)
        root = root.right

    while stack:
        node = stack[-1]
        if node.left is not None:
            n = node.left
            while n:
                stack.append(n)
                n = n.right
        else:
            n = stack.pop()
            while stack and stack[-1].left == n:
                n = stack.pop()