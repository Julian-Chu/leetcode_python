class MyQueue(object):
    def __init__(self):
        self.SIZE = 1000000
        self.queue = [0] * self.SIZE
        self.head, self.tail = 0, 0

    def enqueue(self, item):
        queue = self.queue

        if(self.tail+1) % self.SIZE == self.head:
            return

        queue[self.tail] = item
        self.tail = (self.tail+1) % self.SIZE

    def dequeue(self):
        if self.head == self.tail:
            return -1

        item = self.queue[self.head]
        self.head = (self.head+1)%self.SIZE
        return item


