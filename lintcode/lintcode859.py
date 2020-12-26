import heapq


class MaxStack:
    def __init__(self):
        self.heap = []
        self.stack = []
        self.poped_set = set()
        self.count = 0

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, x):
        item = (-x, -self.count)
        self.stack.append(item)
        heapq.heappush(self.heap, item)
        self.count += 1

    """
    @return: An integer
    """

    def pop(self):
        self.__clean_poped_stack(self.stack, self.poped_set)
        item = self.stack.pop()
        self.poped_set.add(item)
        return -item[0]

    """
    @return: An integer
    """

    def top(self):
        self.__clean_poped_stack(self.stack, self.poped_set)
        item = self.stack[-1]
        return -item[0]

    """
    @return: An integer
    """

    def peekMax(self):
        self.__clean_poped_heap(self.heap, self.poped_set)
        item = self.heap[0]
        return -item[0]

    """
    @return: An integer
    """

    def popMax(self):
        self.__clean_poped_heap(self.heap, self.poped_set)
        item = heapq.heappop(self.heap)
        self.poped_set.add(item)
        return -item[0]

    def __clean_poped_stack(self, stack, poped_set):
        while stack[-1] in poped_set:
            poped_set.remove(stack[-1])
            stack.pop()

    def __clean_poped_heap(self, heap, poped_set):
        while heap[-1] in poped_set:
            poped_set.remove(heap[-1])
            heapq.heappop()
