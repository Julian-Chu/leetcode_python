import heapq


class Solution:
    """
    @param quality: an array
    @param wage: an array
    @param K: an integer
    @return: the least amount of money needed to form a paid group
    """

    def mincostToHireWorkers(self, quality, wage, K):
        # Write your code here
        workers = [(float(w) / q, q) for (w, q) in zip(wage, quality)]
        workers.sort()

        heap = []
        res = float('inf')
        q_sum = 0
        for cost_per_q, q in workers:
            heapq.heappush(heap, -q)
            q_sum += q

            if len(heap) > K:
                q_sum += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, q_sum * cost_per_q)

        return res