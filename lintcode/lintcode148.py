"""
2x partitioning
"""
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        left, right = 0, len(nums) - 1

        while left <= right:
            while left <= right and nums[left] == 0:
                left += 1
            while left <= right and nums[right] != 0:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        left = left - 1
        right = len(nums) - 1
        while left <= right:
            while left <= right and nums[left] <= 1:
                left += 1
            while left <= right and nums[right] > 1:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1


"""
two pointers
"""
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        left, curr, right = 0, 0, len(nums) - 1
        while curr <= right:
            if nums[curr] == 0:
                nums[curr], nums[left] = nums[left], nums[curr]
                curr += 1
                left += 1
            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else:
                curr += 1

"""
quicksort
"""
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def sortColors(self, nums):
        self.quicksort(nums, 0, len(nums) - 1)

    def quicksort(self, nums, start, end):
        if start >= end:
            return

        left, right = start, end
        pivot = nums[(left + right) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1

            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quicksort(nums, start, right)
        self.quicksort(nums, left, end)