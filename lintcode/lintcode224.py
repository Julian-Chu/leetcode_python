class ThreeStacks:
    """
    @param: size: An integer
    """

    def __init__(self, size):
        self.stacks = [None] * 3 * (size + 1)
        self.stackTop = [0, size, size * 2]
        self.stackBottom = [0, size, size * 2]  # dummy

    """
    @param: stackNum: An integer
    @param: value: An integer
    @return: nothing
    """

    def push(self, stackNum, value):
        top = self.stackTop[stackNum]
        self.stacks[top + 1] = value
        self.stackTop[stackNum] += 1

    """
    @param: stackNum: An integer
    @return: the top element
    """

    def pop(self, stackNum):
        top = self.stackTop[stackNum]
        element = self.stacks[top]
        self.stackTop[stackNum] -= 1
        return element

    """
    @param: stackNum: An integer
    @return: the top element
    """

    def peek(self, stackNum):
        top = self.stackTop[stackNum]
        element = self.stacks[top]
        return element

    """
    @param: stackNum: An integer
    @return: true if the stack is empty else false
    """

    def isEmpty(self, stackNum):
        return self.stackTop[stackNum] == self.stackBottom[stackNum]

"""
not single array
"""
class ThreeStacks:
    """
    @param: size: An integer
    """

    def __init__(self, size):
        self.cap = size
        self.stacks = [[] for _ in range(3)]

    """
    @param: stackNum: An integer
    @param: value: An integer
    @return: nothing
    """

    def push(self, stackNum, value):
        if len(self.stacks[stackNum]) == self.cap:
            self.stacks[stackNum].pop()
        self.stacks[stackNum].append(value)

    """
    @param: stackNum: An integer
    @return: the top element
    """

    def pop(self, stackNum):
        if len(self.stacks[stackNum]) == 0:
            return -1
        return self.stacks[stackNum].pop()

    """
    @param: stackNum: An integer
    @return: the top element
    """

    def peek(self, stackNum):
        return self.stacks[stackNum][-1]

    """
    @param: stackNum: An integer
    @return: true if the stack is empty else false
    """

    def isEmpty(self, stackNum):
        return len(self.stacks[stackNum]) == 0
