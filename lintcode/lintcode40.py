class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        self.stack1.append(element)

    """
    @return: An integer
    """

    def pop(self):
        self.__move_stack1_to_stack2()
        return self.stack2.pop()

    """
    @return: An integer
    """

    def top(self):
        self.__move_stack1_to_stack2()
        return self.stack2[-1]

    def __move_stack1_to_stack2(self):
        if self.stack2:
            return
        while self.stack1:
            self.stack2.append(self.stack1.pop())