class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def totalOccurrence(self, A, target):
        if not A:
            return 0

        i = self.find_first_index(A, 0, len(A) - 1, target)
        j = self.find_last_index(A, 0, len(A) - 1, target)

        if i == len(A) or j == len(A):
            return 0

        return j - i + 1

    def find_first_index(self, nums, start, end, target):
        if start > end:
            return start

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return len(nums)

    def find_last_index(self, nums, start, end, target):
        if start > end:
            return start

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[end] == target:
            return end
        if nums[start] == target:
            return start

        return len(nums)