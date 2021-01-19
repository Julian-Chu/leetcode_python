class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZeroes(self, nums):
        left, right = 0, 0

        while right < len(nums):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            right += 1

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZeroes(self, nums):
        left = 0

        for i in range(len(nums)):
            while left < len(nums) and nums[left] != 0:
                left += 1
            if nums[i] != 0 and i > left:
                nums[i], nums[left] = nums[left], nums[i]

        return nums