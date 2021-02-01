"""
一个变种是top k，但返回数组本身无需排序，那么这个基于快选的实现就是O(n)的最优解，把那行调用快排的代码删了就好。
即使加了快排，这个实现的时间复杂度是 O(max(n, klogk))。在k比n小很多时，比O(nlogk)的堆解要优，在k和n接近时，复杂度一样。

基于 PriorityQueue 的方法 PriorityQueue 里从远到近排序。当 PQ 里超过 k 个的时候，就 pop 掉一个。 时间复杂度 O(nlogk)
如果使用 Quick Select 离线算法： 0. 计算所有的点到原点的 distance -- O(n) 1. Quick Select 去找到 kth smallest distance -- O(n) 3. 遍历所有 distance 找到 top k smallest distance -- O(n) 4. 找到的 top k smallest points 按 distance 排序并返回 -- O(klogk)
总共 Quick Select 离线算法耗费时间 O ( n + k l o g k )
"""
"""
quickselect(klogk) + quicksort(n)
O(klogk + n)
"""
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        dist = [(self.get_distance(point, origin), point.x, point.y) for point in points]

        self.quickselect(dist, 0, len(dist) - 1, k - 1)
        dist_topk = dist[:k]

        self.quicksort(dist_topk, 0, len(dist_topk) - 1)
        results = [[x[1], x[2]] for x in dist_topk]
        return results

    def get_distance(self, point, origin):
        return (point.x - origin.x) ** 2 + (point.y - origin.y) ** 2

    def quicksort(self, dist, start, end):
        if start >= end:
            return

        left, right = start, end
        pivot = dist[(left + right) // 2]
        while left <= right:
            while left <= right and dist[left] < pivot:
                left += 1
            while left <= right and dist[right] > pivot:
                right -= 1

            if left <= right:
                dist[left], dist[right] = dist[right], dist[left]
                left += 1
                right -= 1
        self.quicksort(dist, start, right)
        self.quicksort(dist, left, end)

    def quickselect(self, dist, start, end, k):
        if start >= end:
            return

        left, right = start, end
        pivot = dist[(left + right) // 2]
        while left <= right:
            while left <= right and dist[left] < pivot:
                left += 1
            while left <= right and dist[right] > pivot:
                right -= 1

            if left <= right:
                dist[left], dist[right] = dist[right], dist[left]
                left += 1
                right -= 1
        if k <= right:
            self.quickselect(dist, start, right, k)
            return
        if k >= left:
            self.quickselect(dist, left, end, k)
            return

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

        # nlogn
        for point in points:
            dist = self.get_dist(point, origin)
            heapq.heappush(heap, (dist, point.x, point.y))

        result = []
        # klogn
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            result.append([x, y])
        return result

    def get_dist(self, point, origin):
        dist_x = point.x - origin.x
        dist_y = point.y - origin.y

        return dist_x ** 2 + dist_y ** 2
"""
maxheap: nlogn vs nlogk
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

        for point in points:
            dist = self.get_dist(point, origin)
            heapq.heappush(heap, (-dist, -point.x, -point.y))

            # keep k element in heap => for-loop: O(nlogk)
            if len(heap) > k:
                heapq.heappop((heap))


        # pop 在for loop外=> for loop複雜度變成 O(nlogn)
        # while len(heap) > k:
        #     heapq.heappop(heap)

        results = []
        while heap:
            _, x, y = heapq.heappop(heap)
            results.append([-x, -y])
        return results[::-1]

    def get_dist(self, point, origin):
        dist_x = point.x - origin.x
        dist_y = point.y - origin.y

        return dist_x ** 2 + dist_y ** 2