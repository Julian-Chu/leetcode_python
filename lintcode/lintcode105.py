"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None

        mapping = {}
        curr = head
        while curr:
            mapping[curr] = RandomListNode(curr.label)
            curr = curr.next

        for node in mapping:
            if node.next:
                mapping[node].next = mapping[node.next]
            if node.random:
                mapping[node].random = mapping[node.random]
        return mapping[head]


"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        hashmap = {}

        cur = head
        while cur:
            hashmap[cur.label] = RandomListNode(cur.label)
            cur = cur.next

        dummy = tail = RandomListNode(0)

        cur = head
        while cur:
            tail.next = hashmap[cur.label]
            tail = tail.next
            if cur.random:
                tail.random = hashmap[cur.random.label]
            cur = cur.next
        return dummy.next