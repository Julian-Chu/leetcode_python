import heapq


class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """

    def topk(self, nums, k):
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num <= heap[0]:
                    continue
                heapq.heappushpop(heap, num)

        heap.sort(reverse=True)
        return heap
