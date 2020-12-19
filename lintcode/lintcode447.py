class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """

    def searchBigSortedArray(self, reader, target):
        kth = 1
        while reader.get(kth - 1) < target:
            kth = kth * 2

        start, end = 0, kth - 1
        while start + 1 < end:
            mid = (start + end) // 2
            mid_val = reader.get(mid)
            if mid_val == target:
                end = mid
            elif mid_val < target:
                start = mid
            else:
                end = mid
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end

        return -1