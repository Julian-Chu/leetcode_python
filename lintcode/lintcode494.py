import collections


class Stack:
    def __init__(self):
        self.queue1 = collections.deque([])
        self.queue2 = collections.deque([])

    """
    @param: x: An integer
    @return: nothing
    """

    def push(self, x):
        self.queue1.append(x)

    """
    @return: nothing
    """

    def pop(self):
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        val = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return val

    """
    @return: An integer
    """

    def top(self):
        val = self.pop()
        self.push(val)
        return val

    """
    @return: True if the stack is empty
    """

    def isEmpty(self):
        return not self.queue1