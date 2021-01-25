class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        result = []
        self.traverse(root, k1, k2, result)
        return result

    def traverse(self, root, k1, k2, result):
        if not root:
            return

        if root.val > k1:
            self.traverse(root.left, k1, k2, result)
        if k1 <= root.val <= k2:
            result.append(root.val)
        if root.val < k2:
            self.traverse(root.right, k1, k2, result)


class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        stack = []

        while root:
            stack.append(root)
            root = root.left

        result = []
        while stack:
            node = stack.pop()
            if node.right:
                n = node.right
                while n:
                    stack.append(n)
                    n = n.left
            if node.val > k2:
                break
            if k1 <= node.val <= k2:
                result.append(node.val)

        return result


class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        if not root:
            return []
        if k1 > root.val:
            res = self.searchRange(root.right, k1, k2)

        elif k2 < root.val:
            res = self.searchRange(root.left, k1, k2)
        else:
            res = self.searchRange(root.left, k1, root.val) + [root.val] + self.searchRange(root.right, root.val, k2)

        return res