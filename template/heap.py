import heapq
"""
minheap:  nlogn + klogn(worse)
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        heap = []
        # heapify  O(n)
        # heapq.heapify(heap)
        # pushpop
        # heapq.pushpop(....)

        # nlogn
        for point in points:
            dist = self.get_dist(point, origin)
            # push
            # we can push tuple , and first value of tuple will be used for sorting
            # this is minheap, if max heap =>  multiplied by -1
            heapq.heappush(heap, (dist, point.x, point.y))

        result = []
        # klogn
        for _ in range(k):
            # pop
            _, x, y = heapq.heappop(heap)
            result.append([x, y])
        return result

    def get_dist(self, point, origin):
        dist_x = point.x - origin.x
        dist_y = point.y - origin.y

        return dist_x ** 2 + dist_y ** 2