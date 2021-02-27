class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node = head
        dic = {}
        while node:
            copy = Node(node.val, node.next, node.random)
            dic[node] = copy
            node = node.next

        node = head
        while node:
            if node.next is not None:
                dic[node].next = dic[node.next]
            if node.random is not None:
                dic[node].random = dic[node.random]
            node = node.next
        return dic[head]
