"""
sift down

O(n) 是因为从第 N/2 个位置开始往下 siftdown，那么就有大约 N/4 个数在 siftdown 中最多交换 1 次，N/8 个数最多交换 2 次，N/16 个数最多交换 3 次。 所以
O(N/4∗1+N/8∗2+N/16∗3+...+1∗LogN)=O(N)
"""
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

"""
sift up
O(nlogn)
"""

class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """

    def heapify(self, A):
        for i in range(len(A)):
            self.siftup(A, i)

    def siftup(self, A, i):
        if i == 0:
            return
        parentIdx = (i - 1) // 2
        while i > 0 and A[i] < A[parentIdx]:
            A[i], A[parentIdx] = A[parentIdx], A[i]
            i = parentIdx
            parentIdx = (i - 1) // 2