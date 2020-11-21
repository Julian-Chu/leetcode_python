class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > A[mid + 1]:
                end = mid
            else:
                start = mid

        if A[start] > A[end]:
            return start

        return end


class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        start, end = 1, len(A) - 2

        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
            else:
                return mid

        if A[start] > A[end]:
            return start

        return end