import heapq


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        return self.merge_range_lists(lists, 0, len(lists) - 1)

    def merge_range_lists(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = (start + end) // 2
        left = self.merge_range_lists(lists, start, mid)
        right = self.merge_range_lists(lists, mid + 1, end)

        return self.merge_two_lists(left, right)

    def merge_two_lists(self, a, b):
        dummyNode = cur = ListNode(-1)
        while a and b:
            if a.val < b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next

        while a:
            cur.next = a
            cur = cur.next
            a = a.next

        while b:
            cur.next = b
            cur = cur.next
            b = b.next
        return dummyNode.next

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

