import heapq


class Solution:
    """
    @param: k: An integer
    """

    def __init__(self, k):
        self.cap = k
        self.heap = []

    """
    @param: num: Number to be added
    @return: nothing
    """

    def add(self, num):
        heap = self.heap
        cap = self.cap

        if len(heap) < cap:
            heapq.heappush(heap, num)
        else:
            heapq.heappushpop(heap, num)

    """
    @return: Top k element
    """

    def topk(self):
        topk = sorted(self.heap, reverse=True)
        return topk