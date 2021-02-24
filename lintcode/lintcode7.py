class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        if not root:
            return ['#']
        ans = []
        ans.append(str(root.val))
        ans += self.serialize(root.left)
        ans += self.serialize(root.right)
        return ans

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """

    def deserialize(self, data):
        ch = data.pop(0)
        if ch == '#':
            return None
        root = TreeNode(int(ch))
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
        return root


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from collections import deque


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        queue = collections.deque([root])
        bfs_order = []
        while queue:
            node = queue.popleft()
            if node is None:
                bfs_order.append('#')
                continue

            bfs_order.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        return ' '.join(bfs_order)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """

    def deserialize(self, data):
        if not data:
            return  None
        data = data.split()
        res = [TreeNode(int(string)) if string != '#' else None for string in data]
        root = res[0]
        slow, fast = 0, 1
        while slow < len(data):
            # while fast < len(data):
            node = res[slow]
            slow += 1
            if node:
                node.left = res[fast]
                node.right = res[fast + 1]
                fast += 2
        return root
