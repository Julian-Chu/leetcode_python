class DataStream:
    def __init__(self):
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.num_to_prev = {}
        self.duplicates = set()

    """
    @param num: next number in stream
    @return: nothing
    """

    def add(self, num):
        if num in self.duplicates:
            return
        if num not in self.num_to_prev:
            self.push_back(num)
            return
        self.duplicates.add(num)
        self.remove(num)

    def push_back(self, num):
        self.tail.next = ListNode(num)
        self.num_to_prev[num] = self.tail
        self.tail = self.tail.next

    def remove(self, num):
        prev = self.num_to_prev.get(num)
        del self.num_to_prev[num]
        prev.next = prev.next.next
        if prev.next: # smart
            self.num_to_prev[prev.next.val] = prev
        else:
            self.tail = prev

    """
    @return: the first unique number in stream
    """

    def firstUnique(self):
        if not self.dummy.next:
            return None
        return self.dummy.next.val


class DataStream:
    def __init__(self):
        self.point_to_prev = {}
        self.dummy = self.tail = ListNode(-1)

    """
    @param num: next number in stream
    @return: nothing
    """

    def add(self, num):
        if num not in self.point_to_prev:
            self.point_to_prev[num] = self.tail
            self.tail.next = ListNode(num)
            self.tail = self.tail.next
        else:
            prev = self.point_to_prev[num]
            if prev is None:
                return
            if prev.next == self.tail:
                self.tail = prev
            prev.next = prev.next.next
            self.point_to_prev[num] = None
            if prev.next is not None:
                self.point_to_prev[prev.next.val] = prev

    """
    @return: the first unique number in stream
    """

    def firstUnique(self):
        return self.dummy.next.val

# class ListNode:
#     def __init__(self, val, next = None):
#         self.val = val
#         self.next = next