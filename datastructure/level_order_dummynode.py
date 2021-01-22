import collections


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def levelOrder(self, root):
    if not root:
        return []

    queue = collections.deque([root, None])
    results, level = [], []
    while queue:
        node = queue.popleft()
        if node is None:
            results.append(level)
            level = []
            if queue:
                queue.append(None)
            continue
        level.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return  results