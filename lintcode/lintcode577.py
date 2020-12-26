"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq


class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """

    def mergeKSortedIntervalLists(self, intervals):
        if not intervals:
            return []

        heap = []
        results = []

        for i, arr in enumerate(intervals):
            if len(arr) == 0:
                continue
            heapq.heappush(heap, (arr[0].start, arr[0].end, i, 0))

        while heap:
            start, end, x, y = heapq.heappop(heap)
            self.push_back(results, Interval(start, end))
            if y + 1 < len(intervals[x]):
                heapq.heappush(heap, (intervals[x][y + 1].start, intervals[x][y + 1].end, x, y + 1))

        return results

    def push_back(self, intervals, interval):
        if not intervals:
            intervals.append(interval)
            return

        last_interval = intervals[-1]

        if last_interval.end < interval.start:
            intervals.append(interval)
            return

        last_interval.end = max(last_interval.end, interval.end)






