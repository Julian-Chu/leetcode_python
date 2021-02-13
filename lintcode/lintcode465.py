class Solution_heap:

    def kthSmallestSum(self, A, B, kth):

        m, n = len(A), len(B)
        if m < n:
            m, n, A, B = n, m, B, A

        h = [(A[0] + B[j], 0, j) for j in range(min(n, kth))]

        for _ in range(kth):
            num, i, j = heappop(h)

            if i + 1 < m:
                heappush(h, (A[i + 1] + B[j], i + 1, j))

        return num

class Solution_binary_search:

    def kthSmallestSum(self, A, B, kth):

        m, n = len(A), len(B)
        lo, hi = A[0] + B[0], A[-1] + B[-1] + 1

        while lo < hi:
            mid = (lo + hi) // 2
            i, j, count = 0, n - 1, 0
            while i < m and j >= 0:
                if A[i] + B[j] > mid:
                    j -= 1
                else:
                    count += j + 1
                    i += 1
            if count < kth:
                lo = mid + 1
            else:
                hi = mid

        return lo


class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """

    def kthSmallestSum(self, A, B, k):
        start, end = A[0] + B[0], A[-1] + B[-1]

        while start + 1 < end:
            mid = (start + end) // 2
            # 利用find first找到最小符合條件的數
            if self.get_sums_smaller_or_equal(A, B, mid) >= k:
                end = mid
            else:
                start = mid

        if self.get_sums_smaller_or_equal(A, B, start) >= k:
            return start
        # if self.get_sums_smaller_or_equal(A,B, end) >=k:
        return end

    def get_sums_smaller_or_equal(self, A, B, val):
        count = 0
        for a in A:
            for b in B:
                if a + b > val:
                    break
                count += 1
        return count

    def get_sums_smaller_or_equal_2(self, A, B, val):
        m, n = len(A), len(B)
        i, j ,count = 0, n-1, 0
        while i < m and j >=0:
            if A[i] + B[j] >val:
                j-=1
            else:
                # when i is fixed, all j makes sum smaller than mid => count sorting
                count += j + 1
                i += 1
        return count
