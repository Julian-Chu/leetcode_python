class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        if not self.head:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    """
    @return: An integer
    """

    def dequeue(self):
        node = self.head
        self.head = self.head.next

        if not node:
            return -1
        return node.value


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """

    def __init__(self):
        self.SIZE = 100000
        self.queue = [0] * self.SIZE
        self.head, self.tail = 0, 0

    def enqueue(self, item):
        queue = self.queue
        if (self.tail + 1) % self.SIZE == self.head:
            return

        queue[self.tail] = item
        self.tail = (self.tail + 1) % self.SIZE

    """
    @return: An integer
    """

    def dequeue(self):
        queue = self.queue

        if self.head == self.tail:
            return -1

        item = queue[self.head]
        self.head = (self.head+1) % self.SIZE
        return item
