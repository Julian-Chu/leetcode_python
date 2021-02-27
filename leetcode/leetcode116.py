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
            for i in range(qLen):
                node = queue.pop(0)
                if i == qLen-1:
                    node.next = None
                else:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)

        return root


class TestSolution(TestCase):
    def test_connect(self):
         node = Node(1)
         node.left = Node(2)
         node.right = Node(3)
         solution = Solution()
         solution.connect(node)
