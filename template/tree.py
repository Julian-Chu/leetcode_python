def Inorder(self, root: Optional[TreeNode]) -> bool:
    stack = [root]
    prev = None

    while stack:
        node = stack.pop()

        if node:
            # right
            if node.right:
                stack.append(node.right)
            # root
            stack.append(node)
            stack.append(None)

            # left
            if node.left:
                stack.append(node.left)
        else:
            node = stack.pop()
            # do something
    return True