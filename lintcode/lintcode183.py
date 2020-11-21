class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, L, k):
        if not L:
            return 0
        upperLen = sum(L) // k
        if upperLen == 0:
            return 0

        start, end = 1, upperLen

        while start + 1 < end:
            mid = (start + end) // 2
            if self.CutIntoPiecesByLen(L, mid) > k:
                start = mid
            elif self.CutIntoPiecesByLen(L, mid) < k:
                end = mid
            else:
                start = mid

        if self.CutIntoPiecesByLen(L, end) == k:
            return end

        return start

    def CutIntoPiecesByLen(self, nums, length):

        count = 0
        for num in nums:
            count += num // length

        return count


class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, L, k):
        if not L:
            return 0

        start, end = 1, max(L)

        while start + 1 < end:
            mid = (start + end) // 2
            if self.CutIntoPiecesByLen(L, mid) > k:
                start = mid
            elif self.CutIntoPiecesByLen(L, mid) < k:
                end = mid
            else:
                start = mid

        if self.CutIntoPiecesByLen(L, end) >= k:
            return end

        if self.CutIntoPiecesByLen(L, start) >= k:
            return start

        return 0

    def CutIntoPiecesByLen(self, nums, length):
        count = 0
        for num in nums:
            count += num // length
        return count