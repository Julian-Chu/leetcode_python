class Siftup:
    def siftup(self, A, k):
        while k > 0:
            father = (k-1)//2
            if A[k] > A[father]:
                break

            A[k], A[father] = A[father], A[k]
            k = father

    def heapify(self, A):
        for i in range(len(A)):
            self.siftup(A, i)

class Siftdown:
    def siftdown(self, A, k):
        while k*2+1 < len(A):
            son = k * 2 + 1
            if k*2+2 < len(A) and A[son] > A[k*2+2]:
                son = k*2 + 2
            if A[k] <= A[son]:
                break
            A[k], A[son] = A[son], A[k]
            k = son

    def heapify(self, A):
        for i in range(len(A)-1, -1, -1):
            self.siftdown(A, i)

"""
O(n*log(n))
O(1)
"""
class HeapSorting:
    def siftdown(self, A, left, right):
        k = left
        while k*2+1 <= right:
            son = k*2+1
            if son+1 <=right and A[son] < A[son+1]:
                son = k*2+2
            if A[son] <= A[k]:
                break
            A[son], A[k] = A[k], A[son]
            k = son

    def heapify(self, A):
        for i in range((len(A)-1)//2, -1, -1):
            self.siftdown(A, i, len(A)-1)

    def sortIntegers(self, A):
        self.heapify(A)
        for i in range(len(A)-1, -1, -1):
            A[0], A[i] = A[i], A[0]
            self.siftdown(A, 0, i-1)