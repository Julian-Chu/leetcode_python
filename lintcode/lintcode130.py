class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """

    def heapify(self, A):
        for i in range(len(A) // 2, -1, -1):
            self.siftdown(A, i)

    def siftdown(self, A, i):
        while i < len(A):
            left = i * 2 + 1
            right = i * 2 + 2
            minIndex = i
            if right < len(A) and A[right] < A[minIndex]:
                minIndex = right
            if left < len(A) and A[left] < A[minIndex]:
                minIndex = left

            if minIndex == i:
                break

            A[minIndex], A[i] = A[i], A[minIndex]
            i = minIndex


class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """

    def heapify(self, A):
        for i in range(len(A) // 2, -1, -1):
            self.siftdown(A, i)

    def siftdown(self, A, i):
        while i * 2 + 1 < len(A):
            son = i * 2 + 1
            right = i * 2 + 2
            if right < len(A) and A[right] < A[son]:
                son = right
            if A[son] >= A[i]:
                break
            A[son], A[i] = A[i], A[son]
            i = son