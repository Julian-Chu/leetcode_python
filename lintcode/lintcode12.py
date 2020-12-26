class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        self.stack.append(number)
        if not self.min_stack or self.min_stack[-1] >= number:
            self.min_stack.append(number)

    """
    @return: An integer
    """

    def pop(self):
        num = self.stack.pop()
        if self.min_stack[-1] == num:
            self.min_stack.pop()
        return num

    """
    @return: An integer
    """

    def min(self):
        return self.min_stack[-1]
