"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """

    def rehashing(self, hashTable):
        capacity = len(hashTable)
        new_capacity = 2 * capacity
        new_hashTable = [None] * new_capacity
        for i in range(capacity):
            node = hashTable[i]
            while node:
                key = self.hashcode(node.val, new_capacity)
                cur = node
                node = node.next
                cur.next = None
                if not new_hashTable[key]:
                    new_hashTable[key] = cur
                    continue

                tail = new_hashTable[key]
                while tail.next:
                    tail = tail.next
                tail.next = cur

            hashTable[i] = None
        return new_hashTable

    def hashcode(self, key, capacity):
        return key % capacity


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """

    def rehashing(self, hashTable):
        HASH_SIZE = 2 * len(hashTable)
        anshashTable = [None for _ in range(HASH_SIZE)]
        for item in hashTable:
            p = item
            while p != None:
                self.addnode(anshashTable, p.val)
                p = p.next
        return anshashTable

    def addnode(self, anshashTable, number):
        p = number % len(anshashTable)
        if anshashTable[p] == None:
            anshashTable[p] = ListNode(number)
        else:
            self.addlistnode(anshashTable[p], number)

    def addlistnode(self, node, number):
        if node.next != None:
            self.addlistnode(node.next, number)
        else:
            node.next = ListNode(number)