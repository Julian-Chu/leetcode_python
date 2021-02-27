from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 0, len(nums) - 1)

    def quicksort(self, nums, start, end):
        if start >= end:
            return

        left, right = start, end
        pivot = nums[(start + end) // 2]

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


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if nums is None:
            return

        left, right = 0, len(nums) - 1
        i= 0
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1
