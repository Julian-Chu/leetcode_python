import collections


class Solution:
    """
    @param root: the root node
    @param k: an integer
    @return: the number of nodes in the k-th layer of the binary tree
    """

    def kthfloorNode(self, root, k):
        # Write your code here
        if not root:
            return 0
        if k <= 1:
            return k

        queue = collections.deque([root])
        layer = 1
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            layer += 1
            if layer == k:
                break

        return len(queue)


