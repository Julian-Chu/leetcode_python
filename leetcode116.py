from unittest import TestCase


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]

        while len(queue) > 0:
            qLen = len(queue)
            tmp = []
            for i in range(qLen):
                if queue[i].left:
                    tmp.append(queue[i].left)
                    tmp.append(queue[i].right)
                if i < qLen - 1:
                    queue[i].next = queue[i + 1]
            queue = tmp

        return root


class TestSolution(TestCase):
    def test_connect(self):
         node = Node(1)
         node.left = Node(2)
         node.right = Node(3)
         solution = Solution()
         solution.connect(node)
