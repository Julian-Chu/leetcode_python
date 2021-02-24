import heapq
class MaxStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        self.count = 0
        self.poped_set = set()

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
        self.__clean_poped_in_stack(self.stack, self.poped_set)
        item = self.stack.pop()
        self.poped_set.add(item)
        return -item[0]

    """
    @return: An integer
    """

    def top(self):
        self.__clean_poped_in_stack(self.stack, self.poped_set)
        item = self.stack[-1]
        return -item[0]

    """
    @return: An integer
    """

    def peekMax(self):
        self.__clean_poped_in_heap(self.heap, self.poped_set)
        item = self.heap[0]
        return -item[0]

    """
    @return: An integer
    """

    def popMax(self):
        self.__clean_poped_in_heap(self.heap, self.poped_set)
        item = heapq.heappop(self.heap)
        self.poped_set.add(item)
        return -item[0]

    def __clean_poped_in_stack(self, stack, poped_set):
        while stack and stack[-1] in poped_set:
            poped_set.remove(stack[-1])
            self.stack.pop()

    def __clean_poped_in_heap(self, heap, poped_set):
        while heap and heap[0] in poped_set:
            poped_set.remove(heap[0])
            heapq.heappop(self.heap)


class MaxStack:

    def __init__(self):
        self.max_stack = []
        self.stack = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, x):
        if self.max_stack:
            number = max(self.max_stack[-1], x)
            self.max_stack.append(number)
        else:
            self.max_stack.append(x)
        self.stack.append(x)

    """
    @return: An integer
    """

    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()

    """
    @return: An integer
    """

    def top(self):
        return self.stack[-1]

    """
    @return: An integer
    """

    def peekMax(self):
        return self.max_stack[-1]

    """
    @return: An integer
    """

    def popMax(self):
        buffer_stack = []
        while self.stack[-1] != self.max_stack[-1]:
            buffer_stack.append(self.stack.pop())
            self.max_stack.pop()

        num = self.stack.pop()
        self.max_stack.pop()
        while buffer_stack:
            number = (buffer_stack[-1], self.max_stack[-1])
            self.stack.append(buffer_stack.pop())
            self.max_stack.append(number)

        return num