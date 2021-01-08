from collections import deque


class MovingAverage:
    """
    @param: size: An integer
    """

    def __init__(self, size):
        self.cap = size
        self.queue = deque([])
        self.sum = float(0)

    """
    @param: val: An integer
    @return:  
    """

    def next(self, val):
        if len(self.queue) == self.cap:
            self.sum -= self.queue.popleft()
        self.sum += val
        self.queue.append(val)

        return self.sum / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)