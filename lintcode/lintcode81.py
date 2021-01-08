import heapq


class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """

    def medianII(self, nums):
        maxheap = []
        minheap = []
        result = []
        for num in nums:
            if maxheap and num > -maxheap[0]:
                heapq.heappush(minheap, num)
                if len(minheap) > len(maxheap):
                    heapq.heappush(maxheap, -heapq.heappop(minheap))

            else:
                heapq.heappush(maxheap, -num)
                if len(maxheap) - len(minheap) > 1:
                    heapq.heappush(minheap, -heapq.heappop(maxheap))
            result.append(-maxheap[0])
        return result

    def medianII(self, nums):
        max_heap, min_heap, output = [], [], []

        for num in nums:
            if len(max_heap) == len(min_heap):
                if max_heap and num > -max_heap[0]:
                    num = heapq.heappushpop(min_heap, num)
                heapq.heappush(max_heap, -num)
            else:
                if num < -max_heap[0]:
                    num = - heapq.heappushpop(max_heap, -num)
                heapq.heappush(min_heap, num)
            output.append(-max_heap[0])
        return output

