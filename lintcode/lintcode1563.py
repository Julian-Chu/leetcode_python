class Solution:
    """
    @param nums: the array of integers
    @param target:
    @return: the starting and ending position
    """

    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        first = self.find_first(nums, target)
        last = self.find_last(nums, first, target)
        return [first, last]

    def find_first(self, nums, target):
        start, end = 0, len(nums) - 1
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
        return -1

    def find_last(self, nums, start, target):
        start, end = start, len(nums) - 1
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
        return -1