class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """

    def rerange(self, A):
        # write your code here

        pos, neg = 0, 0
        for num in A:
            if num > 0:
                pos += 1
            else:
                neg += 1

        self.partition(A, pos > neg)
        self.interleave(A, pos == neg)

    def partition(self, A, start_from_pos):
        flag = 1 if start_from_pos else -1
        left, right = 0, len(A) - 1
        while left <= right:
            while left <= right and A[left] * flag > 0:
                left += 1
            while left <= right and A[right] * flag < 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

    def interleave(self, A, is_same_length):
        l, r = 1, len(A) - 1
        if is_same_length:
            r = len(A) - 2

        while l < r:
            A[l], A[r] = A[r], A[l]
            l += 2
            r -= 2