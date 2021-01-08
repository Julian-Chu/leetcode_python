class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """

    def permutationIndexII(self, A):
        n = len(A)
        res = 1
        factorial = 1
        repeat = 1
        nums = {}
        for i in range(n - 1, -1, -1):
            if A[i] in nums:
                nums[A[i]] += 1
            else:
                nums[A[i]] = 1
            if nums[A[i]] > 1:
                repeat *= nums[A[i]]
            smaller = 0
            for j in range(i + 1, n):
                if A[j] < A[i]:
                    smaller += 1
            res += smaller * factorial // repeat
            factorial *= (n - i)

        return res


class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """

    def permutationIndexII(self, A):
        permutation = 1
        result = 0
        duplicate_permutation = 1
        duplicate_nums = {A[-1]: 1}
        for i in range(len(A) - 2, -1, -1):
            smaller = 0
            duplicate_nums[A[i]] = duplicate_nums.get(A[i], 0) + 1
            duplicate_permutation *= duplicate_nums[A[i]]

            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    smaller += 1
            result += smaller * permutation // duplicate_permutation
            permutation *= len(A) - i
        return result + 1

"""
timeout
"""
class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """

    def permutationIndexII(self, A):
        nums = A[:]
        nums.sort()
        step = 1
        while nums != A:
            self.nextPermutation(nums)
            step += 1
        return step

    def swapList(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def nextPermutation(self, nums):
        n = len(nums)
        if n <= 1:
            return

        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i != 0:
            j = n - 1
            while nums[j] <= nums[i - 1]:
                j -= 1
            nums[j], nums[i - 1] = nums[i - 1], nums[j]
        self.swapList(nums, i, n - 1)